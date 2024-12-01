from importlib.resources import read_text

def solve() -> tuple:
    # Open puzzle input and split into list
    data :list = read_text("adventofcode.resources.2024", "01.txt").split()
    # Convert list of strings to list of integers
    data = [int(i) for i in data]

    # Initialize variables
    total :int = 0
    similarity :int = 0

    # Create two seperate lists from input
    a_list :list = []
    b_list :list = []

    for i in range(0, len(data)):
        if i % 2:
            a_list.append(data[i])
        else:
            b_list.append(data[i])

    # Sort the lists
    b_list.sort()
    a_list.sort()

    for i in range(0, len(a_list)):
        # Calculate the distance between the two lists
        distance = abs(b_list[i] - a_list[i])
        total = total + distance

        # Calculate the similarity between the two lists
        if a_list[i] in b_list:
            similarity = similarity + a_list[i]

    return total, similarity
