data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print("資料筆數", len(data))
print("第一筆:", data[0])
print('-----------------')
print("第二筆:", data[1])


