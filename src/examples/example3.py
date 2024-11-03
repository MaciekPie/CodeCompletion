def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False
    return True


def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def mean(array):
    import numpy as np

    return np.mean(array)


def median(array):
    import numpy as np

    return np.median(array)


def mode(array):
    from scipy import stats

    return stats.mode(array)[0][0]


def standard_deviation(array):
    import numpy as np

    return np.std(array)


def variance(array):
    import numpy as np

    return np.var(array)


def covariance(array1, array2):
    import numpy as np

    return np.cov(array1, array2)[0, 1]


def correlation(array1, array2):
    import numpy as np

    return np.corrcoef(array1, array2)[0, 1]


def matrix_multiplication(matrix1, matrix2):
    import numpy as np

    return np.dot(matrix1, matrix2)


def matrix_inverse(matrix):
    import numpy as np

    return np.linalg.inv(matrix)


def determinant(matrix):
    import numpy as np

    return np.linalg.det(matrix)


def eigenvalues_eigenvectors(matrix):
    import numpy as np

    return np.linalg.eig(matrix)
