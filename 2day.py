import numpy as np
def calavgtemp(temps):
    return np.mean(temps) # np.mean() use for find the Average

def main():
    temp = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    avgtemp = calavgtemp(temp)
    highesttemp = np.max(temp)
    lowesttemp = np.min(temp)
    print(f" Average temperature for the week is: {avgtemp:.2f} °C")
    print(f"Highest  temperature: {highesttemp:.2f} °C")
    print(f"Lowest  temperature: {lowesttemp:.2f} °C")
# call main function
if __name__ == "__main__":
    main()