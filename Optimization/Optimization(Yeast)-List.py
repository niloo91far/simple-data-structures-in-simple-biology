#Exercise No3.: Optimization based on the host (here, YEAST)

prot='MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIMMTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM'

#RNA Codes
phe = ['uuu','uuc']
leu = ['uua','uug','cuu','cuc','cua','cug']
ile = ['auu','auc','aua']
met = ['aug']
val = ['guu','guc','gua','gug']
ser = ['ucu','ucc','uca','ucg','agu','agc']
pro = ['ccu','ccc','cca','ccg']
thr = ['acu','acc','aca','acg']
ala = ['gcu','gcc','gca','gcg']
tyr = ['uau','uac']
his = ['cau','cac']
gln = ['caa','cag']
asn = ['aau','aac']
lys = ['aaa','aag']
asp = ['gau','gac']
glu = ['gaa','gag']
cys = ['ugu','ugc']
trp = ['ugg']
arg = ['cgu','cgc','cga','cgg','aga','agg']
gly = ['ggu','ggc','gga','ggg']
stop = ['uaa','uag','uga']

allcode3 = [phe,leu,ile,met,val,ser,pro,thr,ala,tyr,
            his,gln,asn,lys,asp,glu,cys,trp,arg,gly]

aacode = ['F','L','I','M','V','S','P','T','A','Y','H',
          'Q','N','K','D','E','C','W','R','G']

#yeast DNA codon frequency
pheF = [0.59,0.41]
leuF = [0.28,0.29,0.13,0.06,0.14,0.11]
ileF = [0.46,0.26,0.27]
metF = [1.00]
valF = [0.39,0.21,0.21,0.19]
serF = [0.26,0.16,0.21,0.10,0.16,0.11]
proF = [0.31,0.15,0.41,0.12]
thrF = [0.35,0.22,0.30,0.13]
alaF = [0.38,0.22,0.29,0.11]
tyrF = [0.56,0.44]
hisF = [0.64,0.36]
glnF = [0.69,0.31]
asnF = [0.59,0.41]
lysF = [0.58,0.42]
aspF = [0.65,0.35]
gluF = [0.71,0.29]
cysF = [0.63,0.37]
trpF = [1.00]
argF = [0.15,0.06,0.07,0.04,0.48,0.21]
glyF = [0.47,0.19,0.22,0.12]
stopF = [0.48,0.24,0.29]

allcode3F = [pheF,leuF,ileF,metF,valF,serF,proF,thrF,alaF,tyrF,
            hisF,glnF,asnF,lysF,aspF,gluF,cysF,trpF,argF,glyF]

mrna_seq=[]
dna_seq=[]

for p in prot:
    for index,aa in enumerate(aacode):
        if p==aa:
            opt=allcode3F[index].index(max(allcode3F[index]))
            mrna_seq.append(allcode3[index][opt])

mrna_seq = ''.join(mrna_seq)
dna_seq=mrna_seq

for i in range(len(mrna_seq)):
    if mrna_seq[i]=='u':
        dna_seq= dna_seq.replace(dna_seq[i],'t')


print("Probably DNA sequence of YEAST based on the given protein sequence: ")
print(dna_seq)


