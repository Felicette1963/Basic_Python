import random

# 2023-06-14
class Basic_06:
    def __init__(self):
        # self.Python_Basic_01();
        # self.Python_Basic_02();
        self.Python_Basic_very_import();

    def Review(self):
        """### 반복문의 변수 i를 변경할 수 있을까?"""

        j = 0
        for i in range(10):
            print(i, j)
            j += i
            i = 100
            print(i, j)
            # 다음 루프에서 새롭게 range 안에 있는 요소가 할당
            # -> 루프 중에서는 반복 요소 할당에 쓰이는 i는 새롭게 값을 저장해도 계속 덮어씌워진다
        print(i, j)  # 루프가 끝나면 i는 마지막 값으로 저장되어 있다
        # 다음과 같이 for와 range로 반복하면서 변수 i를 변경하면 어떻게 될까요?

        """### 입력한 횟수대로 반복하기"""

        # int(input())으로 입력을 받고, 해당 내용을 range(N) <- 넣으면 가능.
        # 백준 : A+B -3

        """## 시퀀스 객체로 반복하기

        지금까지 for에 range를 사용하면서 눈치챘겠지만, for에 range 대신 시퀀스 객체를 넣어도 될 것 같죠? 맞습니다. for는 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있습니다.

        for에 range 대신 리스트를 넣으면 리스트의 요소를 꺼내면서 반복합니다.
        """

        snacks = ["새우깡", "양파깡", "고구마깡", "비 - 깡"]
        for snack in snacks:
            # snack <- 시퀀스 객체의 개별 요소들을 받아주는 변수
            print(snack)

        """# while

        ## while 반복문 사용하기

        while 반복문은 조건식으로만 동작하며 반복할 코드 안에 조건식에 영향을 주는 변화식이 들어갑니다.
        """

        """while 반복문의 실행 과정입니다. 먼저 초기식부터 시작하여 조건식을 판별합니다. 이때 조건식이 참(True)이면 반복할 코드와 변화식을 함께 수행합니다. 그리고 다시 조건식을 판별하여 참(True)이면 코드를 계속 반복하고, 거짓(False)이면 반복문을 끝낸 뒤 다음 코드를 실행합니다.

        여기서는 조건식 → 반복할 코드 및 변화식 → 조건식으로 순환하는 부분이 루프(loop)입니다.

        ### while 반복문 사용하기

        다음과 같이 while 반복문은 조건식을 지정하고 끝에 :(콜론)을 붙인 뒤 다음 줄에 반복할 코드와 변화식을 넣습니다. 초기식은 특별한 것이 없고 보통 변수에 값을 저장하는 코드입니다.

        ```
        초기식
        while 조건식:
             반복할 코드
             변화식
        ```

        while 다음 줄에 오는 코드는 반드시 들여쓰기를 해줍니다.
        """

        # 이제 while 반복문으로 'Hello, world!'를 100번 출력해보겠습니다.

        w = 0  # 반복이 진행될 때마다 변화할 값 -> 시작점
        while w < 100:  # while 조건식 == True 일 때는 반복 -> 끝점
            # while not w >= 100:
            print(w, 'Hello, world!')
            # print(w + 1, 'Hello, world!')
            # w = w + 1  # 그대 있으면 무한루프 -> w를 변화시키는 '변화식'
            w += 1  # -> 증가폭

        """먼저 while 반복문에 사용할 변수 i에 0을 할당합니다. 그리고 while에는 조건식만 지정하면 됩니다. 특히 while 반복문은 반복할 코드 안에 변화식을 지정해야 합니다. 만약 조건식만 지정하고 변화식을 생략하면 반복이 끝나지 않고 계속 실행(무한 루프)되므로 주의해야 합니다.

        i < 100과 같이 조건식을 지정하여 i가 100 미만일 때만 반복하고, i가 100이 되면 반복을 끝내도록 만들었습니다. 그리고 반복할 코드의 변화식에는 i += 1로 i를 1씩 증가시켰으므로 i가 0부터 99까지 증가하면서 100번 반복하게 됩니다. 물론 변화식 i += 1을 풀어서 i = i + 1로 만들어도 동작은 같습니다.

        ### 초깃값을 1부터 시작하기
        """

        # 이번에는 i에 0이 아닌 1을 할당하여 'Hello, world!'를 100번 출력해보겠습니다.

        """i에 1을 넣었으므로 while의 조건식은 i <= 100과 같이 지정합니다. 따라서 i가 1부터 100까지 증가하므로 100번 반복하게 됩니다. 만약 i가 101이 되면 i <= 100은 거짓( False)이므로 반복문을 끝냅니다.

        ### 초깃값을 감소시키기

        지금까지 초깃값을 증가시키면서 루프를 실행했습니다. 반대로 초깃값을 크게 주고, 변수를 감소시키면서 반복할 수도 있습니다. 다음은 100부터 1까지 100번 반복합니다.
        """

        w = 100  # 반복이 진행될 때마다 변화할 값 -> 시작점
        while w > 0:  # while 조건식 == True 일 때는 반복 -> 끝점
            print(w, 'Hello, world!')
            w -= 1

        dice = 0
        while dice != 3:
            dice = random.randint(1, 6)
            print("주사위에서 " + str(dice) + "가 나왔습니다")

        w = 0
        while True:
            w += 1
            lucky = ["SSS", "SS", "SS", "S", "S", "S"] + ["A"] * 30
            c = random.choice(lucky)
            if lucky == "SSS":
                break
            print(w, c)

        print(random.choice(["콜라", "사이다", "환타"]))
        lucky = ["SSS", "SS", "SS", "S", "S", "S"] + ["A"] * 30
        # for i in range(10):
        #     print(random.choice(lucky))

        w = 0
        while True:
            w += 1
            lucky = ["SSS", "SS", "SS", "S", "S", "S"] + ["A"] * 30
            c = random.choice(lucky)
            print(w, c)
            if c == "SSS":
                break

        money = 10000
        for i in range(100):
            money -= 1000
            print(i, money)
            if money <= 0:
                break

        money = 10000
        for i in range(100):
            # money -= 1000
            # money -= random.choice([-1, 0.5, 0, 0.5, 1]) * 1000
            money -= random.choice([-2, 1, 0.5, 0.5, 1]) * 1000
            print(i + 1, money)
            if money <= 0:
                break

        easy = True
        count = 0
        for i in range(10):
            if easy and i % 2 == 0:
                continue
            count += 1
            print(i, count)

        easy = True
        # easy = False
        count = 0
        for i in range(10):
            # if easy and i % 2 == 0:
            #     continue
            if easy and i > 5:
                break
            count += 1
            print(i, count)

    def Python_Basic_01(self):
        # 리스트 응용

        ## 리스트 조작하기

        ### 리스트에 요소 추가하기

        '''
        * append : 요소 하나를 추가 (맨 뒤에)
        * extend : 리스트를 연결하여 확장
        * insert : 특정한 인덱스에 요소를 추가
        '''

        ### 기존 리스트에 요소 하나 추가하기

        a = [10, 20, 30]
        print(a)
        # a = [10, 20, 30, 500] # 재할당 (다시 대입하지 않아도...)
        a.append(500)  # append : 리스트 맨 뒷자리에 새로운 원소(요소)를 추가
        # ? : 없던 인덱스에는 값을 할당할 수 X -> append를 사용하게 되면 신규 인덱스를 생성 및 값 할당
        # '리스트'라는 자료형, 타입, 클래스에 딸린 내장 기능 = 메소드.
        print(a)

        # b = []
        b = list()
        print(b)
        b.append(10)
        print(b)

        ### 리스트 안에 리스트 추가하기
        l = [[0] * 5] * 5  # 행 -> 열
        print(l, len(l))
        l.append([1])
        print(l, len(l))  # append 시에 길이는 무조건 1씩 증가

        ### 리스트 확장하기
        a = ["사과"]
        b = ["배"]
        print(a + b)
        a = ["사과"] * 3
        print(a)
        a.extend(b)  # append, extend -> 다시 할당/대입 과정?
        # inplace -> 대체 -> 메소드를 실행하는 순간 굳이 재대입/재할당 -> 원래 변수에 영향을 미친다
        print(a)
        print(a + b)
        print(a + b)
        print(a + b)
        print(a + b)
        print(a)  # a는 변하지 않는다! (연산자로 하면) *, + 똑같은데...
        # append, extend? -> 원본에 영향을 미친다 (할당연산자 없이 쓰는 애들)
        # extend  => + 가 아니라 += 의 역할을 한다
        # extend는 전달받은 리스트의 원소를 하나씩 반복하면서 append라고 보시면 됨.
        l = [1, 2, 3]
        l2 = [4, 5, 6]

        # 1.
        l3 = l + l2
        print("#1", l3)

        # 2.
        l3 = []
        l3.extend(l)
        l3.extend(l2)
        print("#2", l3)

        # 3.
        l3 = []
        for v1 in l:
            l3.append(v1)  # 2배씩으로 만들어서 더해야한다
        for v2 in l2:
            l3.append(v2)
        print("#3", l3)

        # 3-1.
        l3 = []
        for v1 in l:
            # break? continue?
            l3.append(v1 * 2)  # 2배씩으로 만들어서 더해야한다
        for v2 in l2:
            l3.append(v2 * 2)
        print("#3", l3)

        ### 리스트의 특정 인덱스에 요소 추가하기
        # 리스트객체.insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다.
        a = list(range(10, 40, 10))
        print(a)  # [10, 20, 30]
        # a.insert(2, 15)  # 인덱스 2번째
        a.insert(1, 15)  # 순서상 2번째 자리
        print(a)
        '''
        * insert(0, 요소): 리스트의 맨 처음에 요소를 추가
        * insert(len(리스트), 요소): 리스트 끝에 요소를 추가
        '''
        a.insert(0, 5)  # 파이썬 상 속도를 많이 잡아먹음 -> stack, queue, deque. (자료구조)
        # index 바탕으로 어느 지점에 값을 넣어줘야하나 '찾는 로직' => 느린 메소드.
        a.insert(len(a), 100)  # 굳이 할 필요가 없다
        # a.append(100)
        print(a)

        ### 리스트에서 요소 삭제하기
        print("삭제 전", a)
        del a[0]
        print("삭제 후", a)
        store = [10000, 2000, 5162]
        # 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
        print(store)
        print(store[-1])
        del store[-1]
        print(store)

        # 리스트에서 특정 인덱스 값을 찾아서 삭제 -> 반환

        store = [10000, 2000, 5162]
        # 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
        print(store)
        # print(store[-1])
        # del store[-1]
        # pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환
        p = store.pop()  # pop(-1), pop(len(..)-1)
        print(p)
        print(store)

        store = [10000, 2000, 5162]
        print(store)
        p = store.pop(0)  # 인덱스 -> 인덱스 번째의 값을 반환하고, 해당 값을 리스트에서 삭제
        # 리스트객체.pop(인덱스) : 해당 인덱스의 값을 꺼내옴. (인덱스가 없으면 -1로 default)
        print(p)
        print(store)

        # pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제

        # 리스트에서 특정 값을 찾아서 삭제
        cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '레드벨벳 쿠키']
        print(cookies)
        # r = cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
        # print(r)
        cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
        # 특정한 값을 찾는 기능.
        print(cookies)
        # 리스트.remove(값) -> 해당 값의 요소를 삭제

        print(cookies.index("오레오 쿠키"))
        # 리스트.index(값) -> 해당 값의 요소의 인덱스를 반환)
        # idx = cookies.index("오레오 쿠키")
        # del cookies[idx]
        cookies.remove("오레오 쿠키")
        print(cookies)

        cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '마카다미아 쿠키', '레드벨벳 쿠키', '마카다미아 쿠키']
        # index 혹은 remove 사용했을 때, 무엇을 검색 또는 삭제해줄까요?
        print("cookies.index(\"마카다미아 쿠키\")", cookies.index("마카다미아 쿠키"))  # 1개만 나옴
        # 가장 먼저 발견되는 1개. (index 0부터해서...)

        index = 0
        value = "마카다미아 쿠키"
        # for c in cookies:
        # for i, c in enumerate(cookies):
        for i in range(len(cookies)):
            # if c == value:
            if cookies[i] == value:
                # del(delete) ... -> remove
                break
            # index += 1
        # print(index)
        print(i)

        print(cookies)
        # print(cookies.index("초코파이")) # ValueError: '초코파이' is not in list
        print("초코파이" in cookies)
        # cookies.remove("초코파이") # list.remove(x): x not in list

        store = ["마제소바", "토리동", "부타동"]
        # while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
        while True:
            print(store)
            order = input("무엇을 주문하시겠습니까? : ")
            if order in store:
                store.remove(order)  # 요소를 계속 제거...
                print(order + "을(를) 드리겠습니다")
            else:
                print(order + "은(는) 현재 없는 메뉴입니다")
            if len(store) == 0:  # if not store:
                break
        print("장사 끝났습니다")

    def Python_Basic_02(self):
        ## 특정 값의 개수 구하기
        cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키']
        # 쿠키의 개수
        print('cookies.count("치즈 쿠키")', cookies.count("치즈 쿠키"))  # 정확하게 일치하는지
        song = "'마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키'"
        print(song.count("쿠키"))  # 문자열(string) -> 특정한 단어가 몇 개 존재하는지?

        ### 리스트의 뒤집기
        print(cookies)
        print(cookies[::-1])
        print(list(reversed(cookies)))
        print(cookies)  # 원본에 반영이 안됨 (뒤집었다는 것)
        cookies.reverse()
        print("cookies.reverse() :", cookies)
        print(cookies)

        ### 리스트의 요소 정렬
        '''
        sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

        sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
        sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
        '''

        import random
        r_number = random.choices(range(1000), k=10)
        print(r_number)

        ### 리스트의 요소 정렬
        '''
        sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

        sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
        sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
        '''
        import random
        r_number = random.choices(range(1000), k=10)
        print(r_number)
        print(sorted(r_number))  # reversed -> 뒤집어진, sorted -> 정렬된
        print("<오름차순>")
        for r in sorted(r_number):
            print(r)
        # 오르막 -> 오름차순. (ascending) - asc (데이터가 등장 혹은 전개되는 방향)
        # 1, 2, 3....
        # 내리막 -> 내림차순  (descending) - desc
        # 100, 99, 98, ...
        print(sorted(r_number)[::-1])
        print(sorted(r_number, reverse=True))  # sorted 정렬 -> 오름차순 -> 뒤집겠니?
        print(list(reversed(sorted(r_number))))  # reversed -> print -> list를 묶어줘야함
        # reversed(함수) & 리스트.reverse()
        # sorted(함수) & 리스트.sort()
        r_number = random.choices(range(1000), k=10)
        print("r_number", r_number)
        r_number.sort()
        print("r_number.sort()", r_number)  # 오름차순

        r_number = random.choices(range(1000), k=10)
        print("r_number", r_number)
        r_number.sort(reverse=True)
        print("r_number.sort(reverse=True)", r_number)  # 내림차순

        ### 리스트의 모든 요소 삭제
        print("cookies", cookies)
        cookies.clear()
        print("cookies", cookies)

    def Python_Basic_very_import(self):
        ### 리스트할당: 주소값을 같은 값으로 할당되어 같이 변경되는 현상
        a = [0,0,0,0]
        b = a       # b를 a를 할당
        print(a)
        a[0] = 100
        a[2] = 50
        print(b)    # b의 값이 바뀐다.
        print("a와 b가 같냐:", a is b)   # a 와 b가 같다라는 답이 온다.

        ### 할당 회피 방법
        # 앝은 할당 방법
        # 슬라이싱 방법
        c = a[:]
        # .copy()
        d = a.copy()
        a[1] = 500
        a[3] = 450
        print(c)        # c의 값이 바뀌지 않는다.
        print(d)        # d의 값이 바뀌지 않는다.
        print(a is c)   # a와 b는 같지 않다.
        print(a is d)   # a와 d는 같지 않다.

        ### 2차원 리스트 할당
        e = [a,b,c,d]
        f = e.copy() # e[:] -> 얕은 복사

        print(e is f)

        import copy  # copy
        g = copy.deepcopy(e)
        print("g", g)
        a[0] = 21381238
        print("g", g)

        # 1. 할당 - 얕은 복사 : 할당 -> 특정한 데이터를 저장한 주소를 넘기는 것.
        # 2. 얕은 복사 -> 같은 데이터지만, 다른 주소를 가지도록 사본을 만드는
        # (내부에 들어있는 주소까지 연결을 끊어주진않아요)
        # 3. 깊은 복사 (import copy.deepcopy) -> 모든 주소들의 연결을 끊어버려서 사본을 만드는 것.

    def Python_Basic_03(self):
        # 합계
        s = 0
        for i in range(1, 10):  # 1 ~ 9.
            s += i
        print(s)
        # summarization -> sum
        print(sum(range(1, 10)))
        print(sum([329382, 129312328, 1231231]))

        s = ["바나나", "알러지", "원숭이"]
        # sum(s) # unsupported operand type(s) for +: 'int' and 'str' -> 0?
        # 문자열들은 sum을 쓸 수 X.
        c = ""
        for a in s:  # 1 ~ 9.
            c += a
        print(c)

        # 리스트 표현식 (리스트 컴프리헨션 - list comprehension)
        ## -> 리스트 안에 for 반복문과 if 조건문으로 -> 값들의 묶음을 표현.
        ## -> 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성 = 리스트 컴프리헨션
        ## [식 for 변수 in 시퀀스]

        a = []
        for i in range(10):
            a.append(i ** 2)
        print(a)
        a = [i ** 2 for i in range(10)]
        print(a)
        a = [i ** 0.5 for i in range(5, 10, 2)]
        print(a)
        a = [k ** 3.5 for k in range(3, 12, 3)]
        print(a)
        b = ["아메리카노", "카푸치노", "프라푸치노"]
        # c = []  # 맨 끝 2자리 옮기기
        # for v in b:
        #     c.append(v[-2:])
        # print(c)
        c = [v[-2:] for v in b]
        print(c)

        # 리스트 컴프리헨션 + if 조건문
        '''
        [식 for 변수명 in 리스트 if 조건식]  # if 조건식을 만족시키는 값만, 식으로 표현
        '''
        d = []
        for v in b:
            # print(v)
            if "푸" in v:
                # print(v)
                d.append(v)
        print("d", d)
        e = [v for v in b if "푸" in v]
        print("e", e)

        # 조건부 표현식 (삼항연산자) -> for 앞에 (식)
        e = ["나 단 거 좋아해" if v == "프라푸치노" else "나 단 거 싫어해" for v in b if "푸" in v]
        print("e", e)
        # 리스트 컴프리헨션의 if문은 -> 만족을 안 시키면 필터링. -> continue -> len이 바뀜 !!!!
        # 조건부 표현식(삼항연산자)는 조건의 T/F와는 상관없이 각 행이 여전히 존재. => 값. -> len 안바뀜

        # 문자열

        ## 문자열 조작하기

        ### 문자열 바꾸기

        '''
        문자열.replace('바꿀문자열','새문자열') -> 기존 문자열 안의 바꿀 문자열을 새 문자열로 '교체'
        -> 매번 사본이 나옴.
        '''
        greeting = "안녕하세요! 김파이썬씨"
        print(greeting)
        print(greeting.replace("파이썬", "코딩"))

        greeting = "안녕하세요! 김파이썬씨"
        print(greeting)
        print(greeting.replace("파이썬", "코딩"))
        print(greeting)
        new_greeting = greeting.replace("파이썬", "코딩")
        print(new_greeting)

        ### 문자열 분리하기
        ### 문자열.split(구분자) -> 구분자를 기준으로 문자열을 리스트화 (구분자를 입력 안하면 -> " "(공백))
        a = "태조 정종 태종 세종 문종 단종 세조"
        print(a.split(), a.split(" "), a.split("종"))  # '' <- 빈 구분자 이런건 X
        print(list(a))  # 문자열 -> 리스트 (한 글자씩 조개져서 표현)
        # map(int, input().split()) # -> 요소요소마다 int를 적용 -> split을 통해서 공백으로 나눠줘서...

        # map(int, input().split()) # -> 요소요소마다 int를 적용 -> split을 통해서 공백으로 나눠줘서...
        a = "태조,정종,태종,세종,문종,단종,세조"
        print(a.split(","))

        # 문자열 리스트 연결하기 (특정한 구분자를 입력)
        b = ['태조', '정종', '태종', '세종', '문종', '단종', '세조']
        # b.join(...) -> 이런 메소드가 없음?
        print("".join(b))  # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
        print(",".join(b))
        print(";".join(b))
        print(" ".join(b))  # -> join 빈("")게 가능. / split -> 빈("") 안 됨.

        # 일괄 대문자화, 소문자화
        t = "Hello, Python!"
        print(t.upper())  # uppercase
        print(t.lower())  # lowercase

        # 일괄 대문자화, 소문자화
        t = "Hello, Python!"
        print(t.upper())  # uppercase
        print(t.lower())  # lowercase
        u = "HELLO! PYTHON"
        l = "hello! python"
        print(t.isupper())
        print(u.isupper())
        print(l.isupper())
        print(t.islower())
        print(u.islower())
        print(l.islower())

        text = "                앞 뒤로 스페이스가 있는 경우               "
        print(text)
        print(text.replace(" ", ""))
        print(text.strip())
        print(text.lstrip())  # left
        print(text.rstrip())  # right

        # 문자열 서식

        # 데이터 -> str(...) print(..., ..., ...)
        # 파이썬 3.6 -> f-string (formatted string)

        ## f-string
        '''
        문자열 안에 변수의 값들을 삽입하기 위한 양식 -> 가독성, 편의성
        '''
        name = "박코딩"
        age = 30
        print("이름 :", name, "나이 :", age, "세")
        print("이름 : " + name + " 나이 : " + str(age) + "세")
        # f"" 혹은 f'' -> 이 안에 {변수명}
        print(f"이름 : {name} 나이 : {age}세")

        l = ["아메리카노", "십센치", "권정열"]
        print(f"내가 좋아하는 노래 : {l}")  # f"" f'' -> {}로 표시한다

        f = 0.123913912389  # 소수점 -> 소수점 밑의 2자리.
        print(f'{f:.2f}')  # f:.표시하고싶은자리수f
        print(f'{f:.4f}')  # f:.표시하고싶은자리수f
        # https://blockdmask.tistory.com/429

        # format 메소드 -> 변수에 사용하기에 편하게.
        # 서식 지정자 -> c, c++, java, printf

    def Python_Basic_04(self):
        # 딕셔너리 키-값 쌍의 삭제
        print(x)
        del x['a']  # del
        print(x)
        # print(x.pop()) # 딕셔너리는 순서가 없어서 pop() <- 기본값 처리 X
        print(x.pop('b'))  # 키와 함께... -> pop은 반환값
        print(x)
        # print(x.pop('hello')) # KeyError: 'hello'
        print(x.pop('hello', 0))  # 만약에 해당 삭제대상의 key가 없다면...
        # 딕셔너리.pop(키, 기본값)

        # 전체 삭제
        print(x)
        x.clear()
        print(x)

        # get을 통한 값 가져오기
        x = {
            'a': 10, 'b': 20, 'c': 30, 'd': 40,
        }
        # print(x['e'])  # KeyError: 'e'
        if 'e' in x:
            print(x['e'])
        print(x.get("a"))  # 있는 키
        print(x.get("e"))  # 없는 키 -> None (오류가 안 난다)
        print(x.get("e", 0))  # 없을 경우에 반환해줄 '기본값'
        # 딕셔너리.get(키, 기본값=None)

        # get을 통한 값 가져오기
        x = {
            'a': 10, 'b': 20, 'c': 30, 'd': 40,
        }
        # print(x['e'])  # KeyError: 'e'
        if 'e' in x:
            print(x['e'])
        print(x.get("a"))  # 있는 키
        print(x.get("e"))  # 없는 키 -> None (오류가 안 난다)
        print(x.get("e", 0))  # 없을 경우에 반환해줄 '기본값'
        # 딕셔너리.get(키, 기본값=None)

        # 딕셔너리 키-값-아이템
        for i in x:
            print(i)  # i -> key
            # 시퀀스 취급해서 반복 -> key
        # for문 반복시 요소로는 key.

        print(x.keys())  # 딕셔너리의 key 목록을 받는 메소드
        print(x.values())  # 딕셔너리의 value 목록을 받는 메소드
        print(x.items())  # 딕셔너리의 key, value 쌍을 받는 메소드
        for i in x.items():
            print(i)
        for k, v in x.items():  # 언패킹
            # print(k)
            # print(v)
            print(f"키 : {k}, 값 : {v}")




