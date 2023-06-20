import time   # imports time module to show timer

while True: # while loop to check correct input of user
    timer = int(input("Enter the time in seconds: ")) # Prompt the user to enter the time in seconds

    if timer > 0:   # check if the user entered positive or negative number
        break # breaks loop to enter the for loop to print time
    else:
        print("Please enter positve number :)") # tells the user to put the positive number


for i in range(timer, 0, -1):  # for loop to enter time backwards and in format
    # Here % returns the modulus (mudulus is an operator which return the remainder after division by number
    # here the time entered by the user get divided by the 60 and the remainder is returned in seconds
    seconds = i % 60
    # here the time entered by the user get divided by the 60 and then again by 60 and then remainder is returned in minutes   
    minutes = (i // 60) % 60
    # here the time entered by the user get divided by the 3600 (equal to hour)
    hours = i // 3600
    # Use \r to move the cursor back to the beginning of the line
    # and overwrite the previously displayed time
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r") # it print the hours, minutes and seconds

    time.sleep(1)  # Pause the execution for 1 second

# Display "TIMES UP!!!" when the countdown finishes
print("TIMES UP!!!")


#suiiiiiiiiiiii