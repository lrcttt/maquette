# python3 controle.py <maquette.html> --note "4,8" [--mail corps.txt] [--lien URL]
# Contrôle BLOQUANT avant envoi (kit v6, 18/11/2026). Doit finir par « CONTROLE : OK ».
# Vérifie la page publiée (texte visible, étoiles, barre fixe, prix de Jul, compteur, noindex, bouton carte, réseaux)
# et le corps du mail (lien, STOP, SIREN, réseaux cités = liens de la page, aucun prix, aucune pièce jointe annoncée).
import sys, re, html, argparse

ap = argparse.ArgumentParser()
ap.add_argument('page'); ap.add_argument('--note', required=True)
ap.add_argument('--mail'); ap.add_argument('--lien')
a = ap.parse_args()
erreurs = []
def bad(m): erreurs.append(m)

src = open(a.page, encoding='utf-8', errors='replace').read()
note = float(a.note.replace(',', '.'))

# --- texte visible (sans style ni script), décodé une fois
corps = re.sub(r'(?is)<(style|script)[^>]*>.*?</\1>', ' ', src)
visible = html.unescape(re.sub(r'<[^>]+>', ' ', corps))
visible = ' '.join(visible.split())

# 1. restes d'encodage visibles
for motif in ['nbsp;', '&#', '&amp;', '&quot;', '&lt;', '&gt;', '@@']:
    if motif in visible:
        i = visible.find(motif); bad(f'texte visible contient « {motif} » : …{visible[max(0,i-40):i+30]}…')

# 2. étoiles : 5 étoiles pleines à côté de la note globale alors que la note < 5
# (accepté : étoiles pâles + calque partiel width:X% avec X ≈ note/5×100)
if note < 4.95:
    brut = src.replace('&#9733;', '★')
    attendu = note / 5 * 100
    for m in re.finditer(r'★★★★★', brut):
        if re.search(r'class="(st|av)"', brut[max(0, m.start()-120):m.start()]): continue   # étoiles d'un avis 5/5, pas de la note
        avant = re.sub(r'<[^>]+>', ' ', brut[max(0, m.start()-1500):m.start()])
        if not re.search(r'\d[,.]\d', avant[-200:]): continue      # pas à côté d'une note
        zone = brut[max(0, m.start()-400):m.end()+400]
        w = [float(x) for x in re.findall(r'width:\s*(\d+(?:\.\d+)?)%', zone)]
        if not any(abs(x - attendu) <= 3 for x in w):
            bad(f'5 étoiles pleines près d\'une note {a.note} sans calque partiel ≈{attendu:.0f}%'); break

# 3. barre ou élément fixe visible sur ordinateur (hors modale de réservation .rz)
css = ' '.join(re.findall(r'(?is)<style[^>]*>(.*?)</style>', src))
css = re.sub(r'data:[^)"\']{200,}', 'data:', css)          # images base64 retirées (sinon regex très lente)
css_plat = re.sub(r'\s+', ' ', css)
fixes = set()
for m in re.finditer(r'([^{}]{1,300})\{([^{}]{0,2000})\}', css_plat):
    if not re.search(r'position\s*:\s*fixed', m.group(2)): continue
    for sel in m.group(1).split(','):
        sel = sel.strip()
        if sel.startswith('@') or not sel: continue
        if re.search(r'\.rz\b|#resa', sel): continue
        fixes.add(sel)
for sel in fixes:
    cache = False
    for mq in re.finditer(r'@media\s*\(\s*min-width\s*:\s*(\d+)px\s*\)\s*\{(.*?\})\s*\}', css_plat):
        if int(mq.group(1)) <= 1024 and re.search(re.escape(sel) + r'\s*\{[^}]*display\s*:\s*none', mq.group(2)):
            cache = True
    if not cache:
        bad(f'élément fixe « {sel} » non masqué sur ordinateur (pas de @media(min-width:≤1024px){{{sel}{{display:none}}}})')

# 4. prix / abonnement de Jul jamais dans la page
for motif in [r'/\s*mois', r'par mois', r'abonnement', r'engagement']:
    if re.search(motif, visible, re.I):
        bad(f'la page parle de prix / abonnement (« {motif} »)')

# 5. compteur, noindex, bouton carte, ressources
if 'data-goatcounter="https://julianjulian.goatcounter.com/count"' not in src: bad('compteur GoatCounter absent')
if not re.search(r'<meta[^>]+name="robots"[^>]+noindex', src, re.I): bad('balise noindex absente')
if not re.search(r'href="#carte"', src): bad('bouton « Voir la carte » (href="#carte") absent')
if 'googleusercontent' in src: bad('image liée à Google (googleusercontent) au lieu d\'être intégrée')

# 6. réseaux réellement liés
fb = bool(re.search(r'href="https?://(www\.|m\.)?facebook\.com/', src))
ig = bool(re.search(r'href="https?://(www\.)?instagram\.com/', src))

# --- mail
if a.mail:
    m = open(a.mail, encoding='utf-8').read()
    if 'STOP' not in m: bad('mail : ligne STOP absente')
    if 'SIREN 132 892 753' not in m: bad('mail : SIREN absent de la signature')
    if '€' in m or re.search(r'/\s*mois|abonnement', m, re.I): bad('mail : prix ou abonnement mentionné')
    if re.search(r'pi[eè]ce jointe', m, re.I): bad('mail : annonce une pièce jointe (format lien attendu)')
    liens = re.findall(r'https://lrcttt\.github\.io/maquette/[a-z0-9-]+/', m)
    if not liens: bad('mail : lien vers la maquette en ligne absent')
    elif a.lien and a.lien not in liens: bad(f'mail : le lien {liens[0]} ≠ page vérifiée {a.lien}')
    dit_fb = 'Facebook' in m; dit_ig = 'Instagram' in m
    if dit_fb != fb or dit_ig != ig:
        bad(f'mail : réseaux cités (Facebook={dit_fb}, Instagram={dit_ig}) ≠ liens de la page (Facebook={fb}, Instagram={ig})')

print(f'réseaux liés : Facebook={fb} Instagram={ig} · éléments fixes : {sorted(fixes) or "aucun"}')
for e in erreurs: print('ÉCHEC', e)
print('CONTROLE :', 'OK' if not erreurs else f'À CORRIGER ({len(erreurs)})')
sys.exit(0 if not erreurs else 1)
