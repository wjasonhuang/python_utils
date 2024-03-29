"""
Floyd's cycle-finding algorithm O(lambda + mu)
lambda = length of loop, mu = index of first element of cycle
https://en.wikipedia.org/wiki/Cycle_detection
"""


def Floyd(f, x0):
    """
    f: function, x0: initial value
    find cycle in sequence x0, f(x0), f^2(x0), ..., f^n(x0), ...
    return mu, lambda where f^mu(x0) = f^lambda(f^mu(x0))

    f can be .next in case of linked list

    if cycle exists, once both slow and fast have entered into the loop,
    fast gets closer to slow by 1 at each step and eventually will meet

    assume they first meet at v = mu + k + n_slow * lambda = mu + k + n_fast * lambda
    => mu + k + n_fast * lambda = 2 * (mu + k + n_slow * lamdba)
    => mu + k = lambda * integer (n_fast - 2 * n_slow)
    => v = lambda * integer

    if we restart at x0, v and move by 1 each step, we will meet at mu as v + mu = mu
    """

    # find v
    slow, fast = f(x0), f(f(x0))
    while slow != fast:
        slow, fast = f(slow), f(f(fast))

    # find u
    mu, slow = 0, x0
    while slow != fast:
        slow, fast = f(slow), f(fast)
        mu += 1

    # find lambda
    lamda, fast = 1, f(fast)
    while slow != fast:
        fast = f(fast)
        lamda += 1

    return mu, lamda
