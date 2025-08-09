class StringManipulator:
    def __init__(self, name):
        # Init is a special method called the constructor of the class
        # self is the keyword we can't change this
        self.name = name

    def find_character(self, char):
        return self.name.find(char)

    def get_length(self):
        """Return the length of the string."""
        return len(self.name)

    def to_uppercase(self):
        """Return the string in uppercase."""
        return self.name.upper()
    
    def to_lowercase(self):
        """Return the string in lowercase."""
        return self.name.lower()


def main():
    # Create an instance of the StringManipulator class
    name1 = StringManipulator("hello")

    # Call the find_character method
    result = name1.find_character('x')
    print("Index of 'x':", result)  # Output: 1

    # Call the get_length method
    length = name1.get_length()
    print("Length of string:", length) 

    # Call the to_uppercase method
    uppercase_text = name1.to_uppercase()
    print("Uppercase string:", uppercase_text) 

     # Call the to_lowercase method
    lowercase_text = name1.to_lowercase()
    print("lowercase string:", lowercase_text)



if __name__ == "__main__":
    main()
