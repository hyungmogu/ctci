#include <stdio.h>

int main(){

	char helloWorld[] = "hello world";
	char * name = "Hyungmo Gu";

	char testArray[][5] = {
		{'a','e','i','o','u'},
		{'A','E','I','O','U'},
		{'A'}
	};

	testArray[2][1] = 'e';

	printf("The value of testArray[0][5] is: %c \n", testArray[0][4]);
	printf("The value of testArray[1][5] is: %c \n", testArray[1][4]);
	printf("The value of testArray[2][1] is: %c \n", testArray[2][1]);
	printf("%s \n", helloWorld);
	printf("%s \n", name);
	return 0;
}