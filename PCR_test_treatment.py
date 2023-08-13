print("Please Enter the records as:\nName,Family Name,Age,PCR result (+ or -),Covid16 Symptoms (yes, no),Prior Disease (yes, no)\nPress 'End' to end")
info_list = []
entry = input() 
while entry != 'End':
    entry = entry.split(",")
    info_list.append(entry)
    if len(entry) != 6:
        print ("Please enter information correctly")
        info_list.pop()
    entry = input()
for record in info_list:
    if record[3] == "-":
        print ("For Patient",record[0]+" "+record[1],"no treatment is needed.") 
    if record[3] == "+":
        if int(record[2]) < 60:
            if (record[4] == "no" and record[5] == "no"):
                print("For Patient",record[0]+" "+record[1],"Please follow Health Treatment number 1")
            if (record[4] == "yes" and record[5] == "yes"):
                print("For Patient",record[0]+" "+record[1],"Please follow Health Treatment number 2")
        if int(record[2]) >= 60:
            if (record[4] == "yes" or record[5] == "yes"):
                print("For Patient",record[0]+" "+record[1],"Please follow Health Treatment number 3")
    
