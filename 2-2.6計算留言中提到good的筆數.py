data = []
count = 0
with open('C:/Users/陳ivy/Desktop/read/reviews.txt','r')as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000==0:
            print(len(data))
print('檔案讀取完畢','一共有',len(data),'筆資料')
sum_len = 0
for d in data:
    sum_len=sum_len+len(d)
    print(sum_len)
print('留言平均長度是',sum_len/len(data))

good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good),'筆留言提到good')
print(good[0])