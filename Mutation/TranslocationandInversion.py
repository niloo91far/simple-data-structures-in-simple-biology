#This program apply mutaions of types: Inversion and Translocation
#Note: Here the "translocation" is applied on the same gene, we can easily apply it on a different gene if we had one.
import random
mutnum=int(input("How many mutations you want to apply? "))
mtype = int(input("What should be the type of mutation? '1' for 'Inversion'. '2' for 'Translocation'"))

gene = 'atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa'

phe = ['ttt','ttc']
leu = ['tta','ttg','ctt','ctc','cta','ctg']
ile = ['att','atc','ata']
met = ['atg']
val = ['gtt','gtc','gta','gtg']
ser = ['tct','tcc','tca','tcg','agt','agc']
pro = ['cct','ccc','cca','ccg']
thr = ['act','acc','aca','acg']
ala = ['gct','gcc','gca','gcg']
tyr = ['tat','tac']
his = ['cat','cac']
gln = ['caa','cag']
asn = ['aat','aac']
lys = ['aaa','aag']
asp = ['gat','gac']
glu = ['gaa','gag']
cys = ['tgt','tgc']
trp = ['tgg']
arg = ['cgt','cgc','cga','cgg','aga','agg']
gly = ['ggt','ggc','gga','ggg']
stop = ['taa','tag','tga']

allcode3 = [phe,leu,ile,met,val,ser,pro,thr,ala,tyr,
            his,gln,asn,lys,asp,glu,cys,trp,arg,gly]

aacode = ['F','L','I','M','V','S','P','T','A','Y','H',
          'Q','N','K','D','E','C','W','R','G']
ncode=['a','t','g','c']

prot=[]
p=0

for i in range(0, len(gene)-4,3):
    if gene[i:i+3] in stop:
        break
    for j in range(len(allcode3)):
        if gene[i:i+3] in allcode3[j]:
            prot.append(aacode[j])

protein = "".join(prot)
genelist=list(gene)
print("Original Protein:\n",protein)

tmp=[]

for i in range(mutnum):
    mutpo=random.randint(0,len(genelist)-1)
    print("Mutation position is: ", mutpo)
    mutlen=random.randint(2,len(genelist)-mutpo)
    print("Mutation lenght is: ", mutlen)
    if mtype==1:
        for m in range(0,int(mutlen/2)):
            tmp=genelist[mutpo+m]
            genelist[mutpo+m]=genelist[mutpo+mutlen-m-1]
            genelist[mutpo+mutlen-m-1]=tmp
    elif mtype==2:
        mutpo_in=random.randint(0,len(genelist)-1)
        print("Insertion position is: ", mutpo_in)
        for m in range(0,mutlen):
            tmp.append(genelist.pop(mutpo-1))
        tmplist=''.join(tmp)
        genelist.insert(mutpo_in,tmplist)


geneMuted=''.join(genelist)
protMuted=[]
p=0

#To Protein
for i in range(0, len(geneMuted)-4,3):
    if geneMuted[i:i+3] in stop:
        break
    for j in range(len(allcode3)):
        if geneMuted[i:i+3] in allcode3[j]:
            protMuted.append(aacode[j])

protMuted = "".join(protMuted)
print("Muted Protein:\n",protMuted)

#Effect
if mtype==1:
    if len(protMuted)==len(protein):
        for i in range(len(protein)):
            if (i <= len(protMuted)) and (protein[i] != protMuted[i]):
                print (protein[i], "in position ", i, "is muted to ", protMuted[i], ": Missence")
    else:
        print ("Nonsence mutation")
elif mtype==2:
    if len(protMuted)<len(protein):
        print("Nonsence mutation")
else:
    if len(protMuted)<len(protein):
        print("Nonsence mutaiton")
    elif len(protMuted)==len(protein):
        print("Silent mutaiton")
    else:
        print("Frame shift")


