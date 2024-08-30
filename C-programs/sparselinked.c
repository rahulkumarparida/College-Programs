#include<stdio.h>
#include<stdlib.h>

struct node {
    int value;
    int row;
    int column;
    struct node* next;
};

void create_new_node(struct node** start, int non_zero, int row_index, int column_index) {
    struct node* temp, * r;
    temp = *start;

    if (temp == NULL) {
        temp = (struct node*)malloc(sizeof(struct node));
        temp->value = non_zero;
        temp->row = row_index;
        temp->column = column_index;
        temp->next = NULL;
        *start = temp;
    } else {
        while (temp->next != NULL)
            temp = temp->next;
        
        r = (struct node*)malloc(sizeof(struct node));
        r->value = non_zero;
        r->row = row_index;
        r->column = column_index;
        r->next = NULL;
        temp->next = r;
    }
}

void printlist(struct node* start) {
    struct node* temp = start;

    while (temp != NULL) {
        printf("row: %d, column: %d, value: %d\n", temp->row, temp->column, temp->value);
        temp = temp->next;
    }
}

int main() {
    int sparse[4][5] = {
        {0, 0, 3, 0, 4},
        {0, 0, 5, 7, 0},
        {0, 0, 0, 0, 0},
        {0, 2, 6, 0, 0}
    };

    struct node* start = NULL;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
            if (sparse[i][j] != 0) {
                create_new_node(&start, sparse[i][j], i, j);
            }
        }
    }

    printf("Linked List representation of the sparse matrix:\n");
    printlist(start);

    return 0;
}

