#include <stdio.h>

struct point {
	int x;
	int y;
};
// declare to create an instance of the structure
typedef struct point Point;

// Here is another way to construct struct with typedef

typedef struct {
	int x;
	int y;
} aloha;

typedef struct {
	char * name;
	int age;
} person;

void draw_2(int x, int y) {
	// print what's inside
	printf("value of p.x = %d | value of p.y = %d \n", x, y);
}

void draw_1(Point p) {
	// print what's inside
	printf("value of p.x = %d | value of p.y = %d \n", p.x, p.y);
}

int main() {
	Point p;

	// store multiple values
	p.x = 5;
	p.y = 10;

	// without struct, all arguements have to be registered

	int sample_x = 1;
	int sample_y = 2;

	draw_2(sample_x, sample_y);

	// using struct, number of arguements entered gets reduced to 1
	draw_1(p);

	aloha a;
	a.x = 10;
	a.y = 12;

	printf("the value of a.x and a,y are: %d %d \n", a.x, a.y);

	// Exercise
	/* define the person struct here using the typedef syntax */

    person john;

    /* testing code */
    john.name = "John";
    john.age = 27;
    printf("%s is %d years old. \n", john.name, john.age);

    return 0;
}