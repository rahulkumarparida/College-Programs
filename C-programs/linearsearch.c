#include <stdio.h>

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i; 
        }
    }
    return -1; 
}

int main() {
    int arr[10] = { 9, 8, 7, 6, 5, 4, 0, 0, 0, 0 }; // Initialize with 6 elements

    // Calculate the number of elements in arr
    int n = sizeof(arr) / sizeof(arr[0]); // Correct way to calculate number of elements

    int x = 8; // Element to search for
    int result = linearSearch(arr, n, x);
    
    if (result == -1) {
        printf("Element %d is not present in the array.\n", x);
    } else {
        printf("Element %d is present at index %d.\n", x, result);
    }
    
    return 0;
}

