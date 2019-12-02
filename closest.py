import math
import numpy as np
import matplotlib.pyplot as plt
import random

def distance(p1, p2):
    d = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
    return d

def closest_pair(ax, ay):
    list_size = len(ax)  
    
    # If the list has 3 points or less, find the min dist by comparison
    if list_size <= 3:
        return brute(ax) 

    # Splits the vector in half
    half = int(list_size/2)
    leftX = ax[:half] 
    rightX = ax[half:]
    
    midpoint = ax[half][0]  # Line between 2 halfs

    leftY = list()
    rightY = list()

    for x in ay: 
        if x[0] <= midpoint:
           leftY.append(x)
        else:
           rightY.append(x)
    
    (p1, q1, mi1) = closest_pair(leftX, leftY)
    (p2, q2, mi2) = closest_pair(rightX, rightY)
    
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    
    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

def brute(ax):
    mi = distance(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    list_size = len(ax)

    if list_size == 2:
        return p1, p2, mi
    
    for i in range(list_size - 1):
        for j in range(i + 1, list_size):
            if i != 0 and j != 1:
                d = distance(ax[i], ax[j])
                if d < mi:  # Update min_dist and points
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi

def closest_split_pair(ax, ay, delta, best_pair):
    full_size = len(ax)
    midpoint = ax[int(full_size/2)][0] 

    # Only check the points in a smaller distance then delta from the midpoint 
    margin = [x for x in ay if midpoint - delta <= x[0] <= midpoint + delta]
    best = delta  # delta is the best distance so far
    margin_size = len(margin) 

    for i in range(margin_size - 1):
        for j in range(i+1, min(i + 7, margin_size)):
            p, q = margin[i], margin[j]
            dst = distance(p, q)
            if dst < best:
                best_pair = p, q
                best = dst

    return best_pair[0], best_pair[1], best

def solution(points):
    px = sorted(points, key=lambda x: x[0])  # List sorted x-wise
    py = sorted(points, key=lambda y: y[1])  # List sorted y-wise
    p1, p2, dist = closest_pair(px, py)
    return p1,p2,dist

def random_without_repeat(arr):
    r = random.randint(0,100)
    if r in arr:
        r = random_without_repeat(arr)
    return r

def random_points(size):
    x = []
    y = []

    for i in range(size):
        x.append(random_without_repeat(x))
        y.append(random_without_repeat(y))

    return x, y

def print_points(arr):
    for p in arr:
        print('x: {}, y:{}'.format(p[0], p[1]))

if __name__ == "__main__":
    size = int(input("Amount of points: "))
    x, y = random_points(size)
    points = list(zip(x, y))  # Create a tupple list
    
    plt.scatter(x, y)
    plt.title("Closest Pair of Points")
    p1,p2,dist = solution(points)
    print_points(points)
    print("The smaller distance is {}, from point {} to point {}".format(dist, p1, p2))

    plt.plot([p1[0],p2[0]],[p1[1],p2[1]], 'ro-', label='Distance = {}'.format(dist))
    leg = plt.legend(loc="upper right", mode="expand", fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.show()
