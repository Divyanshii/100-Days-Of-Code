def is_palindrome(s: str) -> bool:
    # Convert the input to string if it's not already
    s = str(s)
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Main function to take input from the user and check for palindrome
def main():
    user_input = input("Enter a string or number: ")
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")

if __name__ == "__main__":
    main()
