#練習讀取檔案
data =[] #空白清單
with open('food.txt','r') as f:
	for food in f:
		data.append(food.strip()) #會印出food.txt中的換行符號: \n
		#加上,strip()去除字串中的換行符號和空格
print(data)