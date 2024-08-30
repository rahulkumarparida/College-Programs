#include<stdio.h>
int main()
{
int arr[100],n,i,j,temp;
printf("Enter the number of element you want to take as an input:\n");
scanf("%d",&n);
printf("Enter %d numbers\n",n);
for(i=0;i<n;i++)
{
printf("Element %d =",i+1);
scanf("%d",&arr[i]);
}
printf("Before sorting the array elements are:\n ");
for(i=0;i<n;i++)
{
printf("%d",arr[i]);
}
for(i=0;i,n;i++)
{
int flag=0;
for(j=0;j<n-1;j++)
{
if(arr[j]>arr[j+1])
{
temp=arr[j];
arr[j]=arr[j+1];
arr[j+1]=temp;
flag=1;
}
}
if(flag==0)
break;
}
printf("\n After sorting the elements are:\n");
for(i=0;i<n;i++)
{
printf("%d",arr[i]);
}
return 0;
}
