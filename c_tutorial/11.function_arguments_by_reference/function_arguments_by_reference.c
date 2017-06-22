#include <stdio.h>

void addn(int n) {
	n++;
	printf("The value of n inside addn(n) is %d \n", n);
}

void addn_2(int * m) {
	(*m)++;
	printf("The value of m inside addn_2 is %d \n", *m);
}

typedef struct {
	int x;
	int y;
} Point;

void move(Point * p) {
	(*p).x++;
	(*p).y++;
}

typedef struct {
  char * name;
  int age;
} person;

/* function declaration */
void birthday(person * p) {
	(*p).age++;
}

int main() {
	int n = 1;
	int m = 1;
	addn_2(&m);
	addn(n);

	Point p;
	p.x = 1;
	p.y = 1;
	move(&p);

	printf("The value of p.x is %d \n", p.x);
	printf("The value of p.y is %d \n", p.y);
	printf("The value of n is %d \n", n);
	printf("The value of m is %d \n", m);

	person john;
	john.name = "John";
	john.age = 27;

	printf("%s is %d years old.\n", john.name, john.age);
	birthday(&john);
	printf("Happy birthday! %s is now %d years old.\n", john.name, john.age);

	return 0;
}