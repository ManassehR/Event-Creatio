import datetime

class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

events = []

def add_event():
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    while not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD format.")
        date = input("Enter event date (YYYY-MM-DD): ")
    time = input("Enter event time (HH:MM): ")
    while not validate_time(time):
        print("Invalid time format. Please use HH:MM format.")
        time = input("Enter event time (HH:MM): ")

    event = Event(title, description, date, time)
    events.append(event)
    print("Event added successfully.")

def display_events():
    if not events:
        print("No events found.")
    else:
        print("=== Events ===")
        for event in events:
            print(f"Title: {event.title}")
            print(f"Description: {event.description}")
            print(f"Date: {event.date}")
            print(f"Time: {event.time}")
            print()

def delete_event():
    title = input("Enter the title of the event you want to delete: ")
    global events
    events = [event for event in events if event.title != title]
    print("Event deleted successfully.")

def main():
    while True:
        print("\n1. Add Event\n2. View Events\n3. Delete Event\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_event()
        elif choice == '2':
            display_events()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
