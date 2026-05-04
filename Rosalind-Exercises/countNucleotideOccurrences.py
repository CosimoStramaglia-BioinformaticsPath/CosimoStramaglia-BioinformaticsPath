def count_nucleotide_occurrences(dna_sequence: str) -> dict:
    """
    Counts the occurrences of each nucleotide in a DNA sequence.

    Args:
        dna_sequence (str): A sequence of nucleotides.

    Returns:
        dict: A dictionary with occurrences for 'A', 'C', 'G', 'T' in that specific order.
    """
    # Initialize with 0 to ensure the presence of all bases and the order
    n_occurrences = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for n in dna_sequence.upper(): # .upper() to handle lowercase inputs
        if n in n_occurrences:
            n_occurrences[n] += 1

    return n_occurrences

count_nucleotide_occurrences(input())