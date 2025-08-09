def main():
    n = int(input("Enter a number: "))
    num = 1
    total = 0

    print("Even numbers from 1 to ", n, ":")
    while num <= n:
        if num % 2 == 0:
            print(num, end=" ")
            total += num
        num += 1

    print("\nTotal sum of even numbers:", total)

if __name__ == "__main__":
    main()