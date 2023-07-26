import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

# First iteration: Generate a random number and print it
lower = int(input("What is the lower bound? "))
upper = int(input("What is the upper bound? "))

# Include error checks to ensure the lower bound is less than the upper bound
while lower >= upper:
    print("Error: The lower bound must be less than the upper bound.")
    lower = int(input("What is the lower bound? "))
    upper = int(input("What is the upper bound? "))

# Generate a random number between the lower and upper bounds
generated_number = random.randint(lower, upper)
print(f"Generated number: {generated_number}")

# Second iteration: Prompt the user to guess the number and provide feedback
print("Guess a number between", lower, "and", upper)

while True:
    guess = int(input("What is your guess? "))
    
    if lower <= guess <= upper:
        if guess < generated_number:
            print("Nope, too low.")
        elif guess > generated_number:
            print("Nope, too high.")
        else:
            print("You got it!")
            break
    else:
        print("Error: Your guess must be between the lower and upper bounds.")
