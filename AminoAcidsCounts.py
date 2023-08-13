#Exercise No.1: This Program counts and prints the index of each amino acid in a protein.

protein = 'MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM'
amino_acids = ['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G']
protein = list(protein)

print (len(amino_acids)) #should be 20 :)

aa_count=[]

for aa in range(len(amino_acids)):
    print("Amino acid", amino_acids[aa], "is repeated", protein.count(protein[aa]), "times in this protein at:")
    for p in range(len(protein)):
        if amino_acids[aa] == protein[p]:
            aa_count.append(p)
    print(aa_count)
    print ("-----------------")
    aa_count=[]
