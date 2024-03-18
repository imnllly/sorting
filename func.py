def sa(a): # работает
    if len(a) > 1:
        p3 = a[1]
        a[1] = a[0]
        a[0] = p3
    print(a)
    return a

def sb(b): # работает
    if len(b) > 1:
        p3 = b[1]
        b[1] = b[0]
        b[0] = p3
    print(b)
    return b

def ss(a, b): # работает
    a = sa(a)
    b = sb(b)
    print(a, b)
    return a, b

def pa(a, b): # работает
    if len(b) > 0:
        a = a[::-1]
        a.append(b[0])
        b = b[1::]
        a = a[::-1]
    print(a, b)
    return a, b

def pb(a, b): # работает
    if len(a) > 0:
        b = b[::-1]
        b.append(a[0])
        a = a[1::]
        b = b[::-1]
    print(a, b)
    return a, b

def ra(a): # работает
    if len(a) > 0:
        c = []
        for i in range(1, len(a)):
            c.append(a[i])
        c.append(a[0])
        a = c
    print(a)
    return a

def rb(b): # работает
    if len(b) > 0:
        c = []
        for i in range(1, len(b)):
            c.append(b[i])
        c.append(b[0])
        b = c
    print(b)
    return b

def rr(a, b): # работает
    a = ra(a)
    b = rb(b)
    print(a, b)
    return a, b

def rra(a): # работает
    if len(a) > 0:
        c = []
        c.append(a[-1])
        for i in range(len(a) - 1):
            c.append(a[i])
        a = c
    print(a)
    return a

def rrb(b): # работает
    if len(b) > 0:
        c = []
        c.append(b[-1])
        for i in range(len(b) - 1):
            c.append(b[i])
        b = c
    print(b)
    return b


def rrr(a, b): # работает
    a = rra(a)
    b = rrb(b)
    print(a, b)
    return a, b

