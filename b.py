from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta")

A = record.seq.count("A")
T = record.seq.count("T")
C = record.seq.count("C")
G = record.seq.count("G")

print(f"A: {A}")
print(f"T: {T}")
print(f"C: {C}")
print(f"G: {G}")
