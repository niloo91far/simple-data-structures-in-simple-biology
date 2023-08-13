#Exercise No3.: This Program is for the reverse transcription: Prot > mRNA > DNA 

#prot = input("please insert the sequence of protein: ")


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

mrna_seq=[]
dna_seq=[]

#Reverse translation
for p in prot:
    for index,aa in enumerate(aacode):
        if p==aa:
            mrna_seq.append(allcode3[index][0])


mrna_seq = ''.join(mrna_seq)

dna_seq=mrna_seq
#Reverse transcription
for i in range(len(mrna_seq)):
    if mrna_seq[i]=='u':
        dna_seq= dna_seq.replace(dna_seq[i],'t')

        
print("The protein: ")
print(prot)
print("is reverse transcripted to the below DNA sequence: ")
print(dna_seq)


