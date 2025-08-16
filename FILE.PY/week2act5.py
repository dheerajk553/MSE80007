class WordCount:
    def __init__(self, sentence):
        # Initialize the class with the user sentence
        self.sentence = sentence

    def countwords(self):
        # Split sentence into words and return the count
        return len(self.sentence.split())

# Main function (program starts here)
def main():
    
    sentence = input("Enter a sentence: ")

    # Create object of WordCount class
    wc = WordCount(sentence)


    print("Number of words:", wc.countwords())

if __name__ == "__main__":
    main()