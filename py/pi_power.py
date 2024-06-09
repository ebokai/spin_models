import math
import numpy as np 
from itertools import product


# Function to find the closest fraction p/q*pi^k to x
def closest_fraction_to_x(x, max_pow = 4):
    best_p, best_q, best_k = 0, 1, 0
    min_diff = float('inf')
    approximants = []
    diffs = []
    
    for k in range(2, 4):  # Range of k values to consider
        for p in range(1, 2**max_pow):
            for q in range(1, 2**max_pow):

                g = math.gcd(p,q)
                if g != 1:
                    continue
                # Compute the fraction p/q*pi^k
                val = p / q * math.pi**k
                # Calculate the difference between val and x
                diff = abs(val - x)

                diffs.append(diff)
                approximants.append([p,q,k])
                
                # Update the closest fraction if a better one is found
                if diff < min_diff:
                    min_diff = diff
                    best_p, best_q, best_k = p, q, k


    idx_sorted = [x for _, x in sorted(zip(diffs, np.arange(len(diffs))))]
    idx_best = np.array(idx_sorted[:10])
    diffs = np.array(diffs)
    best_diffs = diffs[idx_best]
    best_apps = [approximants[i] for i in idx_best]
    
    return best_apps, best_diffs

def integer_relation(x):
    X = np.array([x] + [math.pi**k for k in range(2,4)])
    p_range = 25
    interval = np.arange(-p_range, p_range + 1)
    best_S = np.inf 
    best_A = 0

    for A in product(interval, repeat = len(X)):

        A = np.array(A)
        if A[0] == 0:
            continue

        g1 = math.gcd(A[0],A[1])
        g2 = math.gcd(A[0],A[2])

        if g1 * g2 != 1:
            continue

        S = X @ A
        if np.abs(S) < 1e-2:
            print(A, np.abs(S))
        elif np.abs(S) > 1e-1:
            continue

        if np.abs(S) < best_S:
            best_A = A 
            best_S = np.abs(S)
            print(best_A, best_S, best_A / best_A[0])

    print(best_A, best_S)




# Number to find the closest fraction to
x = 15.64533478562885799159872
# Find the closest fraction

best_apps, best_diffs = closest_fraction_to_x(x, max_pow = 10223234232uiuiu)
integer_relation(x)

# # Print the result
i = 0
for app, diff in zip(best_apps, best_diffs):
    p, q, k = app 
    md = diff
    print(f"The {i}-closest fraction to {x} is {p}/{q}*pi^{k}, with a difference of {md:.2e}.")
    print(f'The approximate value of {p}/{q}*pi^{k} is: {p/q*math.pi**k}\n')
    i += 1