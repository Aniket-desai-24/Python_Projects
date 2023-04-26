# ConstructionRental class to manage rental vehicles
class ConstructionRental:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)

    def list_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.inventory if not vehicle.rented]
        if available_vehicles:
            print("Available vehicles:")
            for vehicle in available_vehicles:
                print(vehicle)
        else:
            print("No vehicles are currently available for rent.")

    def rent_vehicle(self, vehicle_id):
        for vehicle in self.inventory:
            if vehicle.id == vehicle_id:
                if not vehicle.rented:
                    vehicle.rented = True
                    print(f"{vehicle} has been rented.")
                else:
                    print(f"{vehicle} is already rented.")
                return
        print(f"No vehicle with ID {vehicle_id} found.")

    def return_vehicle(self, vehicle_id):
        for vehicle in self.inventory:
            if vehicle.id == vehicle_id:
                if vehicle.rented:
                    vehicle.rented = False
                    print(f"{vehicle} has been returned.")
                else:
                    print(f"{vehicle} has not been rented.")
                return
        print(f"No vehicle with ID {vehicle_id} found.")


# Vehicle class to represent rental vehicles
class Vehicle:
    def __init__(self, id, name, description, hourly_rate, rented=False):
        self.id = id
        self.name = name
        self.description = description
        self.hourly_rate = hourly_rate
        self.rented = rented

    def __str__(self):
        return f"{self.name} ({self.description}), hourly rate: {self.hourly_rate}"

# Function to create a new vehicle object
def create_vehicle():
    id = input("Enter vehicle ID: ")
    name = input("Enter vehicle name: ")
    description = input("Enter vehicle description: ")
    hourly_rate = float(input("Enter hourly rate: "))
    return Vehicle(id, name, description, hourly_rate)

# Function to rent a vehicle
def rent_vehicle(rental_company):
    vehicle_id = input("Enter the ID of the vehicle to rent: ")
    rental_company.rent_vehicle(vehicle_id)

# Function to return a rented vehicle
def return_vehicle(rental_company):
    vehicle_id = input("Enter the ID of the vehicle to return: ")
    rental_company.return_vehicle(vehicle_id)

# Main function to run the program
def main():
    rental_company = ConstructionRental("ABC Construction Rental")
    while True:
        print("\n1. Add a new vehicle to inventory")
        print("2. List available vehicles")
        print("3. Rent a vehicle")
        print("4. Return a rented vehicle")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            vehicle = create_vehicle()
            rental_company.add_vehicle(vehicle)
            print(f"{vehicle} has been added to inventory.")
        elif choice == "2":
            rental_company.list_available_vehicles()
        elif choice == "3":
            rent_vehicle(rental_company)
        elif choice == "4":
            return_vehicle(rental_company)
        elif choice == "5":
            print("Thank you for using ABC Construction Rental!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-5.")

if __name__ == "__main__":
    main()
