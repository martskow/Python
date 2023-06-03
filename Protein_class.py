"""
Autor: Marta Skowron
"""


class Protein:

    def __init__(self, ID, sequence, name=None, organism=None):
        """
        Create a protein's feature.

        Args:
            ID (str): protein identifier
            sequence (str): protein sequence
            name (str): name for the protein. If None (default),
                        the protein name will not be included.
            organism (str): organism name of the protein. If None (default),
                        the organism name will not be included.

        Raises ValueError: 
            if the sequence length is less than or equal to zero,
            if the sequence's elements are not included in protein alphabet.
        Raises TypeError:
            if sequence, ID, name or organism type isn't string.
        """
        self.aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                           'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        if not type(sequence) is str:
            raise TypeError('Sequence entered incorrectly')
        elif sequence == '':
            raise ValueError("Sequence can't be empty")
        elif not all(element in self.aminoacids for element in sequence):
            raise ValueError('The sequence can only contain characters for ' + \
                             'amino acids from protein alphabet')
        else:
            self.sequence = sequence

        if type(ID) is str and not ID == '':
            self.ID = str(ID)
        elif ID == '':
            raise ValueError("Protein id can't be empty")
        else:
            raise TypeError('Protein ID must be string')

        if name is None or type(name) is str:
            self.name = name
        else:
            raise TypeError('Protein name must be string')

        if organism is None or type(organism) is str:
            self.organism = organism
        else:
            raise TypeError('Protein organism name must be string')

    def __str__(self):
        """
        Function the lenght of the sequence.

        Returns:
            lenght (int): lenght of the sequence
        """
        if self.name is None and self.organism is None:
            record = '>sp|' + self.ID + '|' + '\n' + self.sequence
        elif self.name is not None and self.organism is None:
            record = '>sp|' + self.ID + '|' + self.name + '\n' + self.sequence
        elif self.name is None and self.organism is not None:
            record = '>sp|' + self.ID + '|' + ' OS=' + self.organism + '\n' + \
                     self.sequence
        else:
            record = '>sp|' + self.ID + '|' + self.name + ' OS=' + \
                     self.organism + '\n' + self.sequence

        return record

    def lenght(self):
        """
        Calculate the lenght of the sequence.

        Returns:
            lenght (int): lenght of the sequence
        """
        lenght = len(self.sequence)

        return lenght

    def cut(self, start, end):
        """
        Cut out fragment of the sequence and returns new protein object.
        
        Args:
            start (int): the index of first amino acid where the cut starts
            end (int): the index of amino acid where the cut end
        Returns:
            cut_protein (object): object defined by function protein
        
        Raises ValueError: 
                    if the start value is greater than end value,
                    if the start value isn't greater than 1 or
                    if the end value is greater than lenght of primary sequence.
        Raises TypeError:
                    if start or end type isn't int 
        """
        if not (type(start) is int and type(end) is int):
            raise TypeError
        elif 0 < start <= end <= len(self.sequence):
            cut_sequence = self.sequence[start - 1: end]
            cut_ID = self.ID + '/' + str(start) + '-' + str(end)
            cut_protein = Protein(cut_ID, cut_sequence, self.name, self.organism)
        else:
            raise ValueError

        return cut_protein

    def modify(self, index, aminoacid):
        """
        Modify fragment of the sequence and returns new Protein object
        (or old one if there's no change).
        
        Args:
            index (int): the index of the amino acid that user want to replace
            aminoacid (str): the letter equivalent of the amino acid name
        Returns:
            modify_protein (object): object defined by class Protein;
                    the name and organism data will be lost after modyfing
                    the protein
        
        Raises ValueError: 
                    if the start value is greater than end value,
                    if the start value isn't greater than 1 or
                    if the end value is greater than lenght of primary sequence.
        Raises TypeError:
                    if start or end type isn't int 
        """
        if (type(index) is int and index in range(1, len(self.sequence) + 1)
                and type(aminoacid) is str and aminoacid in self.aminoacids):
            if aminoacid == self.sequence[index - 1]:
                modify_protein = self
            else:
                modify_sequence = self.sequence[0: index - 1] + aminoacid + \
                                  self.sequence[index: len(self.sequence)]
                modify_ID = self.ID + ' ' + str(self.sequence[index - 1]) + \
                            str(index) + str(aminoacid)
                modify_protein = Protein(modify_ID, modify_sequence)
        elif not (type(index) is int and type(aminoacid) is str):
            raise TypeError
        elif index not in range(1, len(self.sequence) + 1):
            raise IndexError
        elif aminoacid not in self.aminoacids:
            raise ValueError

        return modify_protein

print(Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY').cut(2, 8).modify(4,'D'))