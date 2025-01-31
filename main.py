import time
def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 +seconds
    print("\nCountdown started...")
    while total_seconds > 0:
        h, remainder = divmod(total_seconds,3600)
        m,s = divmod(remainder,60)
        print("{:02d}:{:02d}:{:02d}".format(h, m, s))
        time.sleep(1)
        total_seconds -=1
        print("\nTime's up!")
def get_time_input():
    while True:
        user_input = input("Insert time to count down (h:m:s)")
        parts = user_input.split(":")
        print(parts)
        if len(parts) != 3:
                print("Invalid format. You should only enter second, minute and hour ")
                continue
        try:
            hours, minutes, seconds = map(int,parts)
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Time cannot be negative. Please try again.")
                continue
            if minutes > 59:
                print("The minute cannot be greater than 59. Please try again")
                continue
            if seconds > 59:
                print("The second cannot be greater than 59. Please try again")
                continue

            return hours, minutes, seconds

        except ValueError:

            print("Invalid input format. Please enter only integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            exit(0)

def main():
    print("Welcome to the Countdown Timer Program!")

    while True:
        try:
            hours, minutes, seconds = get_time_input()
            countdown_timer(hours,minutes,seconds)
            restart = input("\nWould you like to restart the timer? (y/n): ").strip().lower()
            if restart != 'y':
                print("Goodbye!")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break 

if __name__ == "__main__":
    main()
