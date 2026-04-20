# DNA Mutation Analyzer

## Overview
This project simulates how a single-point mutation in a DNA sequence affects the resulting protein.

It models the central dogma of molecular biology:

DNA → RNA → Protein

The program allows a user to:
- Input a DNA sequence
- Introduce a mutation at a specific position
- Translate both original and mutated sequences into proteins
- Identify the affected codon and amino acid
- Classify the mutation as silent, missense, or nonsense


## Features

- DNA validation (accepts only A, T, G, C)
- Transcription (DNA → RNA)
- Translation (RNA → protein using codon table)
- Mutation simulation (single base substitution)
- Codon-level analysis
- Amino acid comparison
- Mutation classification:
  - Silent (no change in protein)
  - Missense (amino acid change)
  - Nonsense (premature stop codon)


## Example

Enter a DNA sequence: ATGGCC
Enter mutation position (0-based index): 3
Enter new base: A

Original DNA: ATGGCC
Mutated DNA: ATGACC

Original RNA: AUGGCC
Mutated RNA: AUGACC

Original protein: MA
Mutated protein: MT

Changed codon index: 1
Original codon: GCC
Mutated codon: ACC

Original amino acid: A
Mutated amino acid: T

Mutation type: Missense

## How It Works

1. DNA sequence is validated
2. DNA is transcribed into RNA
3. RNA is split into codons (groups of 3 bases)
4. Each codon is translated into an amino acid
5. A mutation is introduced into the DNA sequence
6. The mutated sequence is reprocessed
7. The program compares:
   - original vs mutated protein
   - codon and amino acid changes
8. The mutation is classified

## Technologies Used

- Python
- Dictionaries (codon table)
- Control flow and functions

## Limitations

- Uses a simplified mutation classification method
- Only supports single-point mutations
- Does not include full biological complexity (e.g. introns, reading frames, etc.)

## Future Improvements

- Allow for multiple mutations
- Add random mutation generation.
- Build simple user interface.

## Author

Created to learn how genetic mutations affect protein structure.