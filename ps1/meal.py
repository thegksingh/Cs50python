def main():
    ask = input("What time is it? (HH:MM) ")
            
    h = convert(ask)

    if 7.0 <= h <= 8.0:
        print("breakfast time")
    elif 12.0 <= h <= 13.0:
        print("lunch time")
    elif 18.0 <= h <= 19.0:
        print("dinner time")

def convert(ask):
    hour, minute = ask.split(":") 
    hours = int(hour)
    minutes = int(minute)
                                                                    
    return hours + (minutes / 60)

if __name__ == "__main__":
    main()