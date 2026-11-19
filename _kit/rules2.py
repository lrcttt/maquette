# Règles 3, 4, 6 (version session 17/11 midi) : favicon, modale de réservation de démo, section « Ce site vous plaît ? »
# Le HTML doit contenir @@JLC@@ (avant la note jaune) ; les boutons de réservation portent data-resa.
import urllib.parse
def apply(t,c):
    tel=c['tel'];telh=c['telh'];L,bg,fg=c['fav']
    svg=f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='{bg}'/><text x='32' y='45' text-anchor='middle' font-family='Georgia,serif' font-size='38' font-weight='700' fill='{fg}'>{L}</text></svg>"
    t=t.replace('</title>','</title>\n<link rel="icon" href="data:image/svg+xml,'+urllib.parse.quote(svg)+'">',1)
    css='''.rz{position:fixed;inset:0;z-index:98;background:rgba(10,10,12,.7);display:none;place-items:center;padding:16px}.rz.on{display:grid}
.rz form{background:#fffdf8;color:#1d1d1d;border-radius:16px;padding:22px 20px;width:min(420px,100%);max-height:92vh;overflow:auto;display:grid;gap:10px;font:15px/1.4 var(--fB,system-ui)}
.rz h4{font:600 24px var(--fT,inherit);color:var(--c1)}.rz .dm{background:#fff3b8;border:1px dashed #b89b1a;color:#3b3200;border-radius:8px;padding:8px 10px;font:400 13px/1.4 system-ui,sans-serif}
.rz label{display:grid;gap:4px;font-weight:600;font-size:13.5px}.rz input,.rz select{font:inherit;padding:10px 12px;border:1.5px solid #c9c9c9;border-radius:10px;background:#fff;width:100%;min-width:0}
.rz .two{display:grid;grid-template-columns:1fr 1fr;gap:10px}.rz button{font:600 16px var(--fB,inherit);padding:13px;border-radius:99px;border:0;background:var(--c1);color:#fff;cursor:pointer}
.rz .x{background:none;color:#666;padding:6px;font-weight:500;font-size:14px}.rz .ok{display:none;text-align:center;padding:10px 0}.rz.done .ok{display:block}.rz.done .f{display:none}
.jlc{margin:34px auto 0;max-width:640px;border:1px solid var(--jb,rgba(255,255,255,.25));border-radius:16px;padding:22px 20px;text-align:center}.jlc h4{font:600 26px var(--fT,inherit);color:var(--jt,#fff)}.jlc p{color:var(--jp,#cfcfcf);font-size:15px;margin-top:4px}
.jlc .lk{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-top:14px}.jlc .lk a{display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border-radius:99px;text-decoration:none;font-weight:600;font-size:15px;border:1px solid var(--jb,rgba(255,255,255,.4));color:var(--jt,#fff)}.jlc .lk a.p{background:var(--c2);color:var(--c2t,#fff);border-color:var(--c2)}.jlc .lk svg{width:16px;height:16px}'''
    t=t.replace('</head>','<style>'+css+'</style></head>',1)
    modal=f'''<div class="rz" id="resa" role="dialog" aria-label="Réserver une table"><form novalidate>
<div class="f"><h4>Réserver une table</h4>
<p class="dm">Démo — la réservation en ligne sera active sur votre vrai site.</p>
<div class="two"><label>Date<input type="date"></label><label>Heure<input type="time" value="12:30"></label></div>
<label>Nombre de couverts<select><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8 et plus</option></select></label>
<label>Nom<input type="text" autocomplete="name"></label><label>Téléphone<input type="tel" autocomplete="tel"></label>
<button type="submit">Envoyer la demande</button>
<p style="text-align:center;font-size:14px">ou par téléphone&nbsp;: <a href="tel:{telh}">{tel}</a></p></div>
<div class="ok"><h4>Demande enregistrée (démo)</h4><p>Sur le vrai site, le restaurant reçoit la demande et la confirme. Rien n'a été envoyé.</p></div>
<button type="button" class="x">Fermer</button></form></div>'''
    js='''<script>(function(){var z=document.getElementById('resa');if(!z)return;var f=z.querySelector('form');
document.querySelectorAll('[data-resa]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();z.classList.remove('done');z.classList.add('on')})});
z.querySelector('.x').addEventListener('click',function(){z.classList.remove('on','done')});
z.addEventListener('click',function(e){if(e.target===z){z.classList.remove('on','done')}});
f.addEventListener('submit',function(e){e.preventDefault();z.classList.add('done')});})();</script>'''
    i=t.rindex('</body>');t=t[:i]+modal+js+t[i:]
    fin='''<div class="jlc"><h4>Ce site vous plaît&nbsp;?</h4><p>Julian Lorcet · JLC Service · Création de sites internet</p>
<div class="lk"><a class="p" href="tel:+33698232335">@@I_TEL@@ 06 98 23 23 35</a><a href="https://lrcttt.github.io/maquette/" target="_blank" rel="noopener">JLC Service</a></div></div>
'''
    assert '@@JLC@@' in t and 'data-resa' in t
    t=t.replace('@@JLC@@',fin,1)
    return t
