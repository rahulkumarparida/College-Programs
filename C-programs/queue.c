#include<stdio.h>
#include<stdlib.h>
int queue[50],front=-1,rear=-1;
void enqueue();
void dequeue();
void display();
int main()
 {
   int ch;
   printf("1. ENQUEUE \n");
   printf("2. DEQUEUE \n");
   printf("3. DISPLAY \n");
   printf("4. EXIT \n");

   while(1)
    {
      printf("\n Enter the Choice : ");
      scanf("%d",&ch);
      switch(ch)
       {
	 case 1: enqueue();
		 break;
	 case 2: dequeue();
		 break;
	 case 3: display();
		 break;
	 case 4: exit(0);
		 break;
	 default: printf(" Invalid Option");
       }
    }
   return 0;
 }
void enqueue()
 {
  int item;
  if(rear==50-1)
   printf("\n Queue is Full ");
  else
    {
      if(front==-1)
	front=0;
      printf(" Insert Element in Queue: ");
      scanf("%d",&item);
      rear=rear+1;
      queue[rear]=item;
    }
 }
void dequeue()
 {
  if(front==-1)
   printf("\n Queue is empty ");
  else
    {
     printf("\n Deleted : %d",queue[front]);
     front++;
    }
 }
void display()
 {
   int i;
   if(rear==-1)
    printf("\n Queue is Empty ");
   else
    {
     printf("\n Queue Elements are : \n");
     for(i=front;i<=rear;i++)
      printf(" %d ",queue[i]);
    }
   printf("\n");
 }
