import math

def euclidean_distance(point1, point2):
    """Calculates the Euclidean distance between two points."""
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))
    return distance

def manhattan_distance(point1, point2):
    """Calculates the Manhattan distance between two points."""
    distance = sum([abs(a - b) for a, b in zip(point1, point2)])
    return distance

def hamming_distance(string1, string2):
    """Calculates the Hamming distance between two strings."""
    distance = sum(a != b for a, b in zip(string1, string2))
    return distance

def jaccard_distance(set1, set2):
    """Calculates the Jaccard distance between two sets."""
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    distance = 1 - (intersection / union)
    return distance