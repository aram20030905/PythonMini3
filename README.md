# PythonMini3

his is a simple countdown timer program that allows users to enter a time in the format h:m:s (hours:minutes:seconds). The program will countdown from the entered time and display the time remaining in the format hh:mm:ss. If the program is interrupted by the user (e.g., pressing Ctrl+C), it will exit gracefully with a message.

Features
Accepts time input in h:m:s format (hours:minutes:seconds).
Performs countdown and displays the time remaining in a 24-hour clock format (hh:mm:ss).
Handles user interruption (Ctrl+C) and exits gracefully.
Provides feedback if the input format is invalid, or if hours, minutes, or seconds are out of range.
Requirements
Python 3.x (Tested with Python 3.7 and later)
time module (built-in)
How to Run
Running the Program
Clone the repository or download the main.py file.

Open a terminal or command prompt and navigate to the directory where the main.py file is located.

Run the script using the following command:

bash
Copy
python main.py
You will be prompted to enter a time to countdown (in the format h:m:s). For example, you could enter 1:30:00 for 1 hour and 30 minutes.

Example Input/Output
Example 1: Valid Countdown Input
less
Copy
Insert time to count down (h:m:s): 0:02:10
Countdown started...
00:02:10
00:02:09
00:02:08
...
Time's up!
Example 2: Invalid Format Input
less
Copy
Insert time to count down (h:m:s): 2:70:00
The minute cannot be greater than 59. Please try again.
Insert time to count down (h:m:s): 2:30:00
Countdown started...
00:02:30
...
Time's up!
Example 3: User Interrupt (Ctrl+C)
less
Copy
Insert time to count down (h:m:s): 0:01:30
Countdown started...
00:01:30
^C
Program interrupted. Exiting...
Program Structure
countdown_timer():

This function receives the countdown time (hours, minutes, and seconds) and performs the countdown.
It prints the time remaining in hh:mm:ss format each second, and stops once the time reaches zero.
get_time_input():

This function prompts the user to enter a time in the h:m:s format.
It checks for valid input, such as ensuring that minutes and seconds are within a valid range (0-59), and the time is not negative.
If an invalid input is detected, the user will be asked to try again.
main():

This is the main entry point of the program. It handles the user interaction loop and allows the user to restart the timer after it finishes or is interrupted.
It also handles graceful exit when the user interrupts the program using Ctrl+C.
Error Handling
The program catches KeyboardInterrupt exceptions during both the countdown and input phases, ensuring that the program exits gracefully when interrupted.
If invalid input is provided (e.g., non-integer values or improper format), the user will be prompted to provide a correct input.
License
This project is licensed under the MIT License - see the LICENSE file for details.
