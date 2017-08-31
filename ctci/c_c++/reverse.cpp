#include <iostream>
#include <exception>
using namespace std;


void reversed_string(string *string_var);

int main() {
	string example1 = "hello world/0";
	string expected_output = "dlrow olleh/0";
	string example2 = "a";

	reversed_string(&example1);
	reversed_string(&example2);

	if (example2 != "a") {
		cout << "The output (" << example2 << ") is not the same as the expected_output (" << expected_output << ")" << endl; 
		return 1;
	}

	if (example1 != expected_output) {
		cout << "The output (" << example1 << ") is not the same as the expected_output (" << expected_output << ")" << endl; 
		return 1;
	} 

	cout << "success!" << endl;

	return 0;
} 

void reversed_string(string *string_var) {
	// -1 is done to exclude '/0' symbol
	int string_length = (*string_var).length() - 2;
	char temp;

	if (string_length == 0) {
		throw length_error("Error. Length of string must be greater than 0");
	} else if (string_length == 1){
		return;
	} else {
		for (int i = string_length - 1; i >= string_length/2; i--) {
			temp = (*string_var)[i];
			(*string_var)[i] = (*string_var)[string_length - (i+1)];
			(*string_var)[string_length - (i+1)] = temp;
		}
	};

}