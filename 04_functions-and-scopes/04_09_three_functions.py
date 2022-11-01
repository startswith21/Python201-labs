# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
DNAseq = ["GATCAC", "CCCAGG", "ATGCGG"]

def patients1(DNA):
    stopcodon = DNA + ["TCAAAG"]
    return stopcodon

complDNAseq = patients1(DNAseq)

Proteinseq = ["AS", "GS", "TL", "KG"]
def patients2(Protein):
    ProtDNAseq = Proteinseq + complDNAseq
    return ProtDNAseq

ProtDNA = patients2(Proteinseq)
print(ProtDNA)

def Seqanalysis(nsMut):
    Results = []
    for item in ProtDNA:
        if item == "GATCAG":
            Results += "p"
        else:
            Results += "n"
    return Results

Outcome = Seqanalysis(ProtDNA)
print(Outcome)





            
