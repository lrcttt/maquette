# python3 prepare.py <maquette.html> --nom "Chez Erwan" --note "4,8" --avis 511 --reseaux "Facebook" [--code e8w3q5]
# Kit v6 (18/11/2026). Prépare UN envoi au format « aperçu + lien », sans rien envoyer ni pousser :
#  1. copie la maquette dans /home/claude/maquette/<code>-<slug>/index.html (+ noindex, + compteur GoatCounter si absents)
#  2. capture l'aperçu 390 px (JPEG ≤ 150 Ko) -> envoi/<code>-<slug>/apercu.jpg
#  3. écrit le corps du mail (texte + HTML avec cid:att0) -> envoi/<code>-<slug>/mail.txt / mail.html / infos.json
#  4. lance controle.py (page + mail) : sortie 0 seulement si « CONTROLE : OK »
# --reseaux : ce qui est cité dans le mail, ex. "Facebook", "Instagram", "Facebook et Instagram", "une fiche Google" (si aucun réseau).
# Ensuite (orchestrateur, une fois par vague) : git add/commit/push, attendre, WebFetch de chaque lien, puis envoi.
import sys, os, re, json, secrets, string, unicodedata, subprocess, argparse, html as H

ap = argparse.ArgumentParser()
ap.add_argument('page'); ap.add_argument('--nom', required=True); ap.add_argument('--note', required=True)
ap.add_argument('--avis', required=True); ap.add_argument('--reseaux', required=True); ap.add_argument('--code')
a = ap.parse_args()

REPO = '/home/claude/maquette'; KIT = os.path.dirname(os.path.abspath(__file__))
GC = '<script data-goatcounter="https://julianjulian.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
if not os.path.isdir(os.path.join(REPO, '.git')): sys.exit('ÉCHEC dépôt absent : cloner lrcttt/maquette dans ' + REPO)

slug = unicodedata.normalize('NFKD', a.nom).encode('ascii', 'ignore').decode().lower()
slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')[:40]
code = a.code or ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(6))
dossier = f'{code}-{slug}'; lien = f'https://lrcttt.github.io/maquette/{dossier}/'
dest = os.path.join(REPO, dossier); os.makedirs(dest, exist_ok=True)
out = os.path.join(KIT, 'envoi', dossier); os.makedirs(out, exist_ok=True)

# 1. page
src = open(a.page, encoding='utf-8').read()
if not re.search(r'<meta[^>]+name="robots"', src, re.I):
    src = re.sub(r'(<head[^>]*>)', r'\1<meta name="robots" content="noindex,nofollow">', src, count=1, flags=re.I)
if 'julianjulian.goatcounter.com' not in src:
    src = src.replace('</body>', GC + '\n</body>', 1) if '</body>' in src else src + GC
page = os.path.join(dest, 'index.html'); open(page, 'w', encoding='utf-8').write(src)

# 2. aperçu
from playwright.sync_api import sync_playwright
from PIL import Image
png = os.path.join(out, 'm390.png')
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 390, 'height': 700}, device_scale_factor=2)
    pg.goto('file://' + page); pg.wait_for_timeout(800)
    pg.add_style_tag(content='.rv{opacity:1!important;transform:none!important}'); pg.wait_for_timeout(200)
    pg.screenshot(path=png); b.close()
im = Image.open(png).convert('RGB').resize((390, 700))
jpg = os.path.join(out, 'apercu.jpg')
for q in (85, 78, 70, 62, 55, 48):
    im.save(jpg, 'JPEG', quality=q, optimize=True, progressive=True)
    if os.path.getsize(jpg) <= 150_000: break
os.remove(png)

# 3. mail
note = a.note.replace('.', ',')
lignes1 = ['Bonjour,', '',
           f'{note} sur Google et {a.avis} avis, mais seulement {a.reseaux} quand on vous cherche.',
           f"J'ai préparé gratuitement une maquette de site pour {a.nom}, en voici l'aperçu :"]
lignes2 = [f'La maquette complète est ici : {lien}',
           '(simple page web, rien à télécharger ni à installer)',
           'Le site peut aussi intégrer un système de réservation en ligne.', '',
           'Elle vous plaît ? Je peux vous appeler 5 minutes cette semaine.', '',
           'Julian Lorcet · JLC Service · Création de sites internet · 06 98 23 23 35 · SIREN 132 892 753',
           'Si vous ne souhaitez plus recevoir de message de ma part, répondez simplement STOP.']
txt = '\n'.join(lignes1 + lignes2) + '\n'
open(os.path.join(out, 'mail.txt'), 'w', encoding='utf-8').write(txt)
P = lambda ls: ''.join(f'<p style="margin:0 0 6px">{H.escape(l)}</p>' if l else '<br>' for l in ls)
corps2 = P(lignes2).replace(H.escape(lien), f'<a href="{lien}">{lien}</a>')
img = (f'<p><a href="{lien}"><img src="cid:att0" width="300" alt="Aperçu de la maquette de site pour {H.escape(a.nom)}" '
       'style="border:1px solid #ddd;border-radius:8px;max-width:100%"></a></p>')
htm = f'<div style="font-family:Arial,sans-serif;font-size:15px;color:#222">{P(lignes1)}{img}{corps2}</div>'
open(os.path.join(out, 'mail.html'), 'w', encoding='utf-8').write(htm)
info = {'nom': a.nom, 'lien': lien, 'dossier': dossier, 'objet': f'Une maquette de site pour {a.nom}',
        'apercu': jpg, 'apercu_ko': round(os.path.getsize(jpg) / 1000), 'mail_txt': os.path.join(out, 'mail.txt'),
        'mail_html': os.path.join(out, 'mail.html')}
json.dump(info, open(os.path.join(out, 'infos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 4. contrôle bloquant
r = subprocess.run(['python3', os.path.join(KIT, 'controle.py'), page, '--note', a.note,
                    '--mail', info['mail_txt'], '--lien', lien], capture_output=True, text=True, timeout=120)
print(r.stdout.strip())
print(json.dumps(info, ensure_ascii=False))
if r.returncode != 0:
    print('PRÉPARATION : À CORRIGER (page copiée mais ne pas pousser ni envoyer ; corriger la maquette source et relancer avec --code', code + ')')
sys.exit(r.returncode)
