def check_col(a,b,c):
    for i in range (3):
        if a[i]==b[i]==c[i]:
            print a[i],'WINNER'
            return 1
def check_row(a,b,c):
    for i in range (1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],'WINNER'
            return 1
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],'WINNER'
            return 1
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],'WINNER'
            return 1
def check_dia(a,b,c):
    for i in range(1):
        if a[0]==b[1]==c[2]:
            print a[0],'WINNER'
            return 1
        elif a[2]==b[1]==c[0]:
            print a[2],'WINNER'
            return 1
