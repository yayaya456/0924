x = int(input("請輸入一個 0-15 的整數: "))
if 0 > x or x > 15:
    print("輸入錯誤")
else:
   a1 = x % 2
   temp1 = x // 2    
   a2 = temp1 % 2
   temp2 = temp1 // 2
   a3 = temp2 % 2
   a4 = temp2 // 2
   print(f"二進制：{a4}{a3}{a2}{a1}")
   b1 = x % 8
   b2 = x // 8
   print(f"八進制：{b2}{b1}")
   if x < 10:
       hex_res = str(x) 
   elif x == 10:
            hex_res = "A"
   elif x == 11:
            hex_res = "B"
   elif x == 12:
            hex_res = "C"
   elif x == 13:
            hex_res = "D"
   elif x == 14:
            hex_res = "E"
   elif x == 15:
            hex_res = "F"
   print(f"十六進制:{hex_res}")