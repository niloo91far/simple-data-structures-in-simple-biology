# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:51:15 2023

@author: Niloofar
"""

with open(r"C:\Users\Niloofar\Desktop\Code\Set\AD.txt",'r') as AD:
    ADGenes=AD.readlines()
    print(len(ADGenes))
    
with open(r"C:\Users\Niloofar\Desktop\Code\Set\Depression.txt",'r') as Dep:
    DepGenes=Dep.readlines()
    print(len(DepGenes))

with open(r"C:\Users\Niloofar\Desktop\Code\Set\Gastritis.txt",'r') as Gast:
    GastGenes=Gast.readlines()
    print(len(GastGenes))

with open(r"C:\Users\Niloofar\Desktop\Code\Set\HyperT.txt",'r') as Hypt:
    HyptGenes=Hypt.readlines()
    print(len(HyptGenes))
    
common=50
for i in range(common):
    ADGenesSet=set(ADGenes[:50])
    DepGenesSet=set(DepGenes[:50])
    GastGenesSet=set(GastGenes[:50])
    HyptGenesSet=set(HyptGenes[:50])
    
common_genes=ADGenesSet.intersection(DepGenesSet,GastGenesSet,HyptGenesSet)
print("These four diseases have",len(common_genes), "common genes in their top 50 most affecting genes list, these are: ")
print(common_genes)

for g in common_genes:
    with open(r"C:\Users\Niloofar\Desktop\Code\Set\commonGenes.txt",'a') as commonG:
        commonG.write(g)
        

        
        
        
        
        
        
        
        
