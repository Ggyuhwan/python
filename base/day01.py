num = 10
float_num = 10.8
str_msg = "Hello, Big"
bool_type = False
print(num)
print(float_num)
print(str_msg)
print(bool_type)

num = "hi"
print(num)
print('msg' * 10)
msg = """
    안녕 오늘은 수요일!
    주말까지 2일 밖에 없어서 아쉽다....
"""
print(msg.replace("수요일", "목요일"))
arr = msg.split('!')
print(arr)


user_msg = input('숫자 입력:').split()
print(user_msg)
p = "이름: %s 나이: %s"%("김유신", 65)
print(p)