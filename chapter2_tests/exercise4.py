def calculate_area(shape, sides):
    if shape == 'circle':
        return 3.14 * (sides[0] ** 2)
    elif shape == 'triangle':
        return 0.5 * sides[0] * sides[1]
    elif shape == 'square':
        return sides[0] ** 2
    elif shape == 'rectangle':
        return sides[0] * sides[1]
    else:
        return None
