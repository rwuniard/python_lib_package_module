def add(a, b):
    return [x + y for x, y in zip(a, b)]

def multi(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")
    return [x * y for x, y in zip(a, b)]

def dot(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")
    return sum(x * y for x, y in zip(a, b))
