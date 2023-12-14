import random
import string
def generate_password(length):
  #Define characters to be used for generating the password
  characters = string.ascii_letters + string.digits + string.punctuation
  #Generate the password using random choices from the characters
  password = ''.join(random.choice(characters) for i in range(length))
  return password

def main():
    try:
        #prompt user for desired password length
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid length greater than zero.")
            return
        
        #Generate the password
        password = generate_password(length)
        #Display the generated password
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()           

