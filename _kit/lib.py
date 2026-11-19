import base64,io,json,re,glob,os
from PIL import Image
FD=os.path.dirname(os.path.abspath(__file__))+'/fonts/'
def font(name):
    f=glob.glob(FD+'*/package/files/'+name+'.woff2')
    assert f,name
    return base64.b64encode(open(f[0],'rb').read()).decode()
def fontface(fam,name,style='normal',weight='100 900'):
    return '@font-face{font-family:"%s";font-style:%s;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format("woff2")}'%(fam,style,weight,font(name))
def sheet(outdir,W=300,cols=5):
    fs=sorted(glob.glob(outdir+'/*.jpg'));rows=(len(fs)+cols-1)//cols
    s=Image.new('RGB',(W*cols,rows*400),'white')
    for i,f in enumerate(fs):
        t=Image.open(f);t.thumbnail((W,400));s.paste(t,((i%cols)*W,(i//cols)*400))
    s.save(outdir+'/sheet.png');print([os.path.basename(f) for f in fs])
def data(path,crop=(0,0,1,1),w=800,q=74):
    im=Image.open(path).convert('RGB');W,H=im.size
    im=im.crop((int(crop[0]*W),int(crop[1]*H),int(crop[2]*W),int(crop[3]*H)))
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    b=io.BytesIO();im.save(b,'JPEG',quality=q,optimize=True,progressive=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode(),len(b.getvalue())
def imgvars(outdir,spec):
    tot=0;css=[]
    for k,(c,w,q) in spec.items():
        d,n=data(f'{outdir}/{k}.jpg',c,w,q);tot+=n;css.append('--img-%s:url(%s);'%(k,d))
    print('images',tot//1024,'Ko');return ''.join(css)
I={
'TEL':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
'FL':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>',
'PIN':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
'FB':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.5V4.4a19 19 0 0 0-2.2-.1c-2.3 0-3.9 1.4-3.9 4v2.2H8v3h2.5V21z"/></svg>',
'IG':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg>',
}
def asciify(t):
    def ent(x): return ''.join(c if ord(c)<128 else '&#%d;'%ord(c) for c in x)
    def js(x):
        o=[]
        for c in x:
            n=ord(c)
            if n<128:o.append(c)
            elif n<0x10000:o.append('\\u%04x'%n)
            else:
                n-=0x10000;o.append('\\u%04x\\u%04x'%(0xD800+(n>>10),0xDC00+(n&0x3FF)))
        return ''.join(o)
    def css(x): return ''.join(c if ord(c)<128 else '\\%06x'%ord(c) for c in x)
    out=[];pos=0
    for m in re.finditer(r'(<style[^>]*>)(.*?)(</style>)|(<script[^>]*>)(.*?)(</script>)',t,re.S):
        out.append(ent(t[pos:m.start()]))
        if m.group(1): out.append(m.group(1)+css(m.group(2))+m.group(3))
        else: out.append(m.group(4)+js(m.group(5))+m.group(6))
        pos=m.end()
    out.append(ent(t[pos:]));r=''.join(out);r.encode('ascii');return r
def finish(t,out):
    for k,v in I.items(): t=t.replace('@@I_'+k+'@@',v)
    left=re.findall('@@[A-Za-z_0-9]+@@',t);assert not left,left
    assert 'googleusercontent' not in t
    t=asciify(t)
    open(out,'w',encoding='utf-8').write(t);print(out,len(t.encode())//1024,'Ko')
HOURS_JS='''try{var p=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Paris',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()),o={};p.forEach(function(x){o[x.type]=x.value});var j=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(o.weekday),m=(+o.hour)*60+(+o.minute),H=__H__,N=['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi'];var li=document.querySelector('#heures li[data-j="'+j+'"]');if(li)li.classList.add('auj');function f(x){var h=Math.floor(x/60),mm=x%60;return h+' h'+(mm?' '+(mm<10?'0':'')+mm:'')}var t='',on=false,s=H[String(j)]||[];for(var i=0;i<s.length;i++){if(m>=s[i][0]&&m<s[i][1]){t='Ouvert · jusqu\\'à '+f(s[i][1]);on=true;break}if(m<s[i][0]){t='Fermé · ouvre à '+f(s[i][0]);break}}if(!t){for(var k=1;k<=7;k++){var d=(j+k)%7;if((H[String(d)]||[]).length){t='Fermé · ouvre '+(k==1?'demain':N[d])+' à '+f(H[String(d)][0][0]);break}}}var e=document.getElementById('etat');if(e&&t)e.textContent=t;var pa=document.getElementById('past');if(pa&&on)pa.classList.add('on')}catch(e){}'''
def hours_js(H): return HOURS_JS.replace('__H__',json.dumps(H))
