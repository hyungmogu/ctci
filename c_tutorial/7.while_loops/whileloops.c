#include <stdio.h>

int main(){

	int i = 0;
	int j = 0;

	// This returns even number of elements
	while(i < 10) {
		i++;
		if (i % 2 == 1) {
			continue;
		}

		printf("The value of i is: %d \n", i);
	}

	// This stps the loop from looping at i == 1
	while(j < 10) {
		j++;
		if (j % 2 == 1) {
			printf("The value of i before break is: %d \n", j);
			break;
		}

		printf("I am moving onto %dth iteration! \n", j);

	}

	// Exercise

	// if the current number is less than 5, don't print it
	// If the current number is greater than 10, don't print it and stop the loop

    int array[] = {1, 7, 4, 5, 9, 3, 5, 11, 6, 3, 4};
    int k = 0;

    while (k < 10) {
    	k++;
        /* your code goes here */
        if (array[k] < 5) {
        	continue;
        }

        if (array[k] > 10) {
        	break;
        }

        printf("%d\n", array[k]);
    }

	return 0;
}