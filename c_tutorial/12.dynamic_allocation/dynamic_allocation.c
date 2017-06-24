#include <stdio.h>
#include <stdlib.h>

typedef struct {
	char * name;
	int age;
} Person;

typedef struct {
  int x;
  int y;
} point;

int main() {

	Person * myperson = malloc(sizeof(Person));

	// storing value inside myperson
	myperson->name = "John";
	myperson->age = 27;

	// retrieving value
	printf("The name of the person is %s \n", myperson->name);
	printf("The age of the person is %d \n", myperson->age);


	point * mypoint = malloc(sizeof(point));

  /* Dynamically allocate a new point
     struct which mypoint points to here */

	mypoint->x = 10;
	mypoint->y =5 ;
	printf("mypoint coordinates: %d, %d\n", mypoint->x, mypoint->y);

	free(mypoint);
	free(myperson);
	return 0;
}