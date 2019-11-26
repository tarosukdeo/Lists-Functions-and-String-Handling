AAtable = {
    "ATT": "I", "ATC": "I", "ATA": "I",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "TTA": "L", "TTG": "L",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TTT": "F", "TTC": "F",
    "ATG": "M"
    }

def translate(sequence):
    protein = ""
    for i in range(0, len(sequence), 3):        #Loop through the sequence in steps of 3
        codon = sequence[i:i+3]                 #Obtain each codon from the sequence
        if len(codon)%3 == 0:
            if codon in AAtable.keys():
                protein += AAtable[codon]
            else:
                protein += "X"                #Add an X to our amino acid sequence if the codon represents an amino acid not listed in our table
        else:
            protein += "_"                    #The underscore represents an incomplete codon in the sequence (Fewer than 3 bases)
    return protein  

def mutate(dna):
    replaceA = dna.replace("a", "A")            #find first occurence of 'a' and replace with 'A'
    normDNA = open("normalDNA.txt", "w")
    normDNA.write(replaceA)                     #Write new sequence to normalDNA.txt"
    normDNA.close()

    replaceT = dna.replace("a", "T")            #find first occurence of 'a' and replace with 'T'
    mutDNA = open("mutatedDNA.txt", "w")
    mutDNA.write(replaceT)                      #Write new sequence to mutatedDNA.txt
    mutDNA.close()

def txtTranslate(user_inputfile):               #Function that takes in text file as input and calls our translate function for the contents of the file
    with open(user_inputfile) as infile:
        for line in infile:
            dna = translate(line)
            print(dna)   
    
with open("DNA.txt") as inputfile:
    dnaSequence = ""                                  #Populate a string with the contents of DNA.txt
    
    print("Amino acid sequence from DNA.txt:\n")
    for line in inputfile:
        dnaSequence += line
        dna = translate(line)
        print(dna)

    print("\n")
    mutate(dnaSequence)                                 #Call to mutate function for contents of DNA.txt
    

print("Amino acid sequence from normalDNA.txt:\n")
txtTranslate("normalDNA.txt")                           #Call to txtTranslate for normalDNA.txt
print("\n")

print("Amino acid sequence from mutatedDNA.txt:\n")
txtTranslate("mutatedDNA.txt")                          #Call to txtTranslate for mutatedDNA.txt



    
    
        
        
    


    
    
    



