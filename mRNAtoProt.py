#Exercise No2.: This program translates mRNA to Protein

mRNA = 'augacugaauauaaacuugugguaguuggagcugguggcguaggcaagagugccuugacgauacagcuaauucagaaucauuuuguggacgaauaugauccaacaauagaggauuccuacaggaagcaaguaguaauugauggagaaaccugucucuuggauauucucgacacagcaggucaagaggaguacagugcaaugagggaccaguacaugaggacuggggagggcuuucuuuguguauuugccauaaauaauacuaaaucauuugaagauauucaccauuauagagaacaaauuaaaagaguuaaggacucugaagauguaccuaugguccuaguaggaaauaaaugugauuugccuucuagaacaguagacacaaaacaggcucaggacuuagcaagaaguuauggaauuccuuuuauugaaacaucagcaaagacaagacagagaguggaggaugcuuuuuauacauuggugagagagauccgacaauacagauugaaaaaaaucagcaaagaagaaaagacuccuggcugugugaaaauuaaaaaaugcauuauaauguaa'

print(len(mRNA))

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

prot=[]
for i in range(0, len(mRNA)-4,3):
    if mRNA[i:i+3] in stop:
        break
    for j in range(len(allcode3)):
        if mRNA[i:i+3] in allcode3[j]:
            prot.append(aacode[j])


protein = "".join(prot)
print(protein)
print(len(protein))





