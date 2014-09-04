__author__ = 'mahadi'
from numpy import linspace
def f(x):
    return x**2-1
def g(x):
    return 1/x
def h(x):
    return x**4 - 8

def midpoint_method(f, a: (int, float), b:(int, float), n : int) -> float:
    h = (b-a)/n
    assert h > 0
    assert type(n)== int
    sum=0.0
    x=a+h/2 # first mid point
    while  (x < b):
        sum +=h*f(x)
        x +=h
    return sum
if __name__ == '__main__':
    print(midpoint_method(f,-2,2,10))
    print(midpoint_method(f,-2,2,10000))
    print(midpoint_method(g,0.1,2.0,100))
    print(midpoint_method(h,-10,20,1000))

def trapezoidal_method(f, a, b, n):
    """
    @param f: callable function
    @param a: start
    @param b: end
    @param n: intervals
    @return: area under the graph
    """
    x = linspace(a, b, n+1)
    y = [0]*(n+1)
    h = float(b - a) / n
    S = 0.0
    for i in range(0, n+1):
        y[i]=f(x[i])
        S += y[i]
    area=h/2*(2*S-y[0]-y[n])
    return area

if __name__ == '__main__':
    print(trapezoidal_method(f,-2,2,10))
    print(trapezoidal_method(f,-2,2,10000))
    print(trapezoidal_method(g,0.1,2.0,100))
    print(trapezoidal_method(h,-10,20,1000))

def simpson_method(f, a, b, n):
    """

    @param f:callable function
    @param a:start
    @param b:end
    @param n:intervals
    @return: approximate integral of function
    """
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3
if __name__ == '__main__':
    print(simpson_method(f,-2,2,10))
    print(simpson_method(f,-2,2,10000))
    print(simpson_method(g,0.1,2.0,100))
    print(simpson_method(h,-10,20,1000))

def test_midpoint():
        n = 100
        err = 1e-12
        assert 3-err <midpoint_method(g,0.1,2,100) < 3+err

def test_trapezoidal():
        n = 100
        err = 1e-12
        assert 3-err <trapezoidal_method(g,0.1,2,100) < 3+err

def test_simpson():
        n = 100
        err = 1e-12
        assert 3-err <simpson_method(g,0.1,2,100) < 3+err
