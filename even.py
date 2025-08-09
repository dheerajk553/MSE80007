def main():
    n = int(input("Enter any Number: "))
    total = 0

    print("Odd  numbers between 1 and", n, "are:")
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(number, end=" ")
            total += number
        

    print("\n sum of Odd numbers:", total)

if __name__ == "__main__":
    main()