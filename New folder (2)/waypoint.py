class Waypoint:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.next = None
        self.prev = None

class Route:
    def __init__(self):
        self.head = None

    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)
        if self.head is None:
            self.head = new_waypoint
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint
            new_waypoint.prev = current

    def insert_waypoint_after(self, target, location, description):
        new_waypoint = Waypoint(location, description)
        current = self.head
        while current:
            if current.location == target:
                new_waypoint.next = current.next
                current.next = new_waypoint
                if new_waypoint.next:
                    new_waypoint.next.prev = new_waypoint
                new_waypoint.prev = current
                break
            current = current.next

    def remove_waypoint(self, location):
        current = self.head
        if current and current.location == location:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        while current:
            if current.location == location:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                break
            current = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(f"Your current Location is: {current.location}, Description: {current.description}")
            current = current.next

class BidirectionalRoute(Route):
    def traverse_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(f"Your current Location is: {current.location}, Description: {current.description}")
            current = current.prev

if __name__ == '__main__':
    route = BidirectionalRoute()
    
    while True:
        print("\nMenu:")
        print("1. Add Waypoint")
        print("2. Insert Waypoint after")
        print("3. Remove Waypoint")
        print("4. Forward Traversal")
        print("5. Backward Traversal")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            location = input("Enter location: ")
            description = input("Enter description: ")
            route.add_waypoint(location, description)
        elif choice == "2":
            target = input("Enter the location after which to insert: ")
            location = input("Enter new location: ")
            description = input("Enter new description: ")
            route.insert_waypoint_after(target, location, description)
        elif choice == "3":
            location = input("Enter the location to remove: ")
            route.remove_waypoint(location)
        elif choice == "4":
            print("\nForward Traversal:")
            route.traverse_forward()
        elif choice == "5":
            print("\nBackward Traversal:")
            route.traverse_backward()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
