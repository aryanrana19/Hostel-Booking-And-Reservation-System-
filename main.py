class Hostel:
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.timings = timings
        self.mess_available = mess_available

    def display_info(self):
        print("Hostel Name:", self.name)
        print("Total Rooms:", self.total_rooms)
        print("Available Rooms:", self.available_rooms)
        print("Timings:", self.timings)
        print("Mess Availability:", "Yes" if self.mess_available else "No")

    def book_room(self):
        if self.available_rooms > 0:
            self.available_rooms -= 1
            print("Room booked successfully!")
        else:
            print("No rooms available.")


class BoysHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available)


class GirlsHostel(Hostel):
    def __init__(self, name, total_rooms, available_rooms, timings, mess_available):
        super().__init__(name, total_rooms, available_rooms, timings, mess_available)


class HostelBookingSystem:
    def __init__(self):
        self.hostels = []

    def create_boys_hostel(self):
        name = input("Enter boys hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        hostel = BoysHostel(name, total_rooms, available_rooms, timings, mess_available)
        self.hostels.append(hostel)

    def create_girls_hostel(self):
        name = input("Enter girls hostel name: ")
        total_rooms = int(input("Enter total rooms: "))
        available_rooms = int(input("Enter available rooms: "))
        timings = input("Enter timings: ")
        mess_available = input("Is mess available? (yes/no): ").lower() == "yes"
        hostel = GirlsHostel(name, total_rooms, available_rooms, timings, mess_available)
        self.hostels.append(hostel)

    def display_hostel_info(self):
        for hostel in self.hostels:
            hostel.display_info()

    def book_room(self):
        hostel_name = input("Enter hostel name: ")
        for hostel in self.hostels:
            if hostel.name == hostel_name:
                hostel.book_room()
                return
        print("Hostel not found.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create Boys Hostel")
            print("2. Create Girls Hostel")
            print("3. Display Hostel Information")
            print("4. Book Room")
            print("5. Exit")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == 1:
                    self.create_boys_hostel()
                elif choice == 2:
                    self.create_girls_hostel()
                elif choice == 3:
                    self.display_hostel_info()
                elif choice == 4:
                    self.book_room()
                elif choice == 5:
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    system = HostelBookingSystem()
    system.main_menu()
