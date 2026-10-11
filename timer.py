"""
Program version 1.0.0v
Program made in 20 minutes 

"""
import time
import os


def set_time():
    try:
        hours = int(input("Podaj godzinę:  "))
        minutes = int(input("Podaj minuty:  "))
        seconds = int(input("Podaj sekundy: "))

    except ValueError:
        os.system("cls")
        print("Wpisz liczbę, nie litery.")
        time.sleep(1)
        os.system("cls")
        return set_time()

    return hours, minutes, seconds


hours, minutes, seconds = set_time()

while True:
    os.system("cls")

    print("┌--------------┐")
    print(f"| {hours:02} : {minutes:02} : {seconds:02} |")
    print("└--------------┘")

    time.sleep(1)
    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

    if hours == 24:
        hours = 0
