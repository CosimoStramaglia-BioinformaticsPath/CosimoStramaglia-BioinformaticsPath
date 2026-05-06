def reverse_complement_DNA(dna_sequence: str) -> str:
    """
    Finds the reverse complement of a DNA sequence.

    Args:
        dna_sequence (str): A sequence of nucleotides.

    Returns:
        str: The reverse complement.
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    return "".join([complement[n] for n in dna_sequence.upper()])[::-1]

print(reverse_complement_DNA(input()))