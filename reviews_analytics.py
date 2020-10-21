data = []
count = 0
total = 0


with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		total = total + len(data[count])
		count += 1
		if count % 1000 == 0:
			print(len(data))

average_length = total / count
print("資料筆數共有：", len(data))
print('每筆資料平均長度為：', average_length )





