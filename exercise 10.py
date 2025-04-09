# this function is going to check weather it is odd or even
def eo_check(number):
    if number % 2 == 0:
     return f"The number {number} is even."
    else:
     return f"The number {number} is odd."
    
# the main function 
def main():
        eo_inp = int(input("enter a number, to evaluate if it's odd or even: ")) # asks the user to input a number 

        print(eo_check(eo_inp)) # prints the output  

# the entry point of the program 
if __name__ == "__main__":
    main()

    


