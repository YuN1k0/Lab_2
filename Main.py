class Array:

    def __init__(elem, a = []):
        elem.a = a

    def bubblesort(elem):
        for i in range(len(elem.a)):
            for j in range(0, len(elem.a) - i - 1):
                if elem.a[j] > elem.a[j + 1]:
                    x = elem.a[j]
                    elem.a[j] = elem.a[j+1]
                    elem.a[j+1] = x
        return elem.a