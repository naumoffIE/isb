from NIST_tests import *
import constants


def read_file(filepath: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Parameters:
    filepath (str): The path to the file to be read.

    Returns:
    str: The content of the file.
    """
    with open(filepath, "r") as file:
        return file.read()


def write_results(
    frequency_cpp: float,
    frequency_java: float,
    runs_cpp: float,
    runs_java: float,
    longest_run_cpp: float,
    longest_run_java: float,
    output_path: str
) -> None:
    """
    Writes the test results to a file.

    Parameters:
    frequency_cpp (float): Frequency test result for C++ sequence.
    frequency_java (float): Frequency test result for Java sequence.
    runs_cpp (float): Runs test result for C++ sequence.
    runs_java (float): Runs test result for Java sequence.
    longest_run_cpp (float): Longest run test result for C++ sequence.
    longest_run_java (float): Longest run test result for Java sequence.
    output_path (str): Path to the file where results will be written.
    """
    with open(output_path, 'w') as file:
        file.write("Frequency Test:\n")
        file.write(f"C++: {frequency_cpp:.6f}\n")
        file.write(f"Java: {frequency_java:.6f}\n\n")

        file.write("Runs Test:\n")
        file.write(f"C++: {runs_cpp:.6f}\n")
        file.write(f"Java: {runs_java:.6f}\n\n")

        file.write("Longest Run Test:\n")
        file.write(f"C++: {longest_run_cpp:.6f}\n")
        file.write(f"Java: {longest_run_java:.6f}\n")


def main() -> None:
    """
    Main function.

    Runs NIST statistical tests on binary sequences from C++ and Java,
    and writes the results to an output file.
    """
    cpp_sequence = read_file(constants.bin_seq_cpp)
    java_sequence = read_file(constants.bin_seq_java)

    frequency_cpp = frequency_test(cpp_sequence)
    frequency_java = frequency_test(java_sequence)

    runs_cpp = runs_test(cpp_sequence)
    runs_java = runs_test(java_sequence)

    longest_run_cpp = longest_run_test(cpp_sequence)
    longest_run_java = longest_run_test(java_sequence)

    write_results(
        frequency_cpp, frequency_java,
        runs_cpp, runs_java,
        longest_run_cpp, longest_run_java,
        constants.result
    )


if __name__ == "__main__":
    main()
