caso = 1
while True:
    try:
        n1 = input()
        n2 = input()
        print('caso #%d:' % caso)
        menge = n2.count(n1)
        if menge == 0:
            print('Nao existe subsequencia')
        else:
            print('menged.Subsequencias: %d' % menge)
            menge = n2.rfind(n1)
            print('Pos: %d' % (int(menge)+1))
        print()
        caso += 1
        
    except EOFError:
        break