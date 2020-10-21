data = []
count = 0
total = 0
less = []
good = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		total = total + len(data[count])
		count += 1
		if count % 1000 == 0:
			print(len(data))

for d in data:
	if len(d) < 100:
		less.append(d) 

for d in data:
	if 'good' in d:
		good.append(d)

average_length = total / count
print("資料筆數共有:", len(data), '筆')
print('每筆資料平均長度為:', average_length )
print('留言少於100字的筆數有:', len(less), '筆')
print('留言包含 Good 的筆數有:', len(good), '筆')








