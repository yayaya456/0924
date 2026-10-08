A=input(int("A="))
B=input(int("B="))
if 0<A<2 or 0<B<2:
    print("輸入錯誤")
elif A==1 or B==1:
    print("OR=1")
elif A==1 and B==1:
    print("AND=1")
elif A!=B:
    print("XOR=1")
elif A==B:
    print("XOR=0")