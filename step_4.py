import time
import numpy as np


def func1(all_elements, subset_elements):
    """Description:The default way to find the intersection of two sets 
    """
    start = time.time()
    verified_elements = []
    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def func2(all_elements, subset_elements):
    """Description:The method of finding intersection of two sets using built-in function of numpy-intersect1d
    """
    start = time.time()
    verified_elements = np.intersect1d(np.array(subset_elements), np.array(all_elements))

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


def func3(all_elements, subset_elements):
    """Description:The method of finding intersection of two sets using set data structure of Python
    """
    start = time.time()
    verified_elements = set(subset_elements) & set(all_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


with open('subset_elements.txt') as f:
    subset_elements = f.read().split('\n')

with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')


def main():
    print(func1.__doc__)
    func1(all_elements, subset_elements)

    print(func2.__doc__)
    func2(all_elements, subset_elements)

    print(func3.__doc__)
    func3(all_elements, subset_elements)

if __name__ == "__main__":
    main() 