# Global storage for vehicle records and traffic booths
vehicle_records = []
traffic_booths = []
import datetime

def welcome_screen():
    """Display the main menu."""
    while True:
        print("\n" + "*" * 50)
        print("WELCOME TO")
        print("TRAFFIC MANAGEMENT SYSTEM")
        print("*" * 50)
        print("1. Record New Vehicles")
        print("2. Get Record of Fine")
        print("3. Search Record of Vehicles")
        print("4. Search Traffic Control Booths")
        print("5. Control the Traffic")
        print("6. HELP")
        print("0. Exit")
        choice = input("Please enter your desired choice: ")

        if choice == '1':
            record_new_vehicles()
        elif choice == '2':
            record_fine()
        elif choice == '3':
            search_vehicles()
        elif choice == '4':
            search_traffic_booths()
        elif choice == '5':
            control_traffic()
        elif choice == '6':
            help_menu()
        elif choice == '0':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def record_new_vehicles():
    """Manage vehicle records."""
    while True:
        print("\n" + "-" * 50)
        print("----Record of Vehicles----")
        print("1. Add a New Vehicle")
        print("2. Search for a Vehicle Using Registration Number")
        print("3. Search by Owner's Name")
        print("4. Search by phone number")
        print("0. Return to Main Menu")
        choice = input("Please enter your desired choice: ")

        if choice == '1':
            add_new_vehicle()
        elif choice == '2':
            search_vehicle_by_reg_number()
        elif choice == '3':
            search_vehicle_by_owner_name()
        elif choice =='4':
            search_vehicle_by_phone_number()
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

def add_new_vehicle():
    """Add a new vehicle to the record."""
    reg_number = input("Enter vehicle registration number: ")
    owner_name = input("Enter owner's name: ")
    owner_phone = input("Enter owner's phone number: ")  
    vehicle_records.append({"reg_number": reg_number, "owner_name": owner_name, "owner_phone": owner_phone})
    print("Data saved successfully!")

def search_vehicle_by_reg_number():
    """Search vehicle by registration number."""
    reg_number = input("Enter vehicle registration number: ")
    for record in vehicle_records:
        if record["reg_number"] == reg_number:
            print(f"Record Found:\nRegistration Number: {record['reg_number']}\nOwner's Name: {record['owner_name']}\nPhone Number:{record['owner_phone']}")
            return
    print("Record not found for the given registration number!")

def search_vehicle_by_owner_name():
    """Search vehicle by owner's name."""
    owner_name = input("Enter owner's name: ")
    for record in vehicle_records:
        if record["owner_name"].lower() == owner_name.lower():
            print(f"Record Found:\nRegistration Number: {record['reg_number']}\nOwner's Name: {record['owner_name']}")
            return
    print("Record not found for the given owner's name!")
    
def search_vehicle_by_phone_number():
    """Search vehicle by owner's phone number."""
    owner_phone = input("Enter owner's phone number: ")
    for record in vehicle_records:
        if record["owner_phone"] == owner_phone:
            print(f"Record Found:\nRegistration Number: {record['reg_number']}\nOwner's Name: {record['owner_name']}\nPhone Number: {record['owner_phone']}")
            return
    print("Record not found for the given phone number!")

def record_fine():
    """Placeholder for fine management."""
    print("\n Fine management is under development.")
def search_vehicles():
    """Provide options to search vehicles based on different criteria."""
    print("\n" + "-" * 50)
    print("----Search Vehicles----")
    print("1. Search by Registration Number")
    print("2. Search by Owner's Name")
    print("3. Search by Owner's Phone Number")
    print("0. Return to Main Menu")
    choice = input("Please enter your choice: ")

    if choice == '1':
        search_vehicle_by_reg_number()
    elif choice == '2':
        search_vehicle_by_owner_name()
    elif choice == '3':
        search_vehicle_by_phone_number()
    elif choice == '0':
        return
    else:
        print("Invalid choice! Please try again.")

def search_traffic_booths():
    """Search traffic control booths."""
    print("\n" + "-" * 50)
    print("----Search Traffic Control Booths----")
    print("1. Search by Booth ID")
    print("2. Search by Location")
    print("0. Return to Main Menu")
    choice = input("Please enter your choice: ")

    if choice == '1':
        search_booth_by_id()
    elif choice == '2':
        search_booth_by_location()
    elif choice == '0':
        return
    else:
        print("Invalid choice! Please try again.")

def search_booth_by_id():
    """Search traffic booth by ID."""
    booth_id = input("Enter Traffic Control Booth ID: ")
    for booth in traffic_booths:
        if booth["booth_id"] == booth_id:
            print(f"Booth Found:\nBooth ID: {booth['booth_id']}\nLocation: {booth['location']}\nContact Info: {booth['contact_info']}")
            return
    print("No traffic booth found with the given ID.")

def search_booth_by_location():
    """Search traffic booth by location."""
    location = input("Enter booth location: ")
    for booth in traffic_booths:
        if location.lower() in booth["location"].lower():
            print(f"Booth Found:\nBooth ID: {booth['booth_id']}\nLocation: {booth['location']}\nContact Info: {booth['contact_info']}")
            return
    print("No traffic booth found at the given location.")

def add_new_booth():
    """Add a new traffic control booth."""
    booth_id = input("Enter Traffic Control Booth ID: ")
    location = input("Enter booth location: ")
    contact_info = input("Enter contact information for the booth: ")
    traffic_booths.append({"booth_id": booth_id, "location": location, "contact_info": contact_info})
    print("Traffic Control Booth added successfully!")

def control_traffic():
    """Manage traffic signals and report traffic conditions."""
    while True:
        print("\n" + "-" * 50)
        print("----Traffic Control----")
        print("1. Report Traffic Condition")
        print("2. Manage Traffic Signals")
        print("0. Return to Main Menu")
        choice = input("Please enter your choice: ")

        if choice == '1':
            report_traffic_condition()
        elif choice == '2':
            manage_traffic_signals()
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

def report_traffic_condition():
    """Report the current traffic condition."""
    location = input("Enter the location of the traffic condition: ")
    condition = input("Enter the traffic condition (e.g., Heavy, Moderate, Light): ")
    print(f"Traffic condition reported at {location}: {condition}")

def manage_traffic_signals():
    """Manage traffic signals."""
    while True:
        print("\n" + "-" * 50)
        print("----Manage Traffic Signals----")
        print("1. Set Signal to Green")
        print("2. Set Signal to Yellow")
        print("3. Set Signal to Red")
        print("0. Return to Traffic Control Menu")
        choice = input("Please enter your choice: ")

        if choice == '1':
            print("Traffic signal set to Green.")
        elif choice == '2':
            print("Traffic signal set to Yellow.")
        elif choice == '3':
            print("Traffic signal set to Red.")
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

def help_menu():
    """Display the help menu."""
    while True:
        print("\n" + "-" * 50)
        print("----HELP INFORMATION----")
        print("1. Understand Vehicle Recording")
        print("2. Understand Fine Recording")
        print("3. Understand Traffic Control Booths")
        print("0. Return to Main Menu")
        choice = input("Please enter your choice: ")

        if choice == '1':
            print("\nVehicle Recording Help:\nYou can add, search, or manage vehicle records easily through the system.")
        elif choice == '2':
            print("\nChallan Recording Help:\nThis feature allows you to manage traffic fines.")
        elif choice == '3':
            print("\nTraffic Control Booths Help:\nSearch for details about traffic control booths in your area or add new ones.")
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point of the program
if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
    welcome_screen()
