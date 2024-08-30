#include <stdio.h>
#include <stdlib.h>
#define SIZE 100
struct stack {
    int info;
};
struct stack s[SIZE];
int top = -1;

void push(int);
void pop();
void disp();
int main() {
    int ch, item;
    printf("First Choose an Option:-\n");
    while (1) {
        printf("\n1-push- (To INSERT an element)\n<=============================>");
        printf("\n2-pop:- (To DELETE the last inserted element)\n<=============================>");
        printf("\n3-display:- (To DISPLAY the element)\n<=============================>");
        printf("\n4-exit:- (To EXIT the operation )\n<=============================>");
        printf("\nEnter your choice: ");
        scanf("%d", &ch);
        printf("\n^__________^\n");
        switch (ch) {
            case 1:
                printf("\nEnter a number: ");
                scanf("%d", &item);
                push(item);
                break;
            case 2:
                pop();
                break;
            case 3:
                disp();
                break;
            case 4:
                exit(0);
            default:
                printf("Sorry, no such operation.(Make Your Choices with the given option)\n");
                break;
        }
    }
    return 0; 
}
void push(int x) {
    if (top >= SIZE - 1) {
        printf("Stack is full and can cause overflow (The limit has reached)\n");
    } else {
        top++;
        s[top].info = x;
    }
}
void pop() {
    if (top == -1) {
        printf("Stack is empty and can cause underflow (add some new elements to continue the operation)\n");
    } else {
        printf("The deleted item is %d\n", s[top].info);
        top--;
    }
}
void disp() {
    if (top == -1) {
        printf("The Stack is empty (Please enter some elements)\n");
    } else {
        for (int i = top; i >= 0; i--) {
            printf("%d \n", s[i].info);
        }  
   } 
} 
