# define the correct password 
correct_password="1989"

# set the max number of attempts 
max_attempts=4

# start the loop and start up the number of attempts 
attempts=0

# begin a loop to keep asking for the password until it is coreect or attempts are over 
while attempts <max_attempts: 
    # ask user for password 
    entered_password=input("enter the password:")
       
    # check if the entered password is correct 
    if entered_password==correct_password:
        print("password correct! you can now login.")
        break # exit the loop when correct password is entered 
    else:
        attempt+=1 # increase the attempt counter 
        print(f"incorrect password. you have {max_attempts-attempts} attempts left.")

# if the loop ends without result 
if attempts==max_attempts:
    print("maximum attempts reached. you can no longer login.")
    