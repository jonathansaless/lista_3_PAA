def teste(m, n):
    print('chamei')
    if (m==0):
        return n + 1
    elif (n==0):
        return teste(m-1, 1)
    else:
        return teste(m-1,teste(m, n-1))
    
testando = teste(1, 2)