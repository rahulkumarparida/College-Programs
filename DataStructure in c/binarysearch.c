#include <stdio.h>

int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
int main() {
    //int arr[10] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    //int n = sizeof(arr) / sizeof(arr[0]);
    //int x;
    int arr[100],num,target,i;
    printf("Enter the total numbers you want to take as an input.\n");
    scanf("%d",&num);
    printf("Enter %d numbers\n",num);
    for(i=0;i<num;i++)
     {
      printf("Element %d=",i+1);
      scanf("%d",&arr[i]);
     }
    printf("Enter the number you want to be searched \n");
    scanf("%d",&target);
    //printf("search number among these:2,4,6,8,10,12,14,16,18,20");
    //printf("enter the number:");
    //scanf("%d",x);
    //int target = x;
    int result = binarySearch(arr, 0, num - 1, target);
    if (result == -1)
        printf("Element %d is not present in the array\n", target);
    else
        printf("Element %d is present at position %d\n", target, result+1);

    return 0;
}

