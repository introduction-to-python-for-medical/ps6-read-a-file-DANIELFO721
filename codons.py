path = '/content/data/codons.txt'
file = open(path)
rows = file.readlines()
file.close()

def create_codon_dict(file_path):
    condon_to_amino_acid = {}
    for row in rows:
        cells = row.strip().split('\t')
        codon = cells[0]
        amino_acid = cells[2]
        condon_to_amino_acid[codon] = amino_acid
        
    return condon_to_amino_acid
  
create_codon_dict(file)
