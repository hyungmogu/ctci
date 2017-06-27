#include <stdio.h>
#include <stdlib.h>


// remember that {} bracket is used when the values inside the array is known
// remember that initializing an array without values take form of 'int array_name[10]'
// remember that for multi-dimensional array of known size, column size must be specified.

int main() {
	char vowels[] = {'A','E','I','O','U'};
	char *pvowels = &vowels;
	int i;

	float calculation = (float)1/3;

	printf("The value of calcuation is: %f \n", calculation);

	// print the address
	// &vowels[i] gives memory location of the ith value in the array
	// each element occupies one byte
	// Memory location of values for pvowels and vowles are the same
	for(i = 0; i < 5; i++){
		printf("&vowels[%d]: %u, pvowels + %d: %u, vowels + %d: %u \n", i, &vowels[i], i, pvowels + i, i, vowels + i);
	}

	// print the values of the array
	// *(pvowels + 10) is equivalent to vowels[10]
	for(i = 0; i < 5; i++) {
		printf("vowels[%d]: %c, *(pvowels + %d): %c, *(vowels + %d): %c \n", i, vowels[i], i, *(pvowels + i), i, *(vowels + i));
	}

	// 1 DIMENSIONAL DYNAMIC ALLOCATION FOR THE ARRAY
	// AN array with dynamically allocated memory is useful when size of array is not known
	int ncolmns = 5;

	char *pvowels2 = (char *)malloc(ncolmns * sizeof(char));


	// The name of an array is a pointer to its first element.
	pvowels2[0] = 'A';
	pvowels2[1] = 'E';
	pvowels2[2] = 'I';
	pvowels2[3] = 'O';
	pvowels2[4] = 'U';

	printf("the value of pvowels2[1] is: %c \n", pvowels2[1]);
	printf("the value of *(pvowels2 + 1) is: %c \n", *(pvowels2 + 1));

	// An array with dynamically allocated memory has an advantage of freeing a part or all memory at will
	// But only the beginning of that array can be freed.

	// 2 DIMENSIONAL DYNAMIC ALLOCATION FOR THE ARRAY

	int nrows = 2;

	char **multi_pvowels = (char **)malloc(nrows * sizeof(char *));

	multi_pvowels[0] = (char *)malloc(ncolmns * sizeof(char));
	multi_pvowels[1] = (char *)malloc(ncolmns * sizeof(char));

    multi_pvowels[0][0] = 'A';
    multi_pvowels[0][1] = 'E';
    multi_pvowels[0][2] = 'I';
    multi_pvowels[0][3] = 'O';
    multi_pvowels[0][4] = 'U';

    multi_pvowels[1][0] = 'a';
    multi_pvowels[1][1] = 'e';
    multi_pvowels[1][2] = 'i';
    multi_pvowels[1][3] = 'o';
    multi_pvowels[1][4] = 'u';

    int j;
    int k;


    for(j = 0; j < nrows; j++){
    	for(k = 0; k < ncolmns; k++) {
    		printf("%c ", multi_pvowels[j][k]);
    	}
    	printf("\n");
    }

	// Use free() on Heap memory only
	free(pvowels2);

	// a block pointer can be freed, but not pointers inside the block
	free(multi_pvowels[0]);
	free(multi_pvowels);


	int number_of_rows = 3;

    /* TODO: complete the following line to allocate memory for holding three rows */
    int **pnumbers = (int **) malloc(number_of_rows * sizeof(int *));

    /* TODO: allocate memory for storing the individual elements in a row */
    pnumbers[0] = (int *) malloc(1 * sizeof(int));
    pnumbers[1] = (int *) malloc(2 * sizeof(int));
    pnumbers[2] = (int *) malloc(3 * sizeof(int));

    pnumbers[0][0] = 1;
    pnumbers[1][0] = 1;
    pnumbers[1][1] = 1;
    pnumbers[2][0] = 1;
    pnumbers[2][1] = 2;
    pnumbers[2][2] = 1;

    for (i = 0; i < 3; i++) {
        for (j = 0; j <= i; j++) {
            printf("%d ", pnumbers[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < 3; i++) {
        /* TODO: free memory allocated for each row */
        free(pnumbers[i]);
    }

    /* TODO: free the top-level pointer */
    free(pnumbers);

  return 0;
}