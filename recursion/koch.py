import math

A = []


def koch(left, right, n):
    if n == 0:
        return

    # point 1/3
    s = ((2.0 * left[0] + 1.0 * right[0])/3.0, (2.0 * left[1] + 1.0 * right[1])/3.0)

    # point 2/3
    t = ((1.0 * left[0] + 2.0  * right[0])/3.0, (1.0 * left[1] + 2.0 * right[1])/3.0)

    u = (
        math.cos(math.pi/3.0)*(t[0]-s[0]) - math.sin(math.pi/3.0)*(t[1]-s[1]) + s[0],
        math.sin(math.pi/3.0)*(t[0]-s[0]) + math.cos(math.pi/3.0)*(t[1]-s[1]) + s[1]
    )
    koch(left, s, n-1)
    A.append(s)
    koch(s, u, n-1)
    A.append(u)
    koch(u, t, n-1)
    A.append(t)
    koch(t, right, n-1)


if __name__ == '__main__':
    n = int(input())
    left = (0.00000000, 0.00000000)
    right = (100.00000000, 0.00000000)
    A.append(left)
    koch(left, right, n)
    A.append(right)

    for a in A:
        print('{:.8f} {:.8f}'.format(a[0], a[1]))
