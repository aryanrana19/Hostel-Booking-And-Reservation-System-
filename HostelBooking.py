from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['hostel_booking_system']
users_collection = db['users']

class Hostel:
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.timings = timings
        self.mess_available = mess_available
        self.laundry_available = laundry_available
        self.wifi_available = wifi_available

    def display_info(self):
        border = "=" * 40
        print(border)
        print(f"Hostel Name: {self.name}")
        print(f"Total Rooms: {self.total_rooms}")
        print(f"Available Rooms: {self.available_rooms}")
        print(f"Timings: {self.timings}")
        print(f"Mess Availability: {'Yes' if self.mess_available else 'No'}")
        print(f"Laundry Availability: {'Yes' if self.laundry_available else 'No'}")
        print(f"WiFi Availability: {'Yes' if self.wifi_available else 'No'}")
        print(border)

    def book_room(self):
        if self.available_rooms > 0:
            self.available_rooms -= 1
            print("Room booked successfully!")
            # Ask for user information
            user_name = input("Enter your name: ")
            user_age = input("Enter your age: ")
            contact_number = input("Enter your contact number: ")
            # Store user information in MongoDB
            user_data = {
                'name': user_name,
                'age': user_age,
                'contact_number': contact_number,
                'hostel': self.name
            }
            users_collection.insert_one(user_data)
            print("User information stored in the database.")
        else:
            print("No rooms available.")

            


class BoysHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)


class GirlsHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)


# MONGODB CONNECTIONS
class HostelBookingSystem:
    def __init__(self):
        self.hostels = []
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['hostel_booking_system']
        self.users_collection = self.db['users']
        self.hostels_collection = self.db['hostels']

    def create_boys_hostel(self):
        name = input("Enter boys hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        laundry_available = input("Is laundry available? (yes/no): ").lower() == "yes"
        wifi_available = input("Is WiFi available? (yes/no): ").lower() == "yes"
        hostel_data = {
            'name': name,
            'total_rooms': total_rooms,
            'available_rooms': available_rooms,
            'timings': timings,
            'mess_available': mess_available,
            'laundry_available': laundry_available,
            'wifi_available': wifi_available,
            'type': 'boys'
        }
        self.hostels_collection.insert_one(hostel_data)
        print("Boys hostel created and stored in the database.")

    def create_girls_hostel(self):
        name = input("Enter girls hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        laundry_available = input("Is laundry available? (yes/no): ").lower() == "yes"
        wifi_available = input("Is WiFi available? (yes/no): ").lower() == "yes"
        hostel_data = {
            'name': name,
            'total_rooms': total_rooms,
            'available_rooms': available_rooms,
            'timings': timings,
            'mess_available': mess_available,
            'laundry_available': laundry_available,
            'wifi_available': wifi_available,
            'type': 'girls'
        }
        self.hostels_collection.insert_one(hostel_data)
        print("Girls hostel created and stored in the database.")

    def display_boys_hostel_info(self):
        found = False
        for hostel in self.hostels:
            if isinstance(hostel, BoysHostel):
                hostel.display_info()
                found = True
        if not found:
            print("No boys hostel information available.")

    def display_girls_hostel_info(self):
        found = False
        for hostel in self.hostels:
            if isinstance(hostel, GirlsHostel):
                hostel.display_info()
                found = True
        if not found:
            print("No girls hostel information available.")

    def book_room(self):
        hostel_name = input("Enter hostel name: ")
        found = False
        for hostel in self.hostels:
            if hostel.name == hostel_name:
                hostel.book_room()
                found = True
                break
        if not found:
            print("Hostel not found.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create Boys Hostel")
            print("2. Create Girls Hostel")
            print("3. Display Boys Hostel Information")
            print("4. Display Girls Hostel Information")
            print("5. Book Room")
            print("6. Display Booked Users")
            print("7. Display Hostels")
            print("8. Exit")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == 1:
                    self.create_boys_hostel()
                elif choice == 2:
                    self.create_girls_hostel()
                elif choice == 3:
                    self.display_boys_hostel_info()
                elif choice == 4:
                    self.display_girls_hostel_info()
                elif choice == 5:
                    self.book_room()
                elif choice == 6:
                    self.display_booked_users()
                elif choice == 7:
                    self.display_hostels()
                elif choice == 8:
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# FETCHING MONGODB DATA

def display_boys_hostel_info(self):
    boys_hostels = self.hostels_collection.find({'type': 'boys'})
    if boys_hostels.count() == 0:
        print("No boys hostel information available.")
    else:
        print("Boys Hostel Information:")
        for hostel in boys_hostels:
            self.display_hostel_info(hostel)

def display_girls_hostel_info(self):
    girls_hostels = self.hostels_collection.find({'type': 'girls'})
    if girls_hostels.count() == 0:
        print("No girls hostel information available.")
    else:
        print("Girls Hostel Information:")
        for hostel in girls_hostels:
            self.display_hostel_info(hostel)

def display_hostel_info(self, hostel):
    border = "=" * 40
    print(border)
    print(f"Hostel Name: {hostel['name']}")
    print(f"Total Rooms: {hostel['total_rooms']}")
    print(f"Available Rooms: {hostel['available_rooms']}")
    print(f"Timings: {hostel['timings']}")
    print(f"Mess Availability: {'Yes' if hostel['mess_available'] else 'No'}")
    print(f"Laundry Availability: {'Yes' if hostel['laundry_available'] else 'No'}")
    print(f"WiFi Availability: {'Yes' if hostel['wifi_available'] else 'No'}")
    print(border)


def display_booked_users(self):
        booked_users = self.users_collection.find()
        if booked_users.count() == 0:
            print("No users have booked rooms yet.")
        else:
            print("Users who have booked rooms:")
            for user in booked_users:
                print(f"Name: {user['name']}, Age: {user['age']}, Contact: {user['contact_number']}, Hostel: {user['hostel']}")


if __name__ == "__main__":
    system = HostelBookingSystem()
    system.main_menu()

