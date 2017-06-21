#include <stdio.h>

int main(){
	// Pointer
	// The following pointer stores the value "John" in memory after compilation
	// Then, the pointer "name" stores the address that points to the memory location of the first letter of the value
	char * name = "John";

	// Deferencing
	int a_number = 1;
	int * pointer_to_a_number = &a_number;

	//changing the value of *pointer_to_a_number changes a_number

	*pointer_to_a_number = 2;
	printf("The value of a_number is: %d \n", a_number);



	// Exercise
	// create a pointer to the variable n, and increase the value by one

	int n = 10;

	/* your code goes here */
	int * pointer_to_n = &n;

	*pointer_to_n += 1;

	/* testing code */
	if (pointer_to_n != &n) return 1;
	if (*pointer_to_n != 11) return 1;

	printf("Done!\n");

	return 0;


}