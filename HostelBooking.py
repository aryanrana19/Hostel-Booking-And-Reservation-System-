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
            # Display user information
            print("\nUser Information:")
            print(f"Name: {user_name}")
            print(f"Age: {user_age}")
            print(f"Contact Number: {contact_number}")
            print(f"Hostel Enrolled in: {self.name}")
        else:
            print("No rooms available.")


class BoysHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)


class GirlsHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)


class HostelBookingSystem:
    def __init__(self):
        self.hostels = []

    def create_boys_hostel(self):
        name = input("Enter boys hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        laundry_available = input("Is laundry available? (yes/no): ").lower() == "yes"
        wifi_available = input("Is WiFi available? (yes/no): ").lower() == "yes"
        hostel = BoysHostel(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)
        self.hostels.append(hostel)

    def create_girls_hostel(self):
        name = input("Enter girls hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        laundry_available = input("Is laundry available? (yes/no): ").lower() == "yes"
        wifi_available = input("Is WiFi available? (yes/no): ").lower() == "yes"
        hostel = GirlsHostel(name, total_rooms, available_rooms, timings, mess_available, laundry_available, wifi_available)
        self.hostels.append(hostel)

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
            print("6. Exit")
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
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    system = HostelBookingSystem()
    system.main_menu()

