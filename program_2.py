# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 years old, it should display "adult".

def categorize_age(age):
    ageCategory = "TBD"
    ######################
    if age >= 20:
        ageCategory = "Adult"
    elif age < 20 and age >= 13:
        ageCategory = "Teenager"
    elif age < 13 and age > 1:
        ageCategory = "Child"
    elif age <= 1 and age >= 0:
        ageCategory = "Infant"
    else:
        ageCategory = "Invalid Age"
    #This program was written by Logan Gibson on 9/17/2025
    #Its name is "Age Categorizer"

    ######################


    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)