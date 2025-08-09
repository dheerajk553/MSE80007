def fact():
    number = input("Enter the Numaric Number")
    a = int(number)

    if a < 0:
        return "number is lower than zero please enter greater than zero"

    elif 0 <= a <= 1:
        return 1

    else:
        result = 1
        for i in range(1, a + 1):
            print(", ",i)    
            result = result *i
        return result
    

if __name__ == "__main__":
    ab = fact()
    print("\n result:", ab)
