#include <iostream>
using namespace std;

int main() {

	int a = 3;
	float b = 4.5; // float can store about 7 decimals
	double c = 5.25; // double can store about 15 decimals

	double sum = (double)a + (double)b + c;

	cout << "The sum of a, b, and c is", sum << std::endl;

	return 0;
}