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

    def create_hostel(self):
        hostel_type = input("Enter 'boys' or 'girls' to specify the hostel type: ").lower()
        while hostel_type not in ['boys', 'girls']:
            hostel_type = input("Invalid input. Please enter 'boys' or 'girls': ").lower()

        name = input(f"Enter {hostel_type} hostel name: ")
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
            'type': hostel_type
        }

        self.hostels_collection.insert_one(hostel_data)
        print(f"{hostel_type.capitalize()} hostel created and stored in the database.")

    def display_hostel_info(self):
        hostel_type = input("Enter 'boys' or 'girls' to display hostel information: ").lower()
        while hostel_type not in ['boys', 'girls']:
            hostel_type = input("Invalid input. Please enter 'boys' or 'girls': ").lower()

        results = self.hostels_collection.find({"type": hostel_type})
        results_list = list(results)
        temp1 = []
        temp2 = []

        for i in results_list:
            if i['name'] not in temp1:
                temp1.append(i['name'].lower())
                temp2.append(i)

        results_list = temp2

        if len(results_list) == 0:
            print(f"No {hostel_type} hostel information available.")
        else:
            for result in results_list:
                border = "=" * 40
                print(border)
                print(f"Hostel Name: {result['name']}")
                print(f"Total Rooms: {result['total_rooms']}")
                print(f"Available Rooms: {result['available_rooms']}")
                print(f"Timings: {result['timings']}")
                print(f"Mess Availability: {'Yes' if result['mess_available'] else 'No'}")
                print(f"Laundry Availability: {'Yes' if result['laundry_available'] else 'No'}")
                print(f"WiFi Availability: {'Yes' if result['wifi_available'] else 'No'}")
                print(border)



    def book_room(self):
        hostel_name = input("Enter the name to book the hostel: ")
        hostel = self.hostels_collection.find_one({"name": hostel_name})

        new_available_rooms = hostel['available_rooms'] - 1
        update_query = {
            "$set": {
                "available_rooms": int(new_available_rooms)
            }
        }

        self.hostels_collection.update_one({"name": hostel_name}, update_query)
        print(f"A room in '{hostel_name}' has been booked successfully.")


    def remove_hostel(self):
        hostel_name = input("Enter the name of the hostel to remove: ")
        result = self.hostels_collection.delete_one({"name": hostel_name})

        if result.deleted_count > 0:
            print(f"Hostel '{hostel_name}' has been removed from the database.")
        else:
            print(f"No hostel found with the name '{hostel_name}'.")   


    def update_hostel_info(self):
        hostel_name = input("Enter the name of the hostel to update: ")
        hostel = self.hostels_collection.find_one({"name": hostel_name})

        if hostel:
            print("Enter the updated values")
            new_total_rooms = input(f"Total Rooms: ") 
            new_available_rooms = input(f"Available Rooms: ")
            new_timings = input(f"Timings: ")
            new_mess_available = input(f"Mess Available?: ").lower() in ['yes', 'y']
            new_laundry_available = input(f"Laundry Available?: ").lower() in ['yes', 'y']
            new_wifi_available = input(f"WiFi Available?: ").lower() in ['yes', 'y']

            update_query = {
                "$set": {
                    "total_rooms": int(new_total_rooms),
                    "available_rooms": int(new_available_rooms),
                    "timings": new_timings,
                    "mess_available": new_mess_available,
                    "laundry_available": new_laundry_available,
                    "wifi_available": new_wifi_available
                }
            }

            self.hostels_collection.update_one({"name": hostel_name}, update_query)
            print(f"Hostel '{hostel_name}' has been updated successfully.")
        else:
            print(f"No hostel found with the name '{hostel_name}'.")

    def count_hostels_by_type(self):
        pipeline = [
            {"$group": {"_id": "$type", "count": {"$sum": 1}}}
        ]
        results = list(self.hostels_collection.aggregate(pipeline))
        for result in results:
            print(f"Number of {result['_id']} hostels: {result['count']}")


    def search_hostels_by_filter(self):
        filter = {}

        mess_available = input("Search for hostels with mess available? (yes/no): ").lower()
        if mess_available == "yes":
            filter["mess_available"] = True
        elif mess_available == "no":
            filter["mess_available"] = False

        laundry_available = input("Search for hostels with laundry available? (yes/no): ").lower()
        if laundry_available == "yes":
            filter["laundry_available"] = True
        elif laundry_available == "no":
            filter["laundry_available"] = False

        wifi_available = input("Search for hostels with WiFi available? (yes/no): ").lower()
        if wifi_available == "yes":
            filter["wifi_available"] = True
        elif wifi_available == "no":
            filter["wifi_available"] = False

        results = list(self.hostels_collection.find(filter))

        if not results:
            print("No hostels found matching the specified filter.")
        else:
            print("Hostels matching the specified filter:")
            for result in results:
                border = "=" * 40
                print(border)
                print(f"Hostel Name: {result['name']}")
                print(f"Total Rooms: {result['total_rooms']}")
                print(f"Available Rooms: {result['available_rooms']}")
                print(f"Timings: {result['timings']}")
                print(f"Mess Availability: {'Yes' if result['mess_available'] else 'No'}")
                print(f"Laundry Availability: {'Yes' if result['laundry_available'] else 'No'}")
                print(f"WiFi Availability: {'Yes' if result['wifi_available'] else 'No'}")
                print(border)

    def group_hostels_by_amenities(self):
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "mess_available": "$mess_available",
                        "laundry_available": "$laundry_available",
                        "wifi_available": "$wifi_available"
                    },
                    "hostels": {
                        "$push": {
                            "name": "$name",
                            "total_rooms": "$total_rooms",
                            "available_rooms": "$available_rooms",
                            "timings": "$timings"
                        }
                    },
                    "count": {"$sum": 1}
                }
            }
        ]
        results = list(self.hostels_collection.aggregate(pipeline))
        if not results:
            print("No hostels found in the database.")
        else:
            for result in results:
                mess_available = result["_id"]["mess_available"]
                laundry_available = result["_id"]["laundry_available"]
                wifi_available = result["_id"]["wifi_available"]
                hostels = result["hostels"]
                count = result["count"]
                print(f"Hostels with Mess: {mess_available}, Laundry: {laundry_available}, WiFi: {wifi_available}")
                print(f"Count: {count}")
                for hostel in hostels:
                    print(f"  - Name: {hostel['name']}, Total Rooms: {hostel['total_rooms']}, Available Rooms: {hostel['available_rooms']}, Timings: {hostel['timings']}")
                print()

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create Hostel")
            print("2. Display Hostel Information")
            print("3. Book Room")
            print("4. Remove a hostel")
            print("5. Update Hostel Information")
            print("6. Count Total of Hostels")
            print("7. Filter Hostels by filter")
            print("8. Group Hostels By ")
            print("0. Exit")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == 1:
                    self.create_hostel()
                elif choice == 2:
                    self.display_hostel_info()
                elif choice == 3:
                    self.book_room()
                elif choice == 4:
                    self.remove_hostel()
                elif choice == 5:
                    self.update_hostel_info()
                elif choice == 6:
                    self.count_hostels_by_type()
                elif choice == 7:
                    self.search_hostels_by_filter()
                elif choice == 8:
                    self.group_hostels_by_amenities()
                elif choice == 0:
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# FETCHING MONGODB DATA

if __name__ == "__main__":
    system = HostelBookingSystem()
    system.main_menu()