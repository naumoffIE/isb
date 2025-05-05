import math
from scipy.special import gammaincc

def frequency_test(bit_sequence: str) -> float:
    """
    NIST Frequency Test.

    Evaluates whether the number of ones and zeros in the input sequence are approximately equal.

    Parameters:
        bit_sequence (str): A binary string consisting of '0's and '1's.

    Returns:
        float: p-value of the test.
    """
    cumulative_sum = sum(1 if bit == '1' else -1 for bit in bit_sequence)
    test_statistic = abs(cumulative_sum) / math.sqrt(len(bit_sequence))
    p_value = math.erfc(test_statistic / math.sqrt(2))
    return p_value


def runs_test(bit_sequence: str) -> float:
    """
    NIST Runs Test.

    Checks whether the transitions between 0 and 1 occur as expected for a random sequence.

    Parameters:
        bit_sequence (str): A binary string consisting of '0's and '1's.

    Returns:
        float: p-value of the test.
    """
    proportion_ones = bit_sequence.count('1') / len(bit_sequence)

    if abs(proportion_ones - 0.5) >= 2 / math.sqrt(len(bit_sequence)):
        return 0.0

    num_runs = sum(1 for i in range(len(bit_sequence) - 1) if bit_sequence[i] != bit_sequence[i + 1]) + 1

    expected_runs = 2 * len(bit_sequence) * proportion_ones * (1 - proportion_ones)
    std_dev = 2 * math.sqrt(2 * len(bit_sequence)) * proportion_ones * (1 - proportion_ones)

    p_value = math.erfc(abs(num_runs - expected_runs) / std_dev)
    return p_value


def longest_run_test(bit_sequence: str, block_size: int = 8) -> float:
    """
    NIST Longest Run of Ones in a Block Test.

    Evaluates whether the longest run of ones in blocks is consistent with expected values.

    Parameters:
        bit_sequence (str): A binary string consisting of '0's and '1's.
        block_size (int): Length of each block. Default is 8.

    Returns:
        float: p-value of the test.

    Raises:
        ValueError: If the length of the sequence is not a multiple of block_size.
    """
    sequence_length = len(bit_sequence)

    if sequence_length % block_size != 0:
        raise ValueError(
            f"Sequence length ({sequence_length}) must be a multiple of block size ({block_size})"
        )

    num_blocks = sequence_length // block_size

    expected_probabilities = [0.2148, 0.3672, 0.2305, 0.1875]
    observed_frequencies = [0, 0, 0, 0]  # For run lengths: <=1, =2, =3, >=4

    for i in range(num_blocks):
        block = bit_sequence[i * block_size:(i + 1) * block_size]
        max_run = 0
        current_run = 0

        for bit in block:
            if bit == '1':
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0

        if max_run <= 1:
            observed_frequencies[0] += 1
        elif max_run == 2:
            observed_frequencies[1] += 1
        elif max_run == 3:
            observed_frequencies[2] += 1
        else:  # max_run >= 4
            observed_frequencies[3] += 1

    chi_squared = sum(
        (observed_frequencies[i] - num_blocks * expected_probabilities[i]) ** 2 /
        (num_blocks * expected_probabilities[i])
        for i in range(4)
    )

    p_value = gammaincc(1.5, chi_squared / 2)
    return p_value
