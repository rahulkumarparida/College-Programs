#WAP to develop queue to perform the insert delete display operation in a list
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
        print(f"Inserted {element} into the queue.")
    def dequeue(self):
        if len(self.queue) > 0:
            removed_element = self.queue.pop(0)
            print(f"Deleted {removed_element} from the queue.")
        else:
            print("Queue is empty, cannot dequeue.")
    def display(self):
        if len(self.queue) > 0:
            print("Current queue:", self.queue)
        else:
            print("Queue is empty.")
if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Insert (Enqueue)")
        print("2. Delete (Dequeue)")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            element = input("Enter the element to insert: ")
            q.enqueue(element)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
