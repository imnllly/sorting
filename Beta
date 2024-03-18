def sa(a): # работает
    if len(a) > 1:
        p3 = a[1]
        a[1] = a[0]
        a[0] = p3
        return a

def sb(b): # работает
    if len(b) > 1:
        p3 = b[1]
        b[1] = b[0]
        b[0] = p3
        return b

def ss(a, b): # работает
    a = sa(a)
    b = sb(b)
    return a, b

def pa(a, b): # работает
    if len(b) > 0:
        a = a[::-1]
        a.append(b[0])
        a = a[::-1]
        return a

def pb(a, b): # работает
    if len(a) > 0:
        b = b[::-1]
        b.append(a[0])
        b = b[::-1]
        return b

def ra(a): # работает
    a = a[::-1]
    return a

def rb(b): # работает
    b = b[::-1]
    return b

def rr(a, b): # работает
    a = ra(a)
    b = rb(b)
    return a, b

def rra(a): # работает
    if len(a) > 0:
        c = []
        c.append(a[-1])
        for i in range(len(a) - 1):
            c.append(a[i])
        a = c
        return a

def rrb(b): # работает
    if len(b) > 0:
        c = []
        c.append(b[-1])
        for i in range(len(b) - 1):
            c.append(b[i])
        b = c
        return b


def rrr(a, b): # работает
    a = rra(a)
    b = rrb(b)
    return a, b
