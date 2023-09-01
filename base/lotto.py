import random
def fn_lotto(user_num):
    user_num = int(input("로또 생성기 입니다 몇개를 원하셈>?"))
    for i in range(user_num):
        lotto = set()   # set 중복허용 x 여서 로또번호 생성에 적합
        while True:
            lotto.add(random.randint(1, 45)) # 랜덤 정수 1 ~ 45
            if len(lotto) == 6:
                break
        print(lotto)
    print("good luck")