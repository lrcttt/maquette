# Maquette La Brasserie du Jard (Châlons-en-Champagne) — modèle exemple-mk231.py
import sys;sys.path.insert(0,'/home/claude/kit');import lib,rules2
D='/home/claude/m-la-brasserie-du-jard-6278106'
c=dict(name='La Brasserie du Jard',tel='03 26 65 61 83',telh='+33326656183',fav=('J','#6e3b30','#f1e2cc'))
FB='https://www.facebook.com/p/La-Brasserie-du-Jard-100076256017665/'
IG='https://www.instagram.com/labrasseriedujard/'
MAP='https://www.google.com/maps/search/?api=1&query=La+Brasserie+du+Jard+10+boulevard+Victor+Hugo+51000+Chalons-en-Champagne'
H={"2":[[600,1380]],"3":[[600,1380]],"4":[[600,1380]],"5":[[600,1380]],"6":[[600,1380]],"0":[[600,900]]}
fonts=(lib.fontface('DM Serif Display','dm-serif-display-latin-400-normal',weight='400')
 +lib.fontface('Cormorant Garamond','cormorant-garamond-latin-500-italic',style='italic',weight='500')
 +lib.fontface('Figtree','figtree-latin-400-normal',weight='400')+lib.fontface('Figtree','figtree-latin-600-normal',weight='600')
 +lib.fontface('Figtree','figtree-latin-700-normal',weight='700')+lib.fontface('Kalam','kalam-latin-400-normal',weight='400')
 +lib.fontface('Kalam','kalam-latin-700-normal',weight='700'))
img=lib.imgvars(D,{'p00':((0,0,1,1),900,72),'p01':((0,.06,1,.94),700,70),'p02':((0,0,1,.8),760,70),'p05':((0,.02,1,.92),640,70),'m2':((0,0,1,.72),640,70)})
def L(n,p,d=''):
    return '<div class="pl"><div class="ln"><b>%s</b><i></i><span>%s&nbsp;&euro;</span></div>%s</div>'%(n,p,('<p>%s</p>'%d) if d else '')
carte_g=('<h3>Entrées</h3>'
 +L('Velours d’Automne','8,90','Velouté de potimarron et éclats de châtaigne')
 +L('La Royale Gourmande','11,90','Bouchée à la reine aux escargots')
 +L('Ceviche Twist Agrumes','12,90','Ceviche de thon - vinaigrette aux agrumes – pickles - salade')
 +L('La Tartelette Gasconne','14,50','Tartelette feuilletée au sésame - confit de canard - compotée de pomme - oignons caramélisés - tranche de foie gras')
 +L('Planche de charcuterie','14,90')
 +'<h3>Salades</h3>'
 +L('Poke-bowl Végétarien','14,90','Riz blanc – oignons – tomates – pickles - légumes de saison')
 +L('La Croquante au Chèvre Chaud','15,90','Croustillant de chèvre - lardons grillés - tomates – carottes – noix - pickles de légumes - sauce balsamique')
 +L('Salade du Jard','17,90','P. de terre sautées - gésiers de poulet – pommes - magret fumé – noisettes grillées – tomates - salade')
 +'<h3>Burgers</h3>'
 +L('Le Poulet Effiloché du Chef','16,90','Poulet effiloché – tomates - oignons confits et choux rouges - sauce fromagère – frites maison - salade')
 +L('Le Fish &amp; Bun','17,50','Poisson pané – cheddar – salade – oignons rouges – tomates – sauce burger – frites maison - salade')
 +L('Le Classique du Jard','17,90','Steak haché de bœuf – oignons – tomates – cornichons - cheddar – frites maison - salade')
 +L('Le Montagnard','18,90','Steak haché de bœuf – reblochon - lardons grillés - oignons confits - sauce montagnarde – frites maison - salade')
 +L('Le Burger Hivernal au Foie Gras','19,50','Steak de veau – tranche de foie gras- galette de p. de terre - compotée de pomme - fromage bleu – frites maison - salade'))
carte_d=('<h3>Poissons</h3>'
 +L('Aile de raie Grenobloise','19,50','Aile de raie - sauce grenobloise – croûtons – p. de terre vapeur')
 +L('Saumon des Jardins d’Hiver','19,90','Pavé de saumon rôti - sauce aux poireaux - risotto de cèleri')
 +L('Cabillaud en Habit Vert','20,90','Dos de cabillaud - pesto crémeux - légumes de saison')
 +L('Saint-Jacques au Champagne','21,50','Saint-Jacques poêlé - sauce champagne-citron - risotto au butternut')
 +'<h3>Viandes</h3>'
 +L('Tartare d’Hiver Signature','20,50')
 +L('Douceur d’Agneau au Thym','23,50','Souris d’agneau – confit - sauce au thym - légumes de saison')
 +'<p class="ill">Les autres viandes de la carte sont masquées par un reflet sur la photo : à recopier avec vous.</p>'
 +'<h3>Suppléments</h3>'
 +L('Supplément garniture','3,50','Garnitures : frites maison – salade – pommes de terre sautées – riz – légumes de saison – pennes.')
 +L('Supplément sauce','2,50','Sauces : morilles – à l’orange – champignons – tomates – grenobloise – poireaux – montagnarde – fromagère'))
html='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>La Brasserie du Jard · 10 bd Victor-Hugo, Châlons-en-Champagne</title>
<style>'''+fonts+''':root{'''+img+'''--c1:#6e3b30;--c2:#e3c7a6;--c2t:#3a211b;--brun:#6e3b30;--rouge:#9b2c26;--tan:#e3c7a6;--tan2:#efdcc4;--papier:#fbf8f3;--nuit:#221c19;--pierre:#f2ebe1;--fT:"DM Serif Display",Georgia,serif;--fI:"Cormorant Garamond",Georgia,serif;--fB:"Figtree",system-ui,sans-serif;--fK:"Kalam",cursive}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font:16px/1.6 var(--fB);color:#2c2320;background:var(--pierre);overflow-x:hidden}a{color:inherit}
.top{position:absolute;left:0;right:0;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:14px 18px;max-width:1180px;margin:0 auto}
.top .soc2{display:flex;gap:8px}.top .soc2 a{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:rgba(34,28,25,.55);color:#fff}.top .soc2 svg{width:18px;height:18px}
.hero{position:relative;background:var(--nuit);color:#fff;overflow:hidden}
.hero-w{display:grid;grid-template-columns:1.05fr .95fr;min-height:640px;max-width:1280px;margin:0 auto}
.hero-ph{background:var(--img-p00) center 40%/cover;min-height:640px}
.hero-tx{display:flex;flex-direction:column;justify-content:center;padding:80px 48px 48px}
.plaque{position:relative;background:var(--tan);color:#2a1a15;padding:34px 30px 28px;max-width:470px;text-align:center;box-shadow:0 20px 40px rgba(0,0,0,.45)}
.plaque:before,.plaque:after{content:"";position:absolute;left:12px;right:12px;height:0;border-top:1.5px solid var(--brun)}
.plaque:before{top:12px}.plaque:after{bottom:12px}
.plaque>.vl,.plaque>.vr{position:absolute;top:6px;bottom:6px;border-left:1.5px solid var(--brun)}.plaque>.vl{left:20px}.plaque>.vr{right:20px}
.plaque .pt{font:600 15px var(--fB);letter-spacing:.32em;text-transform:uppercase}
.plaque h1{font:400 clamp(46px,6.4vw,70px)/.95 var(--fT);letter-spacing:.02em;font-variant:small-caps;margin:2px 0 10px}
.plaque .ad{font-size:15px;color:#4a2f27}
.hero-tx .q{font:italic 500 23px/1.35 var(--fI);color:#f1e2cc;max-width:470px;margin:22px 0 4px}.hero-tx .qa{font-size:13.5px;color:#cbb59c}
.etat{display:inline-flex;align-items:center;gap:8px;font-size:14.5px;background:rgba(255,255,255,.1);padding:6px 13px;border-radius:99px;margin-top:18px;align-self:flex-start}.etat:before{content:"";width:9px;height:9px;border-radius:50%;background:#bbb}.etat.on:before{background:#68d28f}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:4px;text-decoration:none;font-weight:600;font-size:15.5px;border:1.5px solid currentColor}.btn svg{width:17px;height:17px}
.hero .btn{color:#fff}.hero .btn.p{background:var(--tan);color:#2a1a15;border-color:var(--tan)}
.hero .nt{font-size:14px;color:#cbb59c;margin-top:12px}.nt .st{color:#e7b24a;letter-spacing:1px}
@media(max-width:900px){.hero-w{grid-template-columns:1fr;min-height:0}.hero-ph{min-height:340px;order:-1}.hero-tx{padding:0 18px 40px}.plaque{margin-top:-60px;max-width:none}}
@media(max-width:420px){.plaque{padding:28px 22px 22px}.plaque .pt{font-size:13px}}
.band{background:var(--brun);color:#f6e6d2;text-align:center;padding:14px 18px;font-size:15.5px;letter-spacing:.02em}
section{padding:64px 18px}.w{max-width:1120px;margin:0 auto}
.k{font:700 12.5px var(--fB);letter-spacing:.24em;text-transform:uppercase;color:var(--rouge)}
h2{font:400 clamp(36px,5.4vw,52px)/1.05 var(--fT);color:#2a1a15;margin:6px 0 14px}
.maison .w{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.maison p.l{font-size:17.5px;max-width:540px}
.reperes{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:22px}
.rep{background:var(--papier);border-top:3px solid var(--brun);padding:14px 14px 12px}.rep b{display:block;font:400 21px/1.15 var(--fT);color:var(--brun);margin-bottom:4px}.rep span{font-size:14.5px}
.maison .duo{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.duo>div{min-height:420px;background-size:cover;background-position:center}
.duo .d1{background-image:var(--img-p02)}.duo .d2{background-image:var(--img-p05);margin-top:40px}
@media(max-width:860px){.maison .w{grid-template-columns:1fr}.reperes{grid-template-columns:1fr}.duo>div{min-height:300px}.duo .d2{margin-top:24px}}
.carte{background:var(--nuit);color:#fff}
.carte h2{color:#fff}.carte .k{color:var(--tan)}.carte .w>p.s{color:#d9c9b6;max-width:640px}
.livret{background:var(--papier);color:#2c2320;margin-top:26px;padding:34px 34px 30px;position:relative;box-shadow:0 20px 40px rgba(0,0,0,.4)}
.livret:before{content:"";position:absolute;inset:10px;border:1.5px solid #8c5a4b;pointer-events:none}
.livret-h{text-align:center;margin-bottom:8px}.livret-h small{font:600 13px var(--fB);letter-spacing:.3em}.livret-h strong{display:block;font:400 34px/1 var(--fT);font-variant:small-caps}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:6px 48px}
.cols h3{font:700 15px var(--fB);letter-spacing:.14em;text-transform:uppercase;text-decoration:underline;text-underline-offset:5px;text-align:center;margin:22px 0 10px;color:#2a1a15}
.pl{padding:5px 0}.ln{display:flex;align-items:baseline;gap:8px}.ln b{font-weight:700;font-size:16px}.ln i{flex:1;border-bottom:2px dotted #b49a87;transform:translateY(-4px);min-width:16px}.ln span{white-space:nowrap;font-weight:700}
.pl p{font-size:14.5px;color:#5a4a42;line-height:1.45}
.ill{font-size:13.5px;font-style:italic;color:#7a6257;margin-top:6px}
@media(max-width:760px){.cols{grid-template-columns:1fr}.livret{padding:26px 18px 22px}.ln b{font-size:15.5px}}
.champ{margin-top:22px;display:grid;grid-template-columns:1.1fr .9fr;gap:0;background:var(--tan2);color:#2a1a15}
.champ .cx{padding:26px 28px;font-family:var(--fK)}
.champ h3{font:700 30px/1.1 var(--fK);letter-spacing:.04em}.champ .fm{font:400 18px var(--fK);margin:8px 0 6px}.champ .fm b{letter-spacing:.06em}
.champ .ln b{font:400 18px/1.3 var(--fK)}.champ .ln span{font:700 18px var(--fK)}.champ .ln i{border-color:#9c7d66}
.champ .ph{background:var(--img-m2) center top/cover;min-height:320px}
@media(max-width:760px){.champ{grid-template-columns:1fr}.champ .cx{padding:22px 18px}.champ .ph{min-height:260px}}
.cnote{font-size:13.5px;color:#cdbba6;margin-top:14px}
.encs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}
.enc{border:1.5px solid rgba(227,199,166,.5);padding:18px}.enc h3{font:400 25px var(--fT);color:var(--tan)}.enc p{font-size:15px;margin:4px 0 12px;color:#e9dccd}
.enc .btn{color:var(--tan);padding:10px 16px}.enc .btn.p{background:var(--tan);color:#2a1a15;border-color:var(--tan)}
@media(max-width:700px){.encs{grid-template-columns:1fr}}
.assiette{display:grid;grid-template-columns:1fr 1fr;min-height:480px;padding:0}
.assiette .ph{background:var(--img-p01) center/cover;min-height:420px}
.assiette .tx{background:var(--tan);display:flex;flex-direction:column;justify-content:center;padding:40px 44px}
.assiette blockquote{font:italic 500 26px/1.35 var(--fI);color:#2a1a15}.assiette cite{display:block;font:400 14px var(--fB);font-style:normal;margin-top:12px;color:#5a3a30}
@media(max-width:760px){.assiette{grid-template-columns:1fr}.assiette .ph{min-height:300px}.assiette .tx{padding:28px 18px}.assiette blockquote{font-size:22px}}
.avis .w>h2,.avis .w>.k,.avis .w>.sub{text-align:center}.avis .sub{color:#5a4a42}
.avl{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}
.av{background:var(--papier);padding:20px 20px 16px;border-bottom:3px solid var(--brun)}
.av .st{color:#d89a1e;letter-spacing:2px}.av p{font-size:15.5px;margin-top:6px}.av cite{display:block;font-style:normal;font-size:13.5px;color:#7a6257;margin-top:10px}
@media(max-width:860px){.avl{grid-template-columns:1fr}}
.infos{background:var(--brun);color:#fff}
.infos .w{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:start}
.infos h2{color:#fff}.infos .k{color:var(--tan)}.infos p{color:#f3e4d3}
.infos .btn{color:#fff}.infos .btn.p{background:var(--tan);color:#2a1a15;border-color:var(--tan)}
.horaire{background:rgba(0,0,0,.2);padding:18px 20px}
.horaire b{font:400 25px var(--fT);display:block}
#heures{list-style:none;margin-top:8px}#heures li{display:flex;justify-content:space-between;gap:10px;padding:6px 8px;border-bottom:1px solid rgba(255,255,255,.16);font-size:15px}#heures li.auj{background:rgba(255,255,255,.16);font-weight:600}#heures span{white-space:nowrap}
@media(max-width:820px){.infos .w{grid-template-columns:1fr}}
footer{background:var(--nuit);color:#d8cbbd;text-align:center;padding:44px 18px 110px;font-size:14.5px}
footer .fl{font:600 12px var(--fB);letter-spacing:.3em}footer .fn{font:400 36px/1 var(--fT);font-variant:small-caps;color:#fff;margin:2px 0 8px}
footer .socs{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:14px}
footer .soc{display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(255,255,255,.4);padding:9px 15px;text-decoration:none;color:#fff}footer .soc svg{width:18px;height:18px}
.jaune{max-width:640px;margin:22px auto 0;background:#fff3b8;color:#3b3200;border:1px dashed #b89b1a;border-radius:8px;padding:8px 12px;font:400 13px/1.45 system-ui,sans-serif;text-align:left}
.barre{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:repeat(3,1fr);background:var(--nuit);border-top:3px solid var(--tan)}
.barre a{display:flex;flex-direction:column;align-items:center;gap:2px;padding:9px 4px 11px;color:#fff;text-decoration:none;font-size:12.5px;font-weight:600}.barre svg{width:20px;height:20px}
@media(min-width:900px){.barre{display:none}footer{padding-bottom:44px}}
</style></head><body>
<header class="hero"><div class="top"><span></span><div class="soc2"><a href="'''+FB+'''" target="_blank" rel="noopener" aria-label="Facebook">@@I_FB@@</a><a href="'''+IG+'''" target="_blank" rel="noopener" aria-label="Instagram">@@I_IG@@</a></div></div>
<div class="hero-w"><div class="hero-tx">
<div class="plaque"><span class="vl"></span><span class="vr"></span><p class="pt">La Brasserie</p><h1>Du Jard</h1><p class="ad">10 boulevard Victor-Hugo · Châlons-en-Champagne</p></div>
<p class="q">« Très bel édifice face au beau jardin du château , belle déco intérieure […] On s'y sent bien et on a envie de revenir ! »</p><p class="qa">Jocelyne H. · avis Google, octobre 2026</p>
<span class="etat" id="past"><span id="etat">Ouvert du mardi au dimanche</span></span>
<div class="btns"><a class="btn p" href="#carte">Voir la carte</a><a class="btn" href="#resa" data-resa>Réserver</a><a class="btn" href="tel:+33326656183">@@I_TEL@@ Appeler</a></div>
<p class="nt"><span class="st">★★★★☆</span> 4,3 sur Google · 595 avis</p>
</div><div class="hero-ph" role="img" aria-label="La salle de La Brasserie du Jard, chaises rouges et étagères en bois"></div></div></header>
<div class="band">Du mardi au samedi, 10&nbsp;h – 23&nbsp;h · le dimanche, 10&nbsp;h – 15&nbsp;h · fermé le lundi</div>
<section class="maison"><div class="w"><div>
<p class="k">La maison</p><h2>Une brasserie, des champagnes</h2>
<p class="l">Une carte d’automne, des burgers, des poissons et les champagnes de la Famille Carbot, servis dans une salle aux chaises rouges et aux murs d’étagères en bois, ou sur la terrasse.</p>
<div class="reperes"><div class="rep"><b>Famille Carbot</b><span>Champagne à la coupe ou à la bouteille.</span></div><div class="rep"><b>La terrasse</b><span>« très agréable », écrit un client.</span></div><div class="rep"><b>Mardi → dimanche</b><span>Fermé le lundi.</span></div></div>
</div><div class="duo"><div class="d1" role="img" aria-label="Une coupe de champagne Carbot en terrasse"></div><div class="d2" role="img" aria-label="Les cartes affichées à l'entrée"></div></div></div></section>
<section class="carte" id="carte"><div class="w">
<p class="k">La carte</p><h2>Au menu en ce moment</h2>
<p class="s">Recopiée de la carte d’automne photographiée sur la fiche Google.</p>
<div class="livret"><div class="livret-h"><small>LA BRASSERIE</small><strong>Du Jard</strong></div>
<div class="cols"><div>'''+carte_g+'''</div><div>'''+carte_d+'''</div></div></div>
<div class="champ"><div class="cx"><h3>CHAMPAGNES</h3><p class="fm">❖ <b>FAMILLE CARBOT</b> · coupe 12 cl</p>
<div class="pl"><div class="ln"><b>BRUT Grande Réserve ‘Cuvée Violette’</b><i></i><span>9,50&nbsp;&euro;</span></div></div>
<div class="pl"><div class="ln"><b>BRUT Premier Cru Rosé ‘Cuvée Lilly’</b><i></i><span>10,50&nbsp;&euro;</span></div></div>
<div class="pl"><div class="ln"><b>BRUT Grand Cru Blanc de Blancs ‘Cuvée Pierre’</b><i></i><span>11,50&nbsp;&euro;</span></div></div>
<p class="fm" style="margin-top:12px">Et à la bouteille : Famille Carbot, Joseph Perrier, Moet &amp; Chandon, Veuve Clicquot.</p></div>
<div class="ph" role="img" aria-label="La carte des champagnes de la brasserie"></div></div>
<p class="cnote">Carte relevée sur une photo de la fiche Google, prix à confirmer.</p>
<div class="encs"><div class="enc"><h3>Vos suggestions, en ligne</h3><p>Vous changez la suggestion du moment depuis votre téléphone, elle s’affiche ici aussitôt.</p><a class="btn" href="tel:+33326656183">@@I_TEL@@ Demander les suggestions</a></div>
<div class="enc"><h3>Réserver une table</h3><p>Au 03 26 65 61 83. Le site peut aussi intégrer la réservation en ligne.</p><a class="btn p" href="#resa" data-resa>Réserver</a></div></div>
</div></section>
<section class="assiette"><div class="ph" role="img" aria-label="Une assiette de poisson"></div><div class="tx">
<p class="k">Dans l’assiette</p><blockquote>« La Saint-Jacques au Champagne est un vrai régal, la cuisson parfaite , sauce fine et parfumée. le Tartare d’Hiver Signature est très bien assaisonné. »</blockquote><cite>Brynhild F. · avis Google, novembre 2025</cite></div></section>
<section class="avis"><div class="w"><p class="k">Avis Google</p><h2>Ils sont passés au Jard</h2><p class="sub"><span style="color:#d89a1e">★★★★☆</span> 4,3 sur Google · 595 avis</p>
<div class="avl">
<div class="av"><div class="st">★★★★★</div><p>« Très bel édifice face au beau jardin du château , belle déco intérieure , la cuisine est très bonne et le service attentif. Les prix sont très corrects . Lieu calme . »</p><cite>Jocelyne H. · octobre 2026</cite></div>
<div class="av"><div class="st">★★★★★</div><p>« […] d'excellents plats, génèreux, savoureux et un très bon moment dans ce beau cadre, tout était parfait ! »</p><cite>Yannick V. · avril 2026</cite></div>
<div class="av"><div class="st">★★★★★</div><p>« Le cadre est également très joli, avec une décoration soignée et chaleureuse. Et mention spéciale pour le champagne, qui était tout simplement excellent ! »</p><cite>Clara · février 2026</cite></div>
</div></div></section>
<section class="infos" id="infos"><div class="w"><div>
<p class="k">Nous trouver</p><h2>10 boulevard Victor-Hugo</h2>
<p>51000 Châlons-en-Champagne<br><a href="tel:+33326656183">03 26 65 61 83</a></p>
<div class="btns"><a class="btn p" href="'''+MAP+'''" target="_blank" rel="noopener">@@I_PIN@@ Y aller</a><a class="btn" href="#resa" data-resa>Réserver</a></div>
</div><div class="horaire"><b>Horaires d’ouverture</b><ul id="heures">
<li data-j="1">Lundi <span>fermé</span></li><li data-j="2">Mardi <span>10 h – 23 h</span></li><li data-j="3">Mercredi <span>10 h – 23 h</span></li><li data-j="4">Jeudi <span>10 h – 23 h</span></li><li data-j="5">Vendredi <span>10 h – 23 h</span></li><li data-j="6">Samedi <span>10 h – 23 h</span></li><li data-j="0">Dimanche <span>10 h – 15 h</span></li></ul></div>
</div></section>
<footer><p class="fl">LA BRASSERIE</p><p class="fn">Du Jard</p><p>Brasserie · 10 boulevard Victor-Hugo, Châlons-en-Champagne</p>
<div class="socs"><a class="soc" href="'''+FB+'''" target="_blank" rel="noopener">@@I_FB@@ Facebook</a><a class="soc" href="'''+IG+'''" target="_blank" rel="noopener">@@I_IG@@ Instagram</a></div>
@@JLC@@<div class="jaune"><b>Note pour vous (maquette) :</b> carte et horaires relevés sur la fiche Google, à confirmer.</div></footer>
<nav class="barre"><a href="tel:+33326656183">@@I_TEL@@ Appeler</a><a href="#carte">@@I_FL@@ Voir la carte</a><a href="'''+MAP+'''" target="_blank" rel="noopener">@@I_PIN@@ Y aller</a></nav>
<script>'''+lib.hours_js(H)+'''</script>
</body></html>'''
html=rules2.apply(html,c)
lib.finish(html,'/home/claude/Maquette - La Brasserie du Jard.html')
