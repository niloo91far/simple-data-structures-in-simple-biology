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


#yeast DNA codon frequency
RNA_dict={'F':{'uuu':0.59,'uuc':0.41},
          'L':{'uua':0.28,'uug':0.29,'cuu':0.13,'cuc':0.06,'cua':0.14,'cug':0.11},
           'I':{'auu':0.46,'auc':0.26,'aua':0.27},
           'M':{'aug':1.00},
           'V':{'guu':0.39,'guc':0.21,'gua':0.21,'gug':0.19},
           'S':{'ucu':0.26,'ucc':0.16,'uca':0.21,'ucg':0.10,'agu':0.16,'agc':0.11},
           'P':{'ccu':0.31,'ccc':0.15,'cca':0.41,'ccg':0.12},
           'T':{'acu':0.35,'acc':0.22,'aca':0.30,'acg':0.13},
           'A':{'gcu':0.38,'gcc':0.22,'gca':0.29,'gcg':0.11},
           'Y':{'uau':0.56,'uac':0.44},
           'H':{'cau':0.64,'cac':0.36},
           'Q':{'caa':0.69,'cag':0.31},
           'N':{'aau':0.59,'aac':0.41},
           'K':{'aaa':0.58,'aag':0.42},
           'D':{'gau':0.65,'gac':0.35},
           'E':{'gaa':0.71,'gag':0.29},
           'C':{'ugu':0.63,'ugc':0.37},
           'W':{'ugg':1.00},
           'R':{'cgu':0.15,'cgc':0.06,'cga':0.07,'cgg':0.04,'aga':0.48,'agg':0.21},
           'G':{'ggu':0.47,'ggc':0.19,'gga':0.22,'ggg':0.12}
    }

#print("HERE",type(RNA_dict.get('F')))

#stopF = [0.48,0.24,0.29]

mrna_seq=[]
dna_seq=[]

#Reverse transcription with optimization via DICTIONARY
for p in prot:
    if p in RNA_dict.keys():
        mrna_seq.append(max(RNA_dict.get(p)))
    if p in stop:
        break;

mrna_seq = ''.join(mrna_seq)
dna_seq=mrna_seq

for i in range(len(mrna_seq)):
    if mrna_seq[i]=='u':
        dna_seq= dna_seq.replace(dna_seq[i],'t')


print("Probably DNA sequence of YEAST based on the given protein sequence: ")
print(dna_seq)


