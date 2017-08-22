def odds(a,b):
    print [sum(i for i in range(a,b+1) if i % 2 == 1)]


odds(4,13)
