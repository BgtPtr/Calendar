import calendar
import time

def calculate_time_difference(year, month):
    current_time = time.localtime()
    
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    
    year_difference = current_year - year
    month_difference = current_month - month
    
    if month_difference < 0:
        year_difference -= 1
        month_difference = 12 + month_difference
        
    return year_difference, month_difference

def display_complex_calendar():
    year = int(input("Kérlek add meg az évet: "))
    month = int(input("Kérlek add meg a hónapot (1-12): "))
    
    print("\nA kiválasztott hónap naptára:")
    print(calendar.month(year, month))
    
    year_difference, month_difference = calculate_time_difference(year, month)
    print(f"\nAz eltérés a bekért dátum és a jelenlegi idő között:")
    print(f"{year_difference} év és {month_difference} hónap")
    
    current_time = time.localtime()
    seconds = str(current_time.tm_sec).zfill(2)
    current_time_str = f"{current_time.tm_hour}:{current_time.tm_min}:{seconds}"
    print(f"\nA jelenlegi pontos idő másodpercre pontosan: {current_time_str}")

# Főprogram
display_complex_calendar()
