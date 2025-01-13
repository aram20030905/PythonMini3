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
        user_input = raw_input("Insert time to count down (h:m:s)")


        try:
            hours, minutes, seconds = map(int, user_input.split(":"))

            if hours < 0 or minutes < 0 or seconds < 0:
                print("Time cannot be negative. Please try again.")
                continue

            return hours, minutes, seconds

        except ValueError:

            print("Invalid input format. Please enter time in the format h:m:s (e.g., 1:30:45).")



def main():

    print("Welcome to the Countdown Timer Program!")

    while True:

        hours, minutes, seconds = get_time_input()


        countdown_timer(hours,minutes,seconds)


        restart = raw_input("\nWould you like to restart the timer? (y/n): ").strip().lower()



        if restart != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()


