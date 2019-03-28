from matplotlib import pyplot as plt;from math import *

# This program will graph the indefinite integral of a given function.
# The actual function of the indefinite integral will not be calculated.
# However, the graph of the indefinite integral will be plotted at given points.
# This program is based on the concept that the indefinite integral function evaluated
# at a certain point will be equal to the definite integral from that point to 0.
# Riemann sums are therefore used to evaluate the definite integrals.


area = 0    # The area starts at 0 because it is summed up throughout the evaluation at each point.
dx = .000001    # What the width of each Riemann rectangle is equal to.
list2 = []  # The points on the graph of the indefinite integral will be added here.
list1 = [-5,-4,-3,-2,-1,0, 1, 2, 3, 4, 5]   # The points on the function to evaluate and graph.
bound1 = 0    # Starting first bound. The first item on the list must be evaluated from that point to 0.
index = 0  # This just tracks what number on the list the point is.

# This is the function to take the integral of. Change what ans is equal to to change the function.
# Example: ans=x**2 for x^2


def f(x):
    ans = 4*x**3
    return ans


# This function returns the list of values when the indefinite integral is evaluated at points in list1.
# Loops through all the points in list 1, evaluating definite integral at each one. Area is added along the way.
# So instead of evaluating 0 to 1, 0 to 2, etc.. it does 0 to 1, and adds that result to 1 to 2,
# in order to evaluate 0 to 2.
# The amount of rectangles in the definite integral is given as the difference between the two bounds divided
# by dx. 'for rectangle' loops over that.
# After each rectangle loop bound1copy increases, which represents evaluating the next rectangle up.
# After each point loop bound1 increases, representing moving to the next point.


def integrate_func(point):
    global area, index # Allows the outside area and index variables to be modified.
    if index == 0: # If this is the first item in list1...
        bound1copy = bound1 # ...the lower bound is at a certain point (specifically, 0).
                            # bound1copy is just a copy of bound1, so the outside variable is not modified.
    else:   # If the item is not the first item in list1...
        bound1copy = list1[index-1] #...then set the new lower bound to the previous point in list1.
    index += 1 # Tracks the index of point on the list.
    bound2 = point # Upper bound of the definite integral.
    for rectangle in range(abs((int((bound2-bound1copy)/dx)))): # The number of rectangles is absolute value of...
                                                                # ...upper bound minus lower bound, divided by dx.
        area += (f(bound1copy))*dx   # Add the area of the rectangle to the total area.
        bound1copy += dx    # Moving to the next rectangle up by moving the lower bound of the rectangle up by dx.
    return area # Function returns the value of the definite integral.


for point in list1:
    list2.append(round(integrate_func(point), 3))   # Adds the returned value of integrate_func rounded to 3 spots.

print(list2)
plt.plot(list1, list2, 'bo')    # Graphs list1 as x axis, and list 2 as y axis.
plt.show()

