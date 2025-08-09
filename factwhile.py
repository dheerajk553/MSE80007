def calfact(n):
    fact= 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

while True:
    n = input("enter the number")
    # Checks if the input string is numeric vaule from 0 to 9
    # ensuring it is a valid non-negative integer before conversion.
    
    if n.isdigit():
        num = int(n)
        break
    else:
        print("enter zero or greather than zero /n")

        #if __name__ == "__main__":
        #ab = calfact()
        #print(" result:", num)


result = calfact(num)

print(f"{num} factorial is {result}")
