#include <iostream>
#include <exception>
using namespace std;


string reversed_string(string string_var);

int main() {
	string example = "hello world";
	string expected_output = "dlrow olleh";
	string output_string;
	string exception;

	output_string = reversed_string(example);

	cout << "Output: " << output_string << endl;

	if (output_string != expected_output) {
		cout << "The output (" << output_string << ") is not the same as the expected_output (" << expected_output << ")" << endl; 
		return 1;
	} 

	cout << "success!" << endl;

	return 0;
} 

string reversed_string(string string_var) {
	int string_length = string_var.length();
	string reversed_string = "";

	if (string_length == 0) {
		throw length_error("Error. Length of string must be greater than 0");
	} else if (string_length == 1){
		return string_var;
	} else {
		for (int i = string_length - 1; i >= 0; i--) {
			reversed_string += string_var[i];
		}

		return reversed_string;
	};

}