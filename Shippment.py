class Shipment:
    def __init__(self, id, origin, destination, weight, status, payment_method):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = status  # (e.g., "Pending", "In Transit", "Delivered")
        self.payment_method = payment_method  # (e.g., "Cash", "Card", "Bank Transfer")

# Function to add a new shipment
def int(param):
    pass


def input(param):
    pass


def float(param):
    pass


def add_shipment(shipments):
    id = int(input("Enter shipment ID: "))
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    weight = float(input("Enter weight (kg): "))
    status = input("Enter initial status (Pending, In Transit, Delivered): ")
    payment_method = input("Enter payment method (Cash, Card, Bank Transfer): ")
    shipments.append(Shipment(id, origin, destination, weight, status, payment_method))

# Function to display all shipments
def print(param):
    pass


def display_shipments(shipments):
    print("-" * 70)
    print("ID\tOrigin\t\tDestination\tWeight(kg)\tStatus\t\tPayment Method")
    print("-" * 70)
    for shipment in shipments:
        print(f"{shipment.id}\t{shipment.origin:<20}\t{shipment.destination:<20}\t{shipment.weight:.2f}\t{shipment.status}\t{shipment.payment_method}")
    print("-" * 70)

# Function to update shipment status
def update_status(shipments):
    id = int(input("Enter shipment ID to update: "))
    found = False
    for shipment in shipments:
        if shipment.id == id:
            new_status = input("Enter new status: ")
            shipment.status = new_status
            found = True
            break
    if not found:
        print("Shipment not found.")

# Function to search shipments by origin or destination
def search_shipments(shipments):
    search_term = input("Enter origin or destination to search: ").lower()
    for shipment in shipments:
        if search_term in shipment.origin.lower() or search_term in shipment.destination.lower():
            print(f"ID: {shipment.id}")
            print(f"  Origin: {shipment.origin}")
            print(f"  Destination: {shipment.destination}")
            print(f"  Weight: {shipment.weight:.2f} kg")
            print(f"  Status: {shipment.status}")
            print(f"  Payment Method: {shipment.payment_method}")
            print("-" * 20)

# Main program loop
shipments = []
while True:
    print("\nShipping Management System")
    print("1. Add Shipment")
    print("2. Display Shipments")
    print("3. Update Shipment Status")
    print("4. Search Shipments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_shipment(shipments)
    elif choice == "2":
        display_shipments(shipments)
    elif choice == "3":
        update_status(shipments)
    elif choice == "4":
        search_shipments(shipments)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")