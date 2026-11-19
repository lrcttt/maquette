# python3 verifie.py "<maquette.html>" [préfixe]  -> contrôles bloquants + planches à lire (<p>-m390.png, <p>-d1280.png)
import sys,os,json,subprocess,re,math,html as H
from html.parser import HTMLParser
from PIL import Image
K=os.path.dirname(os.path.abspath(__file__));f=os.path.abspath(sys.argv[1]);p=sys.argv[2] if len(sys.argv)>2 else 'v'
ok=True
def bad(m):
    global ok;ok=False;print('ÉCHEC',m)
b=open(f,'rb').read()
try: b.decode('ascii');print('ASCII ok')
except: bad('fichier non ASCII (lib.finish oublié ?)')
if len(b)>3e6: bad('poids %d Ko > 3 Mo'%(len(b)//1024))
s=b.decode('ascii','replace')
class P(HTMLParser):
    T=('div','section','header','footer','figure','nav','main','article','ul')
    def __init__(x):super().__init__();x.st=[];x.n=0
    def handle_starttag(x,t,a):
        if t in x.T:x.st.append(t)
    def handle_endtag(x,t):
        if t in x.T and (not x.st or x.st.pop()!=t):x.n+=1
q=P();q.feed(s)
if q.n or q.st: bad('balises déséquilibrées (%d, %s)'%(q.n,q.st[-3:]))
else: print('balises ok')
r=json.loads(subprocess.check_output(['node',K+'/chk.js',f,p],cwd=os.getcwd()).decode())
for x in r:
    w=x['w'];pb=[]
    if x['sw']>x['W']: pb.append('débordement de page %s'%x['over'])
    if x['dead']: pb.append('liens vides %s'%x['dead'])
    if x['errs']: pb.append('erreurs JS %s'%x['errs'][:2])
    if x['ext']: pb.append('ressources externes %s'%x['ext'])
    if x['broken']: pb.append('%d images cassées'%x['broken'])
    if not (x['carte'] and x['jlc'] and x['fav']): pb.append('manque carte/jlc/favicon %s'%[x['carte'],x['jlc'],x['fav']])
    if x['modal'] is not True: pb.append('modale %s'%x['modal'])
    if w==390 and x['lines']>2: pb.append('note jaune %d lignes'%x['lines'])
    if pb: bad('%d px : %s'%(w,' ; '.join(pb)))
    else: print(w,'ok',('(débordement interne %s)'%x['over'] if x['over'] else ''),'polices',x['fonts'])
t=H.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(style|script)[^>]*>.*?</\1>','',s)));t=' '.join(t.split())
print('--- règle 7 (regles-v4) : chaque occurrence doit avoir une source (sinon légende neutre)')
for w in ['du jour','maison','de saison','marché','artisanal','frais','depuis','famille','chef']:
    for m in re.finditer(w,t,re.I): print('  [%s] …%s…'%(w,t[max(0,m.start()-45):m.end()+35]))
for w,k in [(390,4),(1280,3)]:
    im=Image.open(f'{p}-{w}.png');h=im.size[1];ch=math.ceil(h/k);o=Image.new('RGB',(w*k+10*k,ch),'white')
    for i in range(k):o.paste(im.crop((0,i*ch,w,min(h,(i+1)*ch))),(i*(w+10),0))
    if w>400:o=o.resize((o.size[0]//2,o.size[1]//2))
    o.save(f'{p}-{"m390" if w==390 else "d1280"}.png')
print('planches :',p+'-m390.png',p+'-d1280.png',' | poids',len(b)//1024,'Ko')
print('RÉSULTAT :','OK' if ok else 'À CORRIGER')
