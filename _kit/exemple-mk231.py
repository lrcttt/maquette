# Exemple de maquette autonome (n° 231 Au Bon Porc) : HTML écrit à la main, photos via lib.imgvars, horaires via lib.hours_js, rules2.apply puis lib.finish.
import sys;sys.path.insert(0,'/home/claude/kit');import lib,rules2
D='/home/claude/m231'  # dossier des photos (pull.py)
c=dict(name='Au Bon Porc',tel='03 61 30 80 66',telh='+33361308066',fav=('P','#b3262d','#fff'))
FB='https://www.facebook.com/people/Au-Bon-Porc/61578856079039/'
MAP='https://www.google.com/maps/search/?api=1&query=Au+Bon+Porc+1+rue+du+Banc+Vert+59640+Dunkerque'
H={"1":[[720,870]],"2":[[720,870]],"3":[[720,870]],"4":[[720,870]],"5":[[720,870]]}
fonts=lib.fontface('Bebas Neue','bebas-neue-latin-400-normal',weight='400')+lib.fontface('Work Sans','work-sans-latin-400-normal',weight='400')+lib.fontface('Work Sans','work-sans-latin-600-normal',weight='600')+lib.fontface('Kalam','kalam-latin-400-normal',weight='400')+lib.fontface('Kalam','kalam-latin-700-normal',weight='700')
img=lib.imgvars(D,{'p00':((0,0,1,1),900,70),'p01':((0,.05,1,.85),640,70),'p09':((0,.05,1,.85),640,70),'p11':((0,.05,1,.85),640,70),'p10':((0,.05,1,.85),640,70),'p12':((0,.08,1,.78),560,70),'p13':((0,.1,1,.8),560,70),'p15':((0,.1,1,.9),760,70),'p14':((0,0,1,.85),560,70),'p05':((0,0,1,1),560,68)})
html='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Au Bon Porc · Brasserie, 1 rue du Banc Vert, Dunkerque</title>
<style>'''+fonts+''':root{'''+img+'''--c1:#b3262d;--c2:#b3262d;--c2t:#fff;--rouge:#b3262d;--brique:#8e4a3a;--ard:#26292b;--bois:#9a5a2c;--creme:#f6efe6;--fT:"Bebas Neue",Impact,sans-serif;--fB:"Work Sans",system-ui,sans-serif;--fK:"Kalam",cursive}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font:16px/1.6 var(--fB);color:#2a2321;background:var(--creme);overflow-x:hidden}a{color:inherit}
.brick{background-color:#7d4134;background-image:linear-gradient(90deg,rgba(0,0,0,.18) 2px,transparent 2px),linear-gradient(rgba(0,0,0,.22) 2px,transparent 2px);background-size:56px 28px,100% 28px}
.hero{color:#fff;padding:34px 18px 40px}
.hero .w{max-width:1120px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center}
.carte-v{display:grid;grid-template-columns:.9fr 1.1fr;border-radius:14px;overflow:hidden;box-shadow:0 18px 40px rgba(0,0,0,.4);background:#fff;color:#2a2321;max-width:520px}
.carte-v .lg{display:grid;place-items:center;padding:24px 12px;text-align:center}
.lg .rond{width:128px;height:128px;border-radius:50%;border:5px solid var(--rouge);display:grid;place-items:center;font:400 30px/0.95 var(--fT);color:var(--rouge);letter-spacing:.04em}
.lg .rond small{display:block;font:600 8.5px var(--fB);letter-spacing:.08em;color:#2a2321;margin-top:4px}
.carte-v .rg{background:var(--rouge);color:#fff;padding:24px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.rg h1{font:400 clamp(44px,6vw,62px)/.92 var(--fT);letter-spacing:.03em}
.rg p{font-size:14.5px;opacity:.95}
.hero .tx p.s{font-size:18px;max-width:500px;margin:16px 0 14px;color:#fbe9e2}
.etat{display:inline-flex;align-items:center;gap:8px;font-size:14.5px;background:rgba(0,0,0,.35);padding:5px 12px;border-radius:99px}.etat:before{content:"";width:9px;height:9px;border-radius:50%;background:#bbb}.etat.on:before{background:#62d98e}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15.5px;border:2px solid #fff;color:#fff}.btn svg{width:17px;height:17px}.btn.p{background:#fff;color:var(--rouge);border-color:#fff}
.hero .ph{border-radius:14px;min-height:380px;background:var(--img-p00) center/cover;box-shadow:0 0 0 8px rgba(255,255,255,.12)}
.hero .note{font-size:14px;color:#f3d6cc;margin-top:12px}
@media(max-width:860px){.hero .w{grid-template-columns:1fr;gap:22px}.hero .ph{min-height:250px}.carte-v{max-width:none}}
@media(max-width:420px){.carte-v{grid-template-columns:1fr}.carte-v .lg{padding:16px}.lg .rond{width:104px;height:104px;font-size:25px}}
.band{background:var(--ard);color:#fff;text-align:center;padding:16px 18px;font:400 22px/1.3 var(--fK)}
section{padding:60px 18px}.w{max-width:1100px;margin:0 auto}
.k{font:600 13px var(--fB);letter-spacing:.22em;text-transform:uppercase;color:var(--rouge)}
h2{font:400 clamp(38px,6vw,56px)/1 var(--fT);letter-spacing:.02em;color:#2a2321;margin:4px 0 12px}
.intro .w{display:grid;grid-template-columns:1.1fr .9fr;gap:30px;align-items:center}
.intro p.l{font-size:17.5px;max-width:560px}
.intro ul{list-style:none;margin-top:18px;display:grid;gap:10px}.intro li{background:#fff;border-left:5px solid var(--rouge);padding:10px 14px;border-radius:0 8px 8px 0;font-size:15.5px}.intro li b{display:block;font:400 22px var(--fT);letter-spacing:.04em;color:var(--rouge)}
.intro .ph{min-height:420px;border-radius:12px;background:var(--img-p15) center/cover}
@media(max-width:820px){.intro .w{grid-template-columns:1fr}.intro .ph{min-height:300px}}
.carte{background:#ece2d6}
.cadre{background:var(--bois);padding:14px;border-radius:6px;box-shadow:0 14px 30px rgba(0,0,0,.25);margin-top:22px}
.ardoise{background:var(--ard);color:#f4f4f2;border-radius:2px;padding:26px 28px 20px;display:grid;grid-template-columns:1.25fr 1fr;gap:10px 40px;font-family:var(--fK)}
.ardoise h3{font:700 34px/1.1 var(--fK);text-align:center;text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:2px;margin:6px 0 8px;color:#fff}
.li{display:grid;grid-template-columns:1fr auto;gap:12px;font-size:21px;line-height:1.3;padding:3px 0}.li i{font-style:normal;white-space:nowrap}
.li small{font-size:16px;opacity:.85}
.ardoise .sx{font-size:20px;line-height:1.4}
.ardoise .me{margin-top:16px;font:700 26px var(--fK);text-decoration:underline;text-underline-offset:5px}
@media(max-width:760px){.ardoise{grid-template-columns:1fr;padding:20px 16px}.li{font-size:19px}}
.cnote{font-size:13.5px;color:#5c4f47;margin-top:12px}
.encs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}
.enc{background:#fff;border-radius:10px;padding:18px 18px;border-top:5px solid var(--rouge)}.enc h3{font:400 26px var(--fT);letter-spacing:.03em;color:#2a2321}.enc p{font-size:15px;margin:4px 0 12px}
.enc .btn{color:var(--rouge);border-color:var(--rouge);padding:10px 16px}.enc .btn.p{background:var(--rouge);color:#fff}
@media(max-width:700px){.encs{grid-template-columns:1fr}}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:22px}
.trio figure{border-radius:10px;overflow:hidden;background:#ddd;aspect-ratio:3/4;position:relative}
.trio figure>div{position:absolute;inset:0;background-size:cover;background-position:center}
.trio figcaption{position:absolute;left:8px;bottom:8px;background:rgba(38,41,43,.85);color:#fff;font-size:13px;padding:3px 9px;border-radius:4px}
.trio .t1>div{background-image:var(--img-p01)}.trio .t2>div{background-image:var(--img-p09)}.trio .t3>div{background-image:var(--img-p11)}.trio .t4>div{background-image:var(--img-p10)}.trio .t5>div{background-image:var(--img-p12)}.trio .t6>div{background-image:var(--img-p13)}
@media(max-width:620px){.trio{grid-template-columns:1fr 1fr}}
.bar{display:grid;grid-template-columns:1fr 1fr;min-height:360px}
.bar .a{background:var(--img-p14) center/cover}.bar .a,.bar .b{min-height:340px}.bar .b{background:var(--img-p05) center/cover}
.bar .t{grid-column:1/-1;background:var(--ard);color:#fff;padding:22px 18px;text-align:center}
.bar .t p{font:400 22px/1.35 var(--fK);max-width:760px;margin:0 auto}.bar .t cite{display:block;font:400 14px var(--fB);font-style:normal;color:#f0b9ad;margin-top:6px}
@media(max-width:620px){.bar{min-height:0}.bar .a,.bar .b{min-height:220px}}
.avis .lst{max-width:720px;margin:22px auto 0;display:grid;gap:14px}
.av{background:#fff;border-radius:10px;padding:16px 18px;box-shadow:0 4px 14px rgba(0,0,0,.06)}
.av .st{color:#e0a21b;letter-spacing:2px}.av p{font-size:16px;margin-top:4px}.av cite{display:block;font-style:normal;font-size:14px;color:#7a6a62;margin-top:6px}
.avis .w>h2,.avis .w>.k,.avis .w>.sub{text-align:center}.avis .sub{color:#5c4f47}
.infos{background:var(--rouge);color:#fff}
.infos .w{display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:start}
.infos h2{color:#fff}.infos .k{color:#ffd9cf}
.horaire{background:rgba(0,0,0,.18);border-radius:10px;padding:16px 18px;margin-top:6px}
.horaire b{font:400 26px var(--fT);letter-spacing:.03em;display:block}
#heures{list-style:none;margin-top:8px}#heures li{display:flex;justify-content:space-between;gap:10px;padding:5px 8px;border-bottom:1px solid rgba(255,255,255,.18);font-size:15px}#heures li.auj{background:rgba(255,255,255,.18);border-radius:6px;font-weight:600}#heures span{white-space:nowrap}
.infos .btn{margin-top:4px}
@media(max-width:820px){.infos .w{grid-template-columns:1fr}}
footer{background:var(--ard);color:#ddd;text-align:center;padding:40px 18px 110px;font-size:14.5px}
footer .soc{display:inline-flex;align-items:center;gap:8px;margin-top:12px;border:1px solid rgba(255,255,255,.4);padding:9px 15px;border-radius:8px;text-decoration:none;color:#fff}footer .soc svg{width:18px;height:18px}
.jaune{max-width:640px;margin:22px auto 0;background:#fff3b8;color:#3b3200;border:1px dashed #b89b1a;border-radius:8px;padding:8px 12px;font:400 13px/1.45 system-ui,sans-serif;text-align:left}
.barre{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:repeat(3,1fr);background:var(--ard);border-top:3px solid var(--rouge)}
.barre a{display:flex;flex-direction:column;align-items:center;gap:2px;padding:9px 4px 11px;color:#fff;text-decoration:none;font-size:12.5px;font-weight:600}.barre svg{width:20px;height:20px}
@media(min-width:900px){.barre{display:none}footer{padding-bottom:42px}}
</style></head><body>
<header class="hero brick"><div class="w"><div class="tx">
<div class="carte-v"><div class="lg"><div class="rond">AU BON<br>PORC<small>DUNKERQUE</small></div></div>
<div class="rg"><h1>Au Bon Porc</h1><p>1 rue du Banc Vert<br>59640 Dunkerque</p></div></div>
<p class="s">« Viandes de qualité, plats généreux et ambiance à l'ancienne. »</p>
<span class="etat" id="past"><span id="etat">Cuisine ouverte du lundi au vendredi, le midi</span></span>
<div class="btns"><a class="btn p" href="#carte">Voir la carte</a><a class="btn" href="#resa" data-resa>Réserver</a><a class="btn" href="tel:+33361308066">@@I_TEL@@ Appeler</a></div>
<p class="note">4,7 sur Google · 65 avis</p>
</div><div class="ph" role="img" aria-label="Le bar et la salle d'Au Bon Porc"></div></div></header>
<div class="band">Brasserie · cuisine ouverte du lundi au vendredi, 12&nbsp;h – 14&nbsp;h&nbsp;30</div>
<section class="intro"><div class="w"><div>
<p class="k">La maison</p><h2>Un estaminet au Banc Vert</h2>
<p class="l">Murs de briques, sets de table rouges et cuisine du Nord : potjevleesch, carbonade, camembert rôti. Le plat du jour s'annonce sur la page Facebook.</p>
<ul><li><b>Viandes de qualité</b>et plats généreux, comme le dit la maison.</li><li><b>Un bar à l'entrée</b>« où on peut juste boire une bonne bière », écrit un client.</li><li><b>Le midi en semaine</b>du lundi au vendredi.</li></ul>
</div><div class="ph" role="img" aria-label="Le bar"></div></div></section>
<section class="carte" id="carte"><div class="w">
<p class="k">À l'ardoise</p><h2>La carte</h2>
<p>Recopiée de l'ardoise accrochée au mur (photo de la fiche Google).</p>
<div class="cadre"><div class="ardoise">
<div><h3>Entrées</h3>
<div class="li"><span>Terrine du moment</span><i>5,90 €</i></div>
<div class="li"><span>Croquette de moules</span><i>5,90 €</i></div>
<h3>Plats</h3>
<div class="li"><span>Jambon grillé</span><i>15,50 €</i></div>
<div class="li"><span>Camembert rôti <small>(avec charcuterie)</small></span><i>15,90 €</i></div>
<div class="li"><span>Potjevleesh</span><i>16,90 €</i></div>
<div class="li"><span>Pièce du boucher <small>(≈ 150 g)</small></span><i>18,90 €</i></div>
<div class="li"><span>Fish &amp; Chips</span><i>15,90 €</i></div>
<div class="li"><span>Andouillette de Troyes</span><i>15,90 €</i></div>
<div class="li"><span>Carbonade flamande</span><i>15,90 €</i></div>
</div><div><h3>Desserts</h3>
<div class="li"><span>Café gourmand</span><i>7,90 €</i></div>
<div class="li"><span>Dame blanche</span><i>6,90 €</i></div>
<div class="li"><span>Crème brûlée</span><i>5,90 €</i></div>
<div class="li"><span>Fondant au chocolat</span><i>5,90 €</i></div>
<h3>Accompagnements</h3>
<p class="sx">Frites · pdt grenaille sautées · purée</p>
<h3>Sauces</h3>
<p class="sx">Poivre · échalote · maroilles · moutarde à l'ancienne <small>(si supplément : 1 €)</small></p>
<p class="me">Menu enfant : 9,90 €</p>
</div></div></div>
<div class="encs"><div class="enc"><h3>Le plat du jour, en ligne</h3><p>Vous le changez depuis votre téléphone, il s'affiche ici aussitôt.</p><a class="btn" href="tel:+33361308066">@@I_TEL@@ Demander le plat du jour</a></div>
<div class="enc"><h3>Réserver une table</h3><p>Au 03 61 30 80 66. Le site peut aussi intégrer la réservation en ligne.</p><a class="btn p" href="#resa" data-resa>Réserver</a></div></div>
</div></section>
<section class="gal"><div class="w"><p class="k">Dans l'assiette</p><h2>Vu chez Au Bon Porc</h2>
<div class="trio"><figure class="t1"><div></div><figcaption>Une assiette, frites et salade</figcaption></figure><figure class="t2"><div></div><figcaption>Une assiette et ses frites</figcaption></figure><figure class="t3"><div></div><figcaption>Une assiette en sauce</figcaption></figure><figure class="t4"><div></div><figcaption>Une assiette et ses pommes de terre</figcaption></figure><figure class="t5"><div></div><figcaption>Un dessert glacé</figcaption></figure><figure class="t6"><div></div><figcaption>Un dessert et son café</figcaption></figure></div>
</div></section>
<section class="bar" style="padding:0"><div class="a" role="img" aria-label="Une bière au comptoir"></div><div class="b" role="img" aria-label="Les bouteilles de vin"></div>
<div class="t"><p>« Une belle carte des vins. Un beau bar à l'entrée où on peut juste boire une bonne bière. »</p><cite>Vincent B. · avis Google, février 2026</cite></div></section>
<section class="avis"><div class="w"><p class="k">Avis Google</p><h2>Ils sont passés</h2><p class="sub">4,7 sur Google · 65 avis</p>
<div class="lst">
<div class="av"><div class="st">★★★★★</div><p>« Une excellente découverte à Dunkerque ! […] Le plat du jour et le dessert étaient vraiment délicieux, avec un très bon rapport qualité-prix. L'ambiance y est chaleureuse et le service tout simplement excellent : rapide, souriant et efficace. »</p><cite>Charles S. · juin 2026</cite></div>
<div class="av"><div class="st">★★★★★</div><p>« Le jeune patron qui a repris le restaurant a fait les choses bien ! Une bonne cuisine authentique, franchouillarde comme on aime. »</p><cite>Vincent B. · février 2026</cite></div>
<div class="av"><div class="st">★★★★★</div><p>« Super endroit préservé, authentique comme on en voit hélas de moins en moins. Les plats sont de très bonne qualité. »</p><cite>Laurent S. · novembre 2025</cite></div>
</div></div></section>
<section class="infos" id="infos"><div class="w"><div>
<p class="k">Nous trouver</p><h2>1 rue du Banc Vert</h2>
<p>59640 Dunkerque<br><a href="tel:+33361308066">03 61 30 80 66</a></p>
<div class="btns"><a class="btn p" href="'''+MAP+'''" target="_blank" rel="noopener">@@I_PIN@@ Y aller</a><a class="btn" href="'''+FB+'''" target="_blank" rel="noopener">@@I_FB@@ Facebook</a></div>
</div><div class="horaire"><b>Cuisine ouverte</b><ul id="heures">
<li data-j="1">Lundi <span>12 h – 14 h 30</span></li><li data-j="2">Mardi <span>12 h – 14 h 30</span></li><li data-j="3">Mercredi <span>12 h – 14 h 30</span></li><li data-j="4">Jeudi <span>12 h – 14 h 30</span></li><li data-j="5">Vendredi <span>12 h – 14 h 30</span></li><li data-j="6">Samedi <span>fermé</span></li><li data-j="0">Dimanche <span>fermé</span></li></ul></div>
</div></section>
<footer><p style="font:400 34px var(--fT);color:#fff;letter-spacing:.05em">AU BON PORC</p><p>Brasserie · 1 rue du Banc Vert, Dunkerque</p><a class="soc" href="'''+FB+'''" target="_blank" rel="noopener">@@I_FB@@ Suivre sur Facebook</a>
@@JLC@@<div class="jaune"><b>Note pour vous (maquette) :</b> ardoise et horaires de la fiche Google, à confirmer.</div></footer>
<nav class="barre"><a href="tel:+33361308066">@@I_TEL@@ Appeler</a><a href="#carte">@@I_FL@@ Voir la carte</a><a href="'''+MAP+'''" target="_blank" rel="noopener">@@I_PIN@@ Y aller</a></nav>
<script>'''+lib.hours_js(H)+'''</script>
</body></html>'''
html=rules2.apply(html,c)
lib.finish(html,'/home/claude/Maquette - Au Bon Porc.html')
