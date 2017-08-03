#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	char letter;
	struct Node * next;
	struct Node * prev;
} node_l;

int isPalindrome(node_l * front, node_l * back);
void isAtTheMiddleEven(node_l * top, node_l * prev);
void isAtTheMiddleOdd(node_l * top, node_l * prev);
void addNode(node_l * front, node_l * back);

int main() {

	int n, i, x;
	node_l * front = NULL;
	node_l * back = NULL;

	// get number of elements to add
	printf("enter number of elements to add");
	scanf("%d", &n);

	for(i = 0; i < n; i++){
		printf("enter element %d", i);
		scanf("%d", &x);
		printf("\n");
		addNode(&front, &back, x);
	}

	// if(isPalindrome(front, back)) {
	// 	printf("Yes. The link list is palindrome. \n"); 
	// } else {
	// 	printf("No. The link list is not palindrome. \n");
	// }

	return 0;
}

void showList(node_l * front) {
	node_l * current = front;

	while(current != NULL) {
		printf("%s ", current->letter);
		current = current->next;
	}
	printf("\n");
}

int isEmpty(node_l * front, node_l * back){
	if (front == NULL && back == NULL) {
		return 1;
	}
	return 0;
} 

void addNode(node_l ** front, node_l ** back, int letter) {
	temp = malloc(sizeof(node_l));
	temp->letter = letter;

	if(isEmpty()) {
		temp->next = NULL;
		temp->prev = NULL;
		*front = temp;
		*back = temp;
		return;
	}

	*back->next = temp;
	temp->prev = *back;
	*back = temp;

}

// int isPalindrome(node_l * front, node_l * back) {

// }