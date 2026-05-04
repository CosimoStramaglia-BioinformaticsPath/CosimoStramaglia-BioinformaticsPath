def dna_to_rna(dna_sequence: str) -> str:
    """
    (First version)
    Transcribe a DNA sequence into its RNA equivalent.

    Args:
        dna_sequence (str): A sequence of nucleotides.

    Returns:
        str: The RNA sequence.
    """
    # Inizialise the vocabulary as DNA base (key): RNA base (value) so that it knows how to do substitutions
    rna_vocabulary = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}

    return "".join([rna_vocabulary[n] for n in dna_sequence.upper()])

def dna_to_rna_2(dna_sequence: str) -> str:
    """
    (Second version)
    Transcribe a DNA sequence into its RNA equivalent.

    Args:
        dna_sequence (str): A sequence of nucleotides.

    Returns:
        str: The RNA sequence.
    """
    rna = ""
    # Inizialise the vocabulary as DNA base (key): RNA base (value) so that it knows how to do substitutions
    rna_vocabulary = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}

    for n in dna_sequence.upper():
        rna += rna_vocabulary[n]

    return rna


def dna_to_rna_3(dna_sequence: str) -> str:
    """
    (Third version)
    Transcribe a DNA sequence into its RNA equivalent.

    Args:
        dna_sequence (str): A sequence of nucleotides.

    Returns:
        str: The RNA sequence.
    """
    return dna_sequence.replace('T', 'U')

dna_to_rna(input())

dna_to_rna_2(input())

dna_to_rna_3(input())