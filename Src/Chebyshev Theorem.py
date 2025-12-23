from statistics import pstdev
from statistics import mean
import matplotlib.pyplot as plt

#collects data points from user and creates a list
realdata = []
datapoints = input("Enter your population data points: ").split()
for i in datapoints:
    realdata.append(float(i))

#measurements of spread
sd = (pstdev(realdata))
mu = float(mean(realdata))
k_value = float(input("What is your K-value? "))
upperBound = mu + k_value * sd
lowerBound = mu - k_value * sd

#calculates the number of values within mu +- k_value * sd
values_in = []
for j in realdata:
    if lowerBound <= j <= upperBound:
        values_in.append(j)

#calculates the percentage of datapoints that are within the range and the minimum possible amount
total = len(realdata)
num_in = len(values_in)
percentIn = num_in / total * 100
minPercentK = (1 - (1 / (k_value ** 2))) * 100

#prints out our values
print("The standard deviation of this data set is " + str(sd) + ".")
print("The mean of this data set is " + str(mu) + ".")
print("The absolute minimum ratio of points within " + str(k_value) + " standard deviation(s) is " + str(minPercentK) + "%.")
print("The actual ratio of points within " + str(k_value) + " standard deviation(s) is " + str(percentIn) + "%.")
print(str(k_value) + " standard deviation(s) below the mean is " + str(lowerBound) + ".")
print(str(k_value) + " standard deviation(s) above the mean is " + str(upperBound) + ".")

#function for number line graph
def chebyshevplot(lowerBound, upperBound, realdata):
    fig1 = plt.figure()
    ax = fig1.add_subplot()
    ax.set_ylim(0,5)
    if lowerBound > 0 and upperBound > 0:
        ax.set_xlim (-2 * lowerBound, 2 * upperBound)
    elif lowerBound < 0 < upperBound:
        ax.set_xlim(2 * lowerBound, 2 * upperBound)
    elif lowerBound < 0 and upperBound < 0:
        ax.set_xlim(2 * lowerBound, -2 * upperBound)
    elif lowerBound == 0 and upperBound == 0:
        ax.set_xlim(-20,20)
    elif lowerBound == 0 and upperBound > 0:
        ax.set_xlim(-20, 2 * upperBound)
    else:
        ax.set_xlim(2 * lowerBound, 20)

    xMinimum = lowerBound
    xMaximum = upperBound

    y = 1.75
    height = 0.1

    plt.hlines(y, xMinimum, xMaximum)
    plt.vlines(xMinimum, y - height, y + height, "Red")
    plt.vlines(xMaximum, y - height, y + height, "Red")

    ax.text(-10, 4, f'The minimum possible amount within is {round(minPercentK, 2)}%')
    ax.text(-10, 3.5, f'The actual amount within is {round(percentIn, 2)}%')

    # draw a point on the line
    for t in realdata:
        plt.plot(t,1.75,'o')
    ax.set_axis_off()
    plt.show()

# calls the function
callable(chebyshevplot(lowerBound, upperBound, realdata))