from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in formatted string"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """Calculate and display a future date based on days added"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current datetime
    print("=== Date Time Explorer ===")
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("\nEnter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Error: Please enter a valid integer number.")

if __name__ == "__main__":
    main()