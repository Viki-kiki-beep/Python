def is_year_leap(year):
    return year % 4 == 0

year_to_check = 2025

is_leap = is_year_leap(year_to_check)

print(f"Год {year_to_check}: {is_leap}")