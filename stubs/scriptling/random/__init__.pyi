"""
Scriptling Random Library - Type stubs for IntelliSense support.

Random number generation functions. Python-compatible.
"""

from typing import List, Optional, Union

Number = Union[int, float]

def seed(a: Optional[Number] = None) -> None:
    """
    Initialize the random number generator.

    Parameters:
        a: Seed value (integer or float). If omitted, current time is used.

    Returns:
        None
    """
    ...

def randint(a: int, b: int) -> int:
    """
    Return a random integer N such that a <= N <= b.

    Parameters:
        a: Minimum value (integer)
        b: Maximum value (integer)

    Returns:
        Random integer in [a, b]
    """
    ...

def randrange(start: int, stop: Optional[int] = None, step: Optional[int] = None) -> int:
    """
    Return a randomly selected element from range(start, stop, step).

    Parameters:
        start: Start of range (or stop if only one argument)
        stop: End of range (exclusive). Optional.
        step: Step value. Optional, default: 1

    Returns:
        Random integer from the range
    """
    ...

def random() -> float:
    """
    Return a random float in the range [0.0, 1.0).

    Returns:
        Random float between 0.0 and 1.0
    """
    ...

def uniform(a: Number, b: Number) -> float:
    """
    Return a random float N such that a <= N <= b.

    Parameters:
        a: Minimum value
        b: Maximum value

    Returns:
        Random float in [a, b]
    """
    ...

def gauss(mu: Number, sigma: Number) -> float:
    """
    Return a random number from a Gaussian distribution.

    Parameters:
        mu: Mean of the distribution
        sigma: Standard deviation

    Returns:
        Random float from Gaussian distribution
    """
    ...

def normalvariate(mu: Number, sigma: Number) -> float:
    """
    Return a random number from a normal distribution.
    Same as gauss() but provided for compatibility.

    Parameters:
        mu: Mean of the distribution
        sigma: Standard deviation

    Returns:
        Random float from normal distribution
    """
    ...

def expovariate(lambd: Number) -> float:
    """
    Return a random number from an exponential distribution.

    Parameters:
        lambd: Rate parameter (1.0 divided by the desired mean)

    Returns:
        Random float from exponential distribution
    """
    ...

def betavariate(alpha: Number, beta: Number) -> float:
    """
    Return a random number from a beta distribution.

    Parameters:
        alpha: Shape parameter (must be positive)
        beta: Shape parameter (must be positive)

    Returns:
        Random float in [0, 1]
    """
    ...

def gammavariate(alpha: Number, beta: Number) -> float:
    """
    Return a random number from a gamma distribution.

    Parameters:
        alpha: Shape parameter (must be positive)
        beta: Scale parameter (must be positive)

    Returns:
        Random float from gamma distribution
    """
    ...

def triangular(low: Number, high: Number, mode: Optional[Number] = None) -> float:
    """
    Return a random number from a triangular distribution.

    Parameters:
        low: Minimum value
        high: Maximum value
        mode: Peak value (defaults to midpoint)

    Returns:
        Random float from triangular distribution
    """
    ...

def paretovariate(alpha: Number) -> float:
    """
    Return a random number from a Pareto distribution.

    Parameters:
        alpha: Shape parameter (must be positive)

    Returns:
        Random float from Pareto distribution
    """
    ...

def weibullvariate(alpha: Number, beta: Number) -> float:
    """
    Return a random number from a Weibull distribution.

    Parameters:
        alpha: Scale parameter (must be positive)
        beta: Shape parameter (must be positive)

    Returns:
        Random float from Weibull distribution
    """
    ...

def choice(seq: Union[List, str]) -> object:
    """
    Return a random element from a sequence.

    Parameters:
        seq: List or string to choose from

    Returns:
        Random element from the sequence
    """
    ...

def shuffle(list: List) -> None:
    """
    Shuffle a list in place using the Fisher-Yates algorithm.

    Parameters:
        list: List to shuffle (modified in place)

    Returns:
        None
    """
    ...

def sample(population: List, k: int) -> List:
    """
    Return k unique random elements from population.

    Parameters:
        population: List to sample from
        k: Number of elements to return

    Returns:
        List of k unique elements
    """
    ...

def choices(
    population: List,
    weights: Optional[List[Number]] = None,
    k: int = 1,
) -> List:
    """
    Weighted random sampling with replacement.

    Parameters:
        population: List to sample from
        weights: Optional list of weights (must match population length)
        k: Number of items to select (default: 1)

    Returns:
        List of k selected items
    """
    ...
