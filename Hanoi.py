def Hanoi(N,beg,aux,end):
    if N==1:
        print beg+ "=>"+ end
    else:
        Hanoi(N-1,beg,end,aux)
        Hanoi(1,beg,aux,end)
        Hanoi(N-1,aux,beg,end)
print Hanoi(3,"1","2","3")