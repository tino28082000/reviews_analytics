data = []
less = []
good = []
bad = []
wc = {}
def word_count(filename):
	with open(filename, 'r') as f:
		a = 0
		for message in f:
			words = message.split(' ')
			for word in words:
				if word in wc:
					wc[word] += 1
				else:
					wc[word] = 1

		for word in wc:
			if wc[word] > 1000000:
				print(word, '出現了', wc[word], '次')

		while True:
			key = input('請輸入想查找的字（退出請輸入q)：')
			if key == 'q':
				print('程式結束！')
				break
			else:
				print(key, '出現的次數為：', wc[key])

def analytics(filename):
	with open(filename, 'r') as f:
		total = 0
		count = 0
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

	for d in data:
		if 'bad' in d:
			bad.append(d)

	average_length = total / count
	print("資料筆數共有:", len(data), '筆')
	print('每筆資料平均長度為:', average_length )
	print('留言少於100字的筆數有:', len(less), '筆')
	print('留言包含 Good 的筆數有:', len(good), '筆')
	print('總共有', len(bad), '筆資料裡面有提到 bad') 
	
def main(filename):
	analytics(filename)
	word_count(filename)

main('reviews.txt')

	

