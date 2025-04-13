def binary_search(lst, elem):
    if elem not in lst:
        return -1
    return lst.index(elem)

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 4))