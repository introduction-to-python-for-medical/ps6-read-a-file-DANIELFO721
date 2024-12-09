path = '/content/data/codons.txt'
file = open(path)
rows = file.readlines()
file.close()

def create_codon_dict(file_path):
    codonos_to_amino_acids = {}
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      amino_acid = cells[2]
      codonos_to_amino_acids[codon] = amino_acid
   
    return(codonos_to_amino_acids)


