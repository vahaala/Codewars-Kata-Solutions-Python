dna = "TACGATTTAAAGAACTT"

def DNA_strand(dna):
    new_dna = "".join(["T" if i == "A" else "C" if i == "G" else "A" if i == "T" else "G" if i == "C" else i for i in dna]) #creates a new list, which is a copy of the input, but the iterator changes the amines to their corresponding pair. It then joins the list into a string.
    return new_dna #returns new dna string

print(DNA_strand(dna))