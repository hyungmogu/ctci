#include <stdio.h>

void print_big(int number) {
	if(number > 10) {
		printf("%d is huge \n", number);
	}

}

// void can_func_have_default_parameteric_val(int test = 0) {
// 	printf("This is a printing function %d", test);
// }

void func_cannot_affect_variables_outside_function_normally(int number){
	number = 1;
}

int main(){
	int array[] = { 1, 11, 2, 22, 3, 33 };
	int number = 20;
	int i;
	for (i = 0; i < 6; i++) {
		print_big(array[i]);
	}
	// can_func_have_default_parameteric_val();
	func_cannot_affect_variables_outside_function_normally(number);
	printf("The original value of number is: %d \n", number);
	printf("See? The value cannot be changed without pointers: %d \n", number);
	return 0;
}