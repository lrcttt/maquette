// node chk.js <fichier.html> <préfixe> : 390/820/1280, débordement, liens vides, ressources externes, erreurs JS, images cassées, note jaune, modale ; captures pleine page
const {chromium}=require('playwright');
(async()=>{const f=process.argv[2],out=process.argv[3]||'shot';const b=await chromium.launch();const R=[];
for(const w of [390,820,1280]){const p=await b.newPage({viewport:{width:w,height:w==390?844:900}});const errs=[],ext=[];
p.on('pageerror',e=>errs.push(e.message));p.on('request',r=>{const u=r.url();if(!/^(file|data|about):/.test(u))ext.push(u)});
await p.goto('file://'+f);await p.waitForTimeout(700);
const r=await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}window.scrollTo(0,0);
const st=document.createElement('style');st.textContent='.rv{opacity:1!important;transform:none!important}';document.head.appendChild(st);
const W=document.documentElement.clientWidth;const over=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>W+1&&getComputedStyle(e).position!='fixed'&&!e.closest('.rz,.rail,.defile')}).slice(0,5).map(e=>e.tagName+'.'+e.className);
const dead=[...document.querySelectorAll('a')].filter(a=>{const h=a.getAttribute('href');return !h||h=='#'&&!a.classList.contains('logo')}).map(a=>a.textContent.trim().slice(0,20));
const j=document.querySelector('.jaune');let lines=0;if(j){const rg=document.createRange();rg.selectNodeContents(j);lines=new Set([...rg.getClientRects()].map(r=>Math.round(r.top))).size}
const broken=[...document.images].filter(i=>i.complete&&i.naturalWidth==0).length;
return {sw:document.documentElement.scrollWidth,W,over,dead,lines,broken,carte:!!document.querySelector('a[href="#carte"]'),jlc:!!document.querySelector('.jlc'),fav:!!document.querySelector('link[rel=icon]'),fonts:[...new Set([...document.fonts].filter(x=>x.status=='loaded').map(x=>x.family))]}});
await p.waitForTimeout(500);await p.screenshot({path:`${out}-${w}.png`,fullPage:true});
let mo='?';try{await p.locator('[data-resa]').first().click({timeout:3000});await p.waitForTimeout(200);mo=await p.evaluate(()=>{const e=document.getElementById('resa');return e?e.classList.contains('on'):'absente'})}catch(e){mo='erreur'}
R.push({w,...r,errs,ext:ext.slice(0,3),modal:mo});await p.close()}
console.log(JSON.stringify(R));await b.close()})();
