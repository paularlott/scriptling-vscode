"""
Scriptling Math Library - Type stubs for IntelliSense support.

Mathematical functions and constants.
"""

from typing import List, Union

Number = Union[int, float]

# Constants
pi: float
e: float
inf: float
nan: float
tau: float

def sqrt(x: Number) -> float:
    """
    Return the square root of x.

    Parameters:
        x: Non-negative number (integer or float)

    Returns:
        Float square root
    """
    ...

def pow(base: Number, exp: Number) -> float:
    """
    Return base raised to the power exp.

    Parameters:
        base: Base number
        exp: Exponent

    Returns:
        Float result
    """
    ...

def fabs(x: Number) -> float:
    """
    Return the absolute value of x as a float.

    Parameters:
        x: Number (integer or float)

    Returns:
        Float absolute value
    """
    ...

def floor(x: Number) -> int:
    """
    Return the floor of x.

    Parameters:
        x: Number (integer or float)

    Returns:
        Largest integer less than or equal to x
    """
    ...

def ceil(x: Number) -> int:
    """
    Return the ceiling of x.

    Parameters:
        x: Number (integer or float)

    Returns:
        Smallest integer greater than or equal to x
    """
    ...

def trunc(x: Number) -> int:
    """
    Truncate x to the nearest integer toward zero.

    Parameters:
        x: Number (integer or float)

    Returns:
        Integer
    """
    ...

def sin(x: Number) -> float:
    """
    Return the sine of x (radians).

    Parameters:
        x: Angle in radians

    Returns:
        Float sine value
    """
    ...

def cos(x: Number) -> float:
    """
    Return the cosine of x (radians).

    Parameters:
        x: Angle in radians

    Returns:
        Float cosine value
    """
    ...

def tan(x: Number) -> float:
    """
    Return the tangent of x (radians).

    Parameters:
        x: Angle in radians

    Returns:
        Float tangent value
    """
    ...

def asin(x: Number) -> float:
    """
    Return the arc sine of x in radians.

    Parameters:
        x: Number in range [-1, 1]

    Returns:
        Float in [-pi/2, pi/2]
    """
    ...

def acos(x: Number) -> float:
    """
    Return the arc cosine of x in radians.

    Parameters:
        x: Number in range [-1, 1]

    Returns:
        Float in [0, pi]
    """
    ...

def atan(x: Number) -> float:
    """
    Return the arc tangent of x in radians.

    Parameters:
        x: Number

    Returns:
        Float in [-pi/2, pi/2]
    """
    ...

def atan2(y: Number, x: Number) -> float:
    """
    Return the arc tangent of y/x in radians, correctly handling the quadrant.

    Parameters:
        y: Y coordinate
        x: X coordinate

    Returns:
        Float in [-pi, pi]
    """
    ...

def tanh(x: Number) -> float:
    """
    Return the hyperbolic tangent of x.

    Parameters:
        x: Number

    Returns:
        Float in [-1, 1]
    """
    ...

def log(x: Number) -> float:
    """
    Return the natural logarithm of x.

    Parameters:
        x: Positive number

    Returns:
        Float logarithm
    """
    ...

def log10(x: Number) -> float:
    """
    Return the base-10 logarithm of x.

    Parameters:
        x: Positive number

    Returns:
        Float logarithm
    """
    ...

def log2(x: Number) -> float:
    """
    Return the base-2 logarithm of x.

    Parameters:
        x: Positive number

    Returns:
        Float logarithm
    """
    ...

def log1p(x: Number) -> float:
    """
    Return log(1+x) accurately for small x.

    Parameters:
        x: Number

    Returns:
        Float
    """
    ...

def exp(x: Number) -> float:
    """
    Return e raised to the power x.

    Parameters:
        x: Number

    Returns:
        Float
    """
    ...

def expm1(x: Number) -> float:
    """
    Return exp(x)-1 accurately for small x.

    Parameters:
        x: Number

    Returns:
        Float
    """
    ...

def degrees(x: Number) -> float:
    """
    Convert radians to degrees.

    Parameters:
        x: Angle in radians

    Returns:
        Float in degrees
    """
    ...

def radians(x: Number) -> float:
    """
    Convert degrees to radians.

    Parameters:
        x: Angle in degrees

    Returns:
        Float in radians
    """
    ...

def hypot(x: Number, y: Number) -> float:
    """
    Return the Euclidean distance sqrt(x*x + y*y).

    Parameters:
        x: First coordinate
        y: Second coordinate

    Returns:
        Float
    """
    ...

def fmod(x: Number, y: Number) -> float:
    """
    Return the floating-point remainder of x/y.

    Parameters:
        x: Dividend
        y: Divisor (cannot be 0)

    Returns:
        Float remainder
    """
    ...

def gcd(a: int, b: int) -> int:
    """
    Return the greatest common divisor of a and b.

    Parameters:
        a: Integer
        b: Integer

    Returns:
        Integer GCD
    """
    ...

def factorial(n: int) -> int:
    """
    Return n! (n factorial).

    Parameters:
        n: Non-negative integer (0 <= n <= 20)

    Returns:
        Integer factorial
    """
    ...

def copysign(x: Number, y: Number) -> float:
    """
    Return x with the sign of y.

    Parameters:
        x: Magnitude value
        y: Sign value

    Returns:
        Float with magnitude of x and sign of y
    """
    ...

def cbrt(x: Number) -> float:
    """
    Return the cube root of x.

    Parameters:
        x: Number

    Returns:
        Float cube root
    """
    ...

def remainder(x: Number, y: Number) -> float:
    """
    Return the IEEE 754-style remainder of x/y.

    Parameters:
        x: Dividend
        y: Divisor

    Returns:
        Float remainder
    """
    ...

def nextafter(x: Number, y: Number) -> float:
    """
    Return the next floating-point value after x towards y.

    Parameters:
        x: Starting value
        y: Direction value

    Returns:
        Float next value
    """
    ...

def isnan(x: Number) -> bool:
    """
    Check if x is NaN (Not a Number).

    Parameters:
        x: Number to check

    Returns:
        True if x is NaN, False otherwise
    """
    ...

def isinf(x: Number) -> bool:
    """
    Check if x is infinite.

    Parameters:
        x: Number to check

    Returns:
        True if x is positive or negative infinity
    """
    ...

def isfinite(x: Number) -> bool:
    """
    Check if x is finite.

    Parameters:
        x: Number to check

    Returns:
        True if x is neither NaN nor infinite
    """
    ...

def erf(x: Number) -> float:
    """
    Return the error function of x.

    Parameters:
        x: Number

    Returns:
        Float in [-1, 1]
    """
    ...

def erfc(x: Number) -> float:
    """
    Return the complementary error function of x.

    Parameters:
        x: Number

    Returns:
        Float in [0, 2]
    """
    ...

def gamma(x: Number) -> float:
    """
    Return the gamma function of x.

    Parameters:
        x: Number

    Returns:
        Float
    """
    ...

def lgamma(x: Number) -> List[float]:
    """
    Return the natural log of the absolute value of the gamma function.

    Parameters:
        x: Number

    Returns:
        List [log_abs_gamma, sign]
    """
    ...

def comb(n: int, k: int) -> int:
    """
    Return the number of ways to choose k items from n (binomial coefficient).

    Parameters:
        n: Non-negative integer
        k: Non-negative integer

    Returns:
        Integer binomial coefficient
    """
    ...

def perm(n: int, k: int = ...) -> int:
    """
    Return the number of ways to choose k items from n with order.

    Parameters:
        n: Non-negative integer
        k: Non-negative integer (defaults to n)

    Returns:
        Integer permutation count
    """
    ...

def prod(iterable: List[Number], *, start: Number = ...) -> Union[int, float]:
    """
    Return the product of all elements.

    Parameters:
        iterable: List of numbers
        start: Starting value for multiplication (keyword only, default: 1)

    Returns:
        Integer for all-integer inputs, float otherwise
    """
    ...

def dist(p: List[Number], q: List[Number]) -> float:
    """
    Return the Euclidean distance between two points.

    Parameters:
        p: List of numbers (first point)
        q: List of numbers (second point, same dimension)

    Returns:
        Float Euclidean distance
    """
    ...

def softmax(x: List[Number]) -> List[float]:
    """
    Return numerically stable softmax of a vector.

    Parameters:
        x: List of numbers

    Returns:
        Probability distribution (list of floats summing to 1.0)
    """
    ...

def dot(a: List[Number], b: List[Number]) -> float:
    """
    Return the dot product of two vectors.

    Parameters:
        a: List of numbers
        b: List of numbers (same length as a)

    Returns:
        Float dot product
    """
    ...

def matmul(a: List[List[Number]], b: List[List[Number]]) -> List[List[float]]:
    """
    Matrix-matrix multiply. a is (M x K), b is (K x N). Returns (M x N) matrix.

    Parameters:
        a: Matrix as list of lists (M x K)
        b: Matrix as list of lists (K x N)

    Returns:
        Matrix as list of lists (M x N)
    """
    ...

def transpose(m: List[List[Number]]) -> List[List[float]]:
    """
    Transpose a 2D matrix. Rows become columns.

    Parameters:
        m: Matrix as list of lists

    Returns:
        New transposed matrix
    """
    ...

def mat_add(a: List[List[Number]], b: List[List[Number]]) -> List[List[float]]:
    """
    Element-wise addition of two matrices.

    Parameters:
        a: Matrix as list of lists
        b: Matrix as list of lists (same shape as a)

    Returns:
        New matrix with element-wise sums
    """
    ...
