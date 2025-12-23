from statistics import pstdev, mean
from matplotlib.figure import Figure

#=========================== Chebyshev Figure Builder ===========================#
def build_chebyshev_figure(realdata: list[float], k_value: float):

    # measurements of spread
    standard_deviation = pstdev(realdata)
    mu = mean(realdata)
    upper_bound = mu + k_value * standard_deviation
    lower_bound = mu - k_value * standard_deviation

    # values within bounds
    values_in = [x for x in realdata if lower_bound <= x <= upper_bound]

    # percentages
    total = len(realdata)
    num_in = len(values_in)
    percentIn = (num_in / total * 100) if total else 0.0
    minPercentK = (1 - (1 / (k_value ** 2))) * 100

    # print statements
    print("The standard deviation of this data set is " + str(standard_deviation) + ".")
    print("The mean of this data set is " + str(mu) + ".")
    print("The absolute minimum ratio of points within " + str(k_value) + " standard deviation(s) is " + str(minPercentK) + "%.")
    print("The actual ratio of points within " + str(k_value) + " standard deviation(s) is " + str(percentIn) + "%.")
    print(str(k_value) + " standard deviation(s) below the mean is " + str(lower_bound) + ".")
    print(str(k_value) + " standard deviation(s) above the mean is " + str(upper_bound) + ".")

    # build figure
    fig = Figure(figsize=(6, 2.2), dpi=100)
    ax = fig.add_subplot(111)

    ax.set_ylim(0, 5)

    # keep your xlim logic
    if lower_bound > 0 and upper_bound > 0:
        ax.set_xlim(-2 * lower_bound, 2 * upper_bound)
    elif lower_bound < 0 < upper_bound:
        ax.set_xlim(2 * lower_bound, 2 * upper_bound)
    elif lower_bound < 0 and upper_bound < 0:
        ax.set_xlim(2 * lower_bound, -2 * upper_bound)
    elif lower_bound == 0 and upper_bound == 0:
        ax.set_xlim(-20, 20)
    elif lower_bound == 0 and upper_bound > 0:
        ax.set_xlim(-20, 2 * upper_bound)
    else:
        ax.set_xlim(2 * lower_bound, 20)

    y = 1.75
    height = 0.1

    # line + bounds
    ax.hlines(y, lower_bound, upper_bound)
    ax.vlines(lower_bound, y - height, y + height, colors="red")
    ax.vlines(upper_bound, y - height, y + height, colors="red")

    # text (kept basically the same)
    ax.text(ax.get_xlim()[0], 4, f'The minimum possible amount within is {round(minPercentK, 2)}%')
    ax.text(ax.get_xlim()[0], 3.5, f'The actual amount within is {round(percentIn, 2)}%')

    # points
    for t in realdata:
        ax.plot(t, y, 'o')


    return fig
