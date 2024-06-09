import numpy as np
from itertools import combinations, product

# Function to generate all binary vectors of length k excluding the zero vector
def generate_binary_basis(k):
    # Generate all possible binary vectors of length k
    all_vectors = list(product([0, 1], repeat=k))
    # Exclude the zero vector
    basis = [vec for vec in all_vectors if any(vec)]
    return np.array(basis)

# Function to convert a binary vector to its integer representation
def binary_to_int(vec):
    return int("".join(map(str, vec)), 2)

# Function to generate unique models based on combinations of vectors from the basis
def generate_unique_models(basis, n):
    unique = []
    models = []
    strings = []
    integer_models = []

    # Generate all combinations of n vectors from the basis
    for comb in combinations(basis, n):
        # Convert combination to a numpy array for sum calculation
        comb_array = np.array(comb)
        
        # Sum of the vectors in the combination
        x = np.sum(comb_array, axis=0)
        
        # Sort the sum vector and the sums of the individual vectors in the combination
        ux = sorted(list(x))
        o = sorted([np.sum(vec) for vec in comb])

        
        
        # Create a unique identifier by combining sorted sums
        co = ux + o
        co_str = ''.join([str(k) for k in co])
        
        # If this combination is unique, add to the list of unique combinations and models
        if co not in unique:
            unique.append(co)
            strings.append(co_str)
            models.append([list(vec) for vec in comb])
            integer_models.append([binary_to_int(vec) for vec in comb])
        
            print(ux, o)

    return models, integer_models, strings

if __name__ == "__main__":
    # Example usage
    k = 3  # Length of the binary vectors
    n = 3  # Number of vectors to combine


    # Generate the basis for binary vectors of length k
    basis = generate_binary_basis(k)

    # Generate unique models
    models, integer_models, strings = generate_unique_models(basis, n)

    print(f"Number of unique models for n={n} and k={k}: {len(models)}")
    print("Models:")
    for model in models:
        print(model, np.sum(model, axis = 0))
    print("Integer Models:")
    for int_model in integer_models:
        print(int_model)
