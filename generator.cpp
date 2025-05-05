#include <iostream>
#include <random> // for std::mt19937

int main()
{

	std::random_device rd;
	std::mt19937 mt{}; // Instantiate a 32-bit Mersenne Twister

	std::uniform_int_distribution<int> dist(0, 1);

	std::string bit_sequence;

	bit_sequence.reserve(128);

	for (int i = 0; i < 128; i++)
	{
		bit_sequence += dist(rd) ? '1' : '0';
	}

	std::cout << "Generated bit sequence:\n" << bit_sequence << std::endl;

	return 0;
}