# python3 audit.py <n°>=<fichier téléchargé> ... : verifie.py sur chaque pièce jointe (préfixe a<n°>)
import sys,subprocess,os
K=os.path.dirname(os.path.abspath(__file__))
for a in sys.argv[1:]:
    n,f=a.split('=',1);print('=====',n);subprocess.run(['python3',K+'/verifie.py',f,'a'+n])
