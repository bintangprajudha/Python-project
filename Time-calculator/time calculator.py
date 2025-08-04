def add_time(start, duration, day=None):
    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Convert to 24-hour format for easier calculation
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Add duration to start time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour
    
    # Handle minute overflow
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60
    
    # Calculate days passed
    days_later = total_hours // 24
    final_hour = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        period = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        period = 'PM'
    else:
        display_hour = final_hour - 12
        period = 'PM'
    
    # Format the time
    new_time = f"{display_hour}:{total_minutes:02d} {period}"
    
    # Handle day of week if provided
    if day:
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = days_of_week.index(day.lower())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize()
        new_time += f", {new_day}"
    
    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time


# Test cases to demonstrate functionality
if __name__ == "__main__":
    print("Time Calculator Test Cases:")
    print("=" * 40)
    
    # Test cases with expected outputs
    print(f"add_time('3:00 PM', '3:10') = {add_time('3:00 PM', '3:10')}")
    print(f"add_time('11:30 AM', '2:32', 'Monday') = {add_time('11:30 AM', '2:32', 'Monday')}")
    print(f"add_time('11:43 AM', '00:20') = {add_time('11:43 AM', '00:20')}")
    print(f"add_time('10:10 PM', '3:30') = {add_time('10:10 PM', '3:30')}")
    print(f"add_time('11:43 PM', '24:20', 'tueSday') = {add_time('11:43 PM', '24:20', 'tueSday')}")
    print(f"add_time('6:30 PM', '205:12') = {add_time('6:30 PM', '205:12')}")
