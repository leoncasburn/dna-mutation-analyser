codon_table = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UAA": "STOP", "UAG": "STOP",
    "UGU": "C", "UGC": "C",
    "UGA": "STOP",
    "UGG": "W",

    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

# Translating RNA
def translate_rna(rna, codon_table):
    protein = ""

    for x in range(0, len(rna), 3):
        codon = rna[x:x+3]

        if len(codon) < 3:
            continue

        if codon in codon_table:
            amino_acid = codon_table[codon]

            if amino_acid == "STOP":
                break

            protein = protein + amino_acid
        else:
            protein = protein + "?"

    return protein


# Transcribing DNA to RNA
def transcribe_dna(dna):
    rna = ""

    for base in dna:
        if base == "T":
            rna = rna + "U"
        else:
            rna = rna + base

    return rna


# Getting user input
dna = input("Enter a DNA sequence: ").upper()

# Validation for DNA sequence
if len(dna) == 0:
    print("DNA sequence cannot be empty!")
    exit()

if any(base not in ["A", "T", "G", "C"] for base in dna):
    print("Invalid DNA sequence! Use only A, T, G, C.")
    exit()

# User enters mutation position
mutation_position = int(input("Enter mutation position (0-based index): "))

# User enters new base
new_base = input("Enter new base (A/T/G/C): ").upper()

# Validation for new base
if new_base not in ["A", "T", "G", "C"]:
    print("Invalid base!")
    exit()

# Validation for mutation position
if mutation_position < 0 or mutation_position >= len(dna):
    print("Invalid mutation position!")
    exit()

if dna[mutation_position] == new_base:
    print("Warning: the new base is the same as the original base.")

# Mutation
mutated_dna = dna[:mutation_position] + new_base + dna[mutation_position + 1:]

print("Original DNA:", dna)
print("Mutated DNA:", mutated_dna)

# Transcription
rna = transcribe_dna(dna)
mutated_rna = transcribe_dna(mutated_dna)

print("Original RNA sequence:", rna)
print("Mutated RNA sequence:", mutated_rna)

# Translation
protein = translate_rna(rna, codon_table)
mutated_protein = translate_rna(mutated_rna, codon_table)

print("Original protein:", protein)
print("Mutated protein:", mutated_protein)

# Find changed codon
codon_index = mutation_position // 3
codon_start = codon_index * 3

original_codon = rna[codon_start:codon_start + 3]
mutated_codon = mutated_rna[codon_start:codon_start + 3]

original_amino = codon_table.get(original_codon, "?")
mutated_amino = codon_table.get(mutated_codon, "?")

print("Changed codon index:", codon_index)
print("Original codon:", original_codon)
print("Mutated codon:", mutated_codon)
print("Original amino acid:", original_amino)
print("Mutated amino acid:", mutated_amino)

# Classify mutation
if mutated_protein == protein:
    print("Mutation type: Silent")
elif len(mutated_protein) < len(protein):
    print("Mutation type: Nonsense")
else:
    print("Mutation type: Missense")