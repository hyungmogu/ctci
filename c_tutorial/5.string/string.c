#include <stdio.h>
#include <string.h>


int main(){

	// pointer is used for read only
	char * name1 = "Hyungmo Gu";

	// Character array allows string to be manipulated
	// [] automatically calculates the number of elements required to contain the string in the array
	char name2[] = "Hyungmo Gu";
	int age = 26;

	// String formatting with printf
	// \n is used at the end so this statememnt is printed on a new line
	printf("My name is %s and I am %d years old \n", name1, age);

	// String length
	// The length of a string is determined using strlen()
	// int lengthOfMyName = strlen(name);
	printf("The length of my name is %d \n", strlen(name1));

	// String comparison
	// The two string can be compared using strncmp() function
	// it returns 0 if two strings match. Otherwise, a non-zero number is returned.

	if(strncmp(name1,name2,10) == 0) {
		printf("Ofcourse my names should match. \n");
	} else {
		printf("What happened to my name? \n");
	}

	// String concatenation
	// Two strings can be joined using the function strncat()
	// It appends first n characters of src string to the destination where n is min(n, length(src))
	char dest[20] = "Hello";
	char src[20] = "World";

	printf("Resulting string when concatenated at n=3: %s \n", strncat(dest,src,3));
	printf("Resulting string when concatenated at n=20: %s \n", strncat(dest,src,20));
	printf("Resulting string when concatenated at n=6: %s \n", strncat(dest,src,6));

	// Exercise
	// Define the string first_name with the value John using the pointer notatio, and
	// define the string last_name with the value Doe using the local array expression

	/* define first_name */
	char * first_name = "John";
	char last_name[20] = "Doe";
	/* define last_name */
	char name[100];

	last_name[0] = 'B';

	// sprintf goes to a buffer you've allocated. In this case, it's name
	sprintf(name, "%s %s", first_name, last_name);
	if (strncmp(name, "John Boe", 100) == 0) {
	  printf("Done!\n");
	}
	name[0]='\0';
	strncat(name,first_name,4);
	strncat(name,last_name,20);
	printf("%s\n",name);
	return 0;
}