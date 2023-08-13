# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:33:31 2023

@author: Niloofar
"""

with open(r"C:\Users\Niloofar\Desktop\Code\Set\approved_drugs\EU-drugs.txt",'r') as EU:
    EU_drugs=EU.readlines()
    print("EMA approved",len(EU_drugs), "drugs since 1999")
    
with open(r"C:\Users\Niloofar\Desktop\Code\Set\approved_drugs\USA-drugs.txt",'r') as USA:
    USA_drugs=USA.readlines()
    print("FDA approved",len(USA_drugs), "drugs since 1999")

with open(r"C:\Users\Niloofar\Desktop\Code\Set\approved_drugs\Japan-drugs.txt",'r') as Japan:
    Japan_drugs=Japan.readlines()
    print("PMDA approved",len(Japan_drugs), "drugs since 1999")

    
EU_drugsSet=set(EU_drugs)
USA_drugsSet=set(USA_drugs)
Japan_drugsSet=set(Japan_drugs)

common=EU_drugsSet.intersection(USA_drugsSet,Japan_drugsSet)
print("All the three organizations approved to",len(common), "drugs listed below:" )
print(common)

FDA=USA_drugsSet.difference(EU_drugsSet).difference(Japan_drugsSet)
#FDA=USA_drugsSet.difference(EU_drugsSet,Japan_drugsSet)
print("Here is the list of",len(FDA),"drugs approved only by FDA, and not the other two:" )
print(FDA)


EMA=EU_drugsSet.difference(USA_drugsSet).difference(Japan_drugsSet)
print("Here is the list of",len(EMA),"drugs approved only by EMA, and not the other two:" )
print(EMA)


PMDA=USA_drugsSet.difference(EU_drugsSet).difference(USA_drugsSet)
print("Here is the list of",len(PMDA),"drugs approved only by PMDA, and not the other two:" )
print(PMDA)
