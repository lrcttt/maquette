# python3 pull.py <fichier tool-results> <dossier> : images (data:image) -> <clé>.jpg ; le reste -> info.json (fusionné)
import json,sys,base64,os
f,out=sys.argv[1],sys.argv[2];os.makedirs(out,exist_ok=True)
a=json.load(open(f));t=a[0]['text'] if isinstance(a,list) else a
t=t.split('\n\n(captured at')[0];d=json.loads(t)
if isinstance(d,str): d=json.loads(d)
info={}
ip=f'{out}/info.json'
if os.path.exists(ip): info=json.load(open(ip))
def walk(k,v):
    if isinstance(v,str) and v.startswith('data:image'):
        b=base64.b64decode(v.split(',',1)[1]);open(f'{out}/{k}.jpg','wb').write(b);print(k,len(b)//1024,'Ko')
    else: info[k]=v
for k,v in d.items():
    if not k.startswith('_'): walk(k,v)
json.dump(info,open(ip,'w'),ensure_ascii=False,indent=1)
if info: print('info:',', '.join(info.keys()))
