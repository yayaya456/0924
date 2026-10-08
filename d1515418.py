print("請選擇您要轉換的類型：")
print("1. 攝氏 (℃) 轉 華氏 (℉)")
print("2. 華氏 (℉) 轉 攝氏 (℃)")
print("3. 公里 (km) 轉 英里 (mi)")
print("4. 英里 (mi) 轉 公里 (km)")
print("5. 公斤 (kg) 轉 磅 (lb)")
print("6. 磅 (lb) 轉 公斤 (kg)")
choice = input("請輸入選項 1-6: ")
v = float(input("請輸入數值: "))
if choice in ["1", "2", "3", "4", "5", "6"]:
    if choice == "1":
        result = (v * 9/5) + 32
        print(f"計算結果：{v} ℃ = {result:.2f} ℉")
        
    elif choice == "2":
        result = (v- 32) * 5/9
        print(f"計算結果：{v} ℉ = {result:.2f} ℃")
        
    elif choice == "3":
        result = v * 0.621371
        print(f"計算結果：{v} 公里 = {result:.2f} 英里")
        
    elif choice == "4":
        result = v / 0.621371
        print(f"計算結果：{v} 英里 = {result:.2f} 公里")
        
    elif choice == "5":
        result = v * 2.20462
        print(f"計算結果：{v} 公斤 = {result:.2f} 磅")
        
    elif choice == "6":
        result = v / 2.20462
        print(f"計算結果：{v} 磅 = {result:.2f} 公斤")
else:
    print("無效的選項")