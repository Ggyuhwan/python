
arr = ['ddd','aaaa','bbbb']
# for v in arr:
#     print(v)
#     print('abc')
for i, b in enumerate(arr):
    print('인덱스', i, b)

user_cnt = int(input('몇회?'))
cnt = 0
while cnt < user_cnt:
    cnt += 1
    if cnt == 2:
        continue
    if cnt == 10:

        break
    print(cnt*'*')