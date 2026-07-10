# Theory:
## Minimizing a function by hand-coded grid search evaluates the function
## at every point on a fixed grid and picks the smallest - simple, but
## its accuracy is capped by the grid spacing, and its cost grows
## exponentially with the number of dimensions (a 100-point grid in 1D
## becomes 100^d evaluations in d dimensions). scipy.optimize.minimize
## implements proper numerical optimization algorithms (BFGS, Nelder-Mead,
## etc.) that use the function's local behavior (gradient, or an
## approximation of it) to iteratively step toward a minimum, typically
## converging in a handful of evaluations rather than thousands, with
## precision limited only by numerical tolerance rather than grid spacing.
## This is the workhorse behind fitting models to data, calibrating
## parameters, and portfolio optimization - anywhere you need "the input
## that minimizes this cost function," not just "a good-enough answer."


# Packages:
## scipy.optimize.minimize - general-purpose function minimization (BFGS, Nelder-Mead, etc.)
## scipy.optimize.minimize_scalar - specialized minimizer for single-variable functions
## numpy.linspace / numpy.arange - build the evaluation grid for the brute-force approach
## scipy.optimize.brute - grid-search minimization built into scipy, for comparison


# Task:
## Given the coefficients (a, b, c) of a quadratic f(x) = a*x^2 + b*x + c
## with a > 0 (so it has a unique minimum), return the x value that
## minimizes f, accurate to 2 decimal places.
## Test1: Inputs: a = 1, b = -4, c = 3   Outputs: 2.0
## Test2: Inputs: a = 2, b = 0, c = 5   Outputs: 0.0
## Test3: Inputs: a = 1, b = 6, c = 9   Outputs: -3.0
## Hint:
## Ugly way: grid search - evaluate f(x) over a fixed range of x values at
## some step size, and return the x with the smallest f(x).
## Right way: scipy.optimize.minimize_scalar - a proper numerical
## optimizer converges to the minimum in a handful of evaluations.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def minimize_quadratic_ugly(a, b, c):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def minimize_quadratic(a, b, c):
    return minimize_quadratic_ugly(a, b, c)


# Tests:
def validate():
    cases = [
        (1, -4, 3, 2.0),
        (2, 0, 5, 0.0),
        (1, 6, 9, -3.0),
    ]
    for fn in (minimize_quadratic_ugly, minimize_quadratic):
        for a, b, c, expected in cases:
            result = fn(a, b, c)
            assert round(result, 2) == expected, (
                f"{fn.__name__}({a}, {b}, {c}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(minimize_quadratic_ugly(1, -4, 3))
    print(minimize_quadratic_ugly(2, 0, 5))
    print(minimize_quadratic_ugly(1, 6, 9))
