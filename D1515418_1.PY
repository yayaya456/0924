x = int(input("請輸入一個 0-15 的整數: "))
if 0 > x or x > 15:
    print("輸入錯誤")
else:
   a1 = x % 2          
   a2 = (x // 2) % 2  
   a3 = (x // 4) % 2   
   a4 = x // 8    
   print(f"二進制：{a4}{a3}{a2}{a1}")
   b1 = x % 8
   b2 = x // 8
   print(f"八進制：{b2}{b1}")
   if x < 10:
       s = str(x) 
   elif x == 10:
            s = "A"
   elif x == 11:
            s = "B"
   elif x == 12:
            s= "C"
   elif x == 13:
            s = "D"
   elif x == 14:
            s = "E"
   elif x == 15:
            s = "F"
   print(f"十六進制:{s}")