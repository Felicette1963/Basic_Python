
# 2023-06-09
class Basic_03:
    def __init__(self):
        # self.Review_Python_01();
        # self.Python_Basic_01();
        # self.Python_Basic_02();
        self.Python_Basic_03();

    # 복습 파일명: Review_***
    def Review_Python_01(self):
        """# 숫자 계산
        * 파이썬에서는 숫자의 자료형에 따라 결과가 달라질 수 있음
        * 파이썬에서는 숫자를 정수(int), 실수(float), 복소수(complex)로 구분
        * 보통 프로그래밍에서는 정수와 실수를 주로 사용
        ## 정수 계산
        ### 사칙연산
        """

        # 덧셈
        print("덧셈","1+1=",1+1);

        # 뺄셈
        print("뺄셈", "1-1=", 1 - 1);

        # 곱셈
        print("곱셈", "4*2=", 4*2);

        # 나눗셈
        print("나눗셈", "5/2=", 5/2);

        # 실수인 것을 어떻게 알까?
        print("type(5/2)", type(5/2));


        """### 몫 (`//`) 연산자
        * 정수끼리 나눗셈 결과가 정수로 나오도록 해야할 때 //로 나눗셈을 하면 됨
        * `//`은 버림 나눗셈(floor division)이라고 부르며 나눗셈의 결과에서 소수점 이하는 버림
        """
        print("5/2=",5/2)
        print("5//2=",5//2)
        print("divmod(5, 3) =", divmod(5, 3))


        """* 참고로 실수에 // 연산자를 사용하면 결과는 실수가 나오며 소수점 이하는 버림.
        * 따라서 (연산자 앞뒤 숫자 중 하나라도 실수라면) 결과는 항상 `.0`으로 끝남
        """


        """### 나머지 (`%`) 연산자"""
        # 모듈로(modulo) 연산자
        print("5%2=", 5 % 2)


        """### 거듭제곱 (`**`) 연산자"""
        """### 값을 정수로 만들기
        * 계산 결과가 실수로 나왔을 때 강제로 정수로 만들어야 할 때는 int에 괄호를 붙이고 숫자 또는 계산식을 넣으면 됨
        * 특히 int에 문자열을 넣어도 정수로 만들 수 있음. 단, 정수로 된 문자열이라야 함
        ```
        int(숫자)
        int(계산식)
        int('문자열')
        ```
        """
        # int는 정수(integer)를 뜻하며 값을 정수로 만들어 줌 (소수점 이하는 버림)
        """### 몫과 나머지 함께 구하기"""
        """## 실수 계산
        ### 실수끼리의 계산
        """
        # 실수끼리의 덧셈

        # 실수끼리의 뺄셈

        # 실수끼리의 곱셈

        # 실수끼리의 나눗셈


        """### 실수와 정수 간의 계산
        * 실수와 정수를 함께 계산하면 표현 범위가 넓은 실수로 계산됨 (실수가 정수보다 표현 범위가 넓음)
        """
        """### 값을 실수로 만들기
        * `float`에 괄호를 붙이고 숫자 또는 계산식을 넣으면 됨
        * 특히 `float`에 문자열을 넣어도 실수로 만들 수 있음
        * 단, 실수 또는 정수로 된 문자열이라야 함
        ```
        float(숫자)
        float(계산식)
        float('문자열')
        ```
        """
        """* `float`는 부동소수점(**float**ing point)에서 따왔으며 값을 실수로 만들어줌
        * 즉, 실수는 `float` 자료형
        """
        """## 괄호 사용하기"""
        """* 만약 곱셈보다 덧셈을 먼저 계산하고 싶다면 덧셈 부분을 괄호로 묶어주면 됨"""
        # 변수와 입력
        ## 변수 만들기
        """* `x = 10`이라고 입력하면 10이 들어있는 변수 x가 만들어짐
        * 즉, 변수이름 = 값 형식. 이렇게 하면 변수가 생성되는 동시에 값이 할당(저장)
        * 변수 이름은 원하는 대로 지으면 되지만 다음과 같은 규칙을 지켜야 함
        > 영문 문자와 숫자를 사용할 수 있음<br>
        > 대소문자를 구분함<br>
        > 문자부터 시작해야 하며 숫자부터 시작하면 안 됨<br>
        > _(밑줄 문자)로 시작할 수 있음<br>
        > 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없음<br>
        > 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없음
        """
        """* 변수에는 숫자뿐만 아니라 문자열도 넣을 수 있음"""
        """### 변수의 자료형 알아내기
        * type(변수)
        """
        """* x에는 정수 10이 들어있으므로 int, y에는 문자열 Hello, world!가 들어있으므로 str이라고 나옴
        * int는 정수(**int**eger), str은 문자열(**str**ing)에서 따옴
        * 즉, 변수의 자료형은 변수에 들어가는 값에 따라 달라짐
        ### 할당 연산자 `=`
        * 수학에서는 =(등호) 기호는 양 변이 같다는 뜻
        * 하지만 프로그래밍 언어에서 =는 변수에 값을 할당(assignment)한다는 의미
        * 수학의 등호와 같은 역할을 하는 연산자는 `==`(동등연산자)
        ### 변수 여러 개를 한 번에 만들기
        """
        """* 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3 형식으로 변수를 ,(콤마)로 구분한 뒤 각 변수에 할당될 값을 지정해주면 됨
        * 변수와 값의 개수는 동일하게 맞춰주어야 하며 나열된 순서대로 값이 할당
        * 만약 변수와 값의 개수가 맞지 않으면 에러가 발생
        """
        # 변수 여러 개를 만들 때 값이 모두 같아도 된다면?
        # 두 변수의 값을 바꾸려면?
        # 빈 변수 만들기
        """* 파이썬에서 None은 아무것도 없는 상태를 나타내는 자료형
        * 보통 다른 언어에서는 널(null)이라고 표현
        ## 변수로 계산하기
        """
        """* 변수 a, b에 숫자를 할당한 뒤에 a와 b의 값을 더해서 변수 c에 할당
        * 변수는 변수끼리 계산할 수 있고, 계산 결과를 다른 변수에 할당할 수 있음
        ### 산술 연산 후 할당 연산자 사용
        """
        """* 변수 한 개에서 값의 변화를 계속 유지하려면 계산 결과를 다시 변수에 저장해야 함"""
        """* 파이썬에서는 변수를 두 번 입력하지 않도록 산술 연산 후 할당 연산자를 제공"""
        """* a에는 10이 들어있고 a += 20을 수행하면 a에는 10과 20을 더한 결과인 30이 들어감
        * +=처럼 산술 연산자 앞에 =(할당 연산자)를 붙이면 연산 결과를 변수에 저장(+ =처럼 두 연산자를 공백으로 띄우면 안 됩니다)
        * 즉, a += 20은 a = a + 20을 축약한 형태
        ---
        * 덧셈(+=) 외에도 뺄셈(-=), 곱셈(\*=), 나눗셈(/=, //=), 나머지(%=)도 같은 방식
        * 똑같이 연산(-, *, /, //) 후 할당(=) 한다는 뜻입
        ---
        * 만들지 않은 변수 d에 10을 더한 후 다시 할당하면 에러가 발생
        """
        """### 부호 붙이기
        * 값이나 변수 앞에 양수, 음수 부호를 붙이면 됨
        """
        """## 입력 값을 변수에 저장하기
        ### input 함수 사용하기
        """
        """* 입력한 문자열이 그대로 출력
        * 즉, `input` 함수는 사용자가 입력한 값을 가져오는 함수
        ### input 함수의 결과를 변수에 할당
        * `변수 = input()`
        """
        """* 실행을 해보면 '문자열을 입력하세요: '처럼 안내 문구가 먼저 나옴
        * 여기에 문자열을 입력한 뒤 엔터 키를 누르면 입력한 그대로 출력
        * 즉, 이 문자열은 사용자에게 입력받는 값의 용도를 미리 알려줄 때 사용
        * 다른 말로는 프롬프트(prompt)라고도 부름
        ### 두 숫자의 합 구하기
        """
        """## 입력 값을 변수 두 개에 저장하기
        * input 한 번에 값을 여러 개 입력받으려면 input에서 split을 사용한 변수 여러 개에 저장(각 변수는 콤마로 구분)
        ```
        변수1, 변수2 = input().split()
        변수1, 변수2 = input().split('기준문자열')
        변수1, 변수2 = input('문자열').split()
        변수1, 변수2 = input('문자열').split('기준문자열')
        ```
        """
        """* input에 split을 사용하면 입력받은 값을 공백을 기준으로 분리하여 변수에 차례대로 저장(split은 분리하다, 나누다라는 뜻)
        * 문자열 'Hello Python'을 공백을 기준으로 분리하여 'Hello'는 첫 번째 변수 a에 'Python'은 두 번째 변수 b에 저장
        ### 두 숫자의 합 구하기
        """

        """### map을 사용하여 정수로 변환
        * map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환(실수로 변환할 때는 int 대신 float를 넣음)
        ```
        변수1, 변수2 = map(int, input().split())
        변수1, 변수2 = map(int, input().split('기준문자열'))
        변수1, 변수2 = map(int, input('문자열').split())
        변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
        ```
        """
        A, B = map(int, input().split());

        """### 입력받은 값을 콤마를 기준으로 분리"""
        """* split(',')과 같이 분리할 기준 문자열을 콤마로 지정하였으므로 '10,20'에서 10은 a, 20은 b에 저장
        # 출력
        ## 값을 여러 개 출력하기
        * `print`에는 변수나 값 여러 개를 ,(콤마)로 구분하여 넣을 수 있음
        ```
        print(값1, 값2, 값3)
        print(변수1, 변수2, 변수3)
        ```
        """
        """* print에 변수나 값을 콤마로 구분해서 넣으면 각 값이 공백으로 띄워져서 한 줄로 출력 (값을 여러 개 출력할 때 print 함수를 여러 번 쓰지 않아도 됨)
        ### sep로 값 사이에 문자 넣기
        * 값 사이에 공백이 아닌 다른 문자를 넣고 싶을  때는 print의 sep에 문자 또는 문자열을 지정(sep는 구분자라는 뜻의 **sep**arator에서 따옴)
        ```
        print(값1, 값2, sep='문자 또는 문자열')
        print(변수1, 변수2, sep='문자 또는 문자열')
        ```
        """
        """* sep=', '처럼 콤마와 공백을 넣어주면 1, 2, 3과 같은 형태로 출력 (공백 없이 콤마만 지정해도 됨)
        * 또한, sep=''처럼 빈 문자열을 지정하면 각각의 값은 서로 붙어서 출력됨
        * 특히 sep에는 'x'와 같은 일반적인 문자도 넣을 수 있음
        ## 줄바꿈 활용하기
        """
        # print에 값을 여러 개 지정하면 한 줄에 모든 값이 출력
        # print의 sep에 개행 문자(\n)라는 특별한 문자를 지정하면 값을 한 줄에 하나씩 출력
        """### end 사용하기
        * print는 기본적으로 출력하는 값 끝에 \n을 붙임. 그래서 print를 여러 번 사용하면 값이 여러 줄에 출력
        """
        """* print를 여러 번 사용해서 print(1, 2, 3)처럼 한 줄에 여러 개의 값을 출력하려면 print의 end에 빈 문자열을 지정해주면 됨
        ```
        print(값, end='문자 또는 문자열')
        print(변수, end='문자 또는 문자열')
        ```
        """
        """* end는 현재 print가 끝난 뒤 그 다음에 오는 print 함수에 영향을 줌"""
        """## 숫자를 콤마로 구분해서 표현하기"""

    def Python_Basic_01(self):
        # 불(Bool)과 비교, 논리 연산자
        ## 불과 비교 연산자 사용하기
        '''
        * 프로그래밍 -> 참, 거짓 판단 -> 참(True) : 어떠한 조건이나 수식을 만족시키는가? / 거짓(False) : 만족시키지 못한다
        * 불(Bool) 혹은 불리언(Boolean) : 참과 거짓으로 구성된 자료형. <- 조건이나 수식들이 존재하게 됨.
        * 두 값의 관계를 판단하는 비교 연산자 / 두 값의 논리적 관계를 판단하는 논리 연산자
        * if, while.. 구문을 작성.
        '''
        print(True, False)  # 다른 언어들은 대개 true, false
        print(int(True), int(False))  # 1, 0

        # 비교 연산자 - 판단 결과
        ## 등호(같다, 다르다)와 부등호(크다, 작다). -> 비교하는 식이 맞으면 True 아니면 False
        print('10 > 5', '10이 5보다 크다, 10은 5를 초과한다', 10 > 5)  # 초과
        print('10 < 5', '10이 5보다 작다, 10은 5의 미만이다', 10 < 5)  # 미만

        ## 숫자가 같은지 다른지 비교
        '''
        * 일반적 수학에서는 =(등호)로 쓰는데, 파이썬 등 프로그래밍에서는 ==을 등호(동등 연산자, equal)로 쓴다
        * =은 파이썬 뭐에요? -> 대입 연산자 -> 특정한 변수에 값을 할당해주는 연산자
        * 다를 때 !=(not equal)을 사용
        '''
        print("1 == 1 :", 1 == 1)
        print("2 == 1 :", 2 == 1)
        print("1 != 1 :", 1 != 1)

        ## 문자열 동등 여부 비교 (only)
        print("'python' == 'python'", "python" == "python")  # java == X. equals -> 주소값을 비교하니까.
        print("'Python' == 'python'", "Python" == "python")  # 대소문자가 다르면 다른 문자!!!!
        print("'Python' != 'python'", "Python" != "python")  # 대소문자가 다르면 다른 문자!!!!

        # 숫자 비교 : 부등호
        print("10 > 20", 10 > 20)  # 초과 (왼쪽 값 기준으로 생각)
        print("10 < 20", 10 < 20)  # 미만
        print("10 >= 20", 10 >= 20)  # 이상
        print("10 <= 20", 10 <= 20)  # 이하

        # 객체가 같은지 다른지 비교하기
        '''
        * is, is not -> 연산자. ==, !=. 왜 is(~이다), is not(~는 ~가 아니다)?
        * ==, != : 값 자체를 비교한다
        * is, is not -> 객체를 비교한다, 객체 주소를 비교한다(타입) 
        '''
        # 정수 1과 실수 1.0은 까다롭게 생각하면 다른 애들.
        print("1 == 1.0 :", 1 == 1.0)  # 1이라고 하는 '값'은 같아요 (상호 변환이 가능) - 같은 숫자형일 경우에는 같다고 침
        print("'1' == 1 :", '1' == 1)  # 문자열과 숫자의 비교이므로 성립 안함
        # a = 1 is 1.0 # 비교 연산의 결과값을 변수에 담을 수 있음
        # print("1 is 1.0 :", a)
        # b = (1 is not 1.0)
        # print("1 is not 1.0 :")
        # print(b)

        # 논리 연산자 사용하기
        ## 논리 연산자는 and, or, not. (연산자가 꼭 특수문자나 기호일 필요는 없음)
        '''
        내가 알고 있던 and는 &? &&? 내가 알고 있던 or은 |? ||? 내가 알고 있는 not은 !인데??
        '''
        ## 그리고(and) 연산 (&)
        have_car = True
        have_money = True
        can_drive = have_car and have_money
        print("have_car", have_car)
        print("have_money", have_money)
        print("can_drive", can_drive)
        print()
        have_car = False
        have_money = True
        can_drive = have_car and have_money  # 하나라도 False면은 다 False 틀린다
        print("have_car", have_car)
        print("have_money", have_money)
        print("can_drive", can_drive)
        print()
        have_car = True
        have_money = False
        can_drive = have_car and have_money  # 하나라도 False면은 다 False / 틀린다
        print("have_car", have_car)
        print("have_money", have_money)
        print("can_drive", can_drive)
        print()
        have_car = False
        have_money = False
        can_drive = have_car and have_money  # 하나라도 False면은 다 False / 틀린다
        print("have_car", have_car)
        print("have_money", have_money)
        print("can_drive", can_drive)

        print("have_car & have_money", have_car & have_money)
        # print("have_car && have_money", have_car && have_money) # 문법 오류

        # or (또는) / a or b : or로 묶인 것들 중에 하나가 True라면 결과값 True (a | b)
        hungry = True
        study = True
        eat_lunch = hungry or study
        print("hungry?", hungry)
        print("study?", study)
        print("eat_lunch?", eat_lunch)
        print()
        hungry = False
        study = True
        eat_lunch = hungry or study
        print("hungry?", hungry)
        print("study?", study)
        print("eat_lunch?", eat_lunch)
        print()
        hungry = True
        study = False
        eat_lunch = hungry or study
        print("hungry?", hungry)  # <-> 배부르다
        print("study?", study)
        print("eat_lunch?", eat_lunch)
        print()
        hungry = False
        study = False
        eat_lunch = hungry or study  # 여기서 계산이 끝남
        print("hungry?", hungry)
        print("study?", study)
        print("eat_lunch?", eat_lunch)  # 하나라도 True라면 결과가 True -> OR
        print()
        print("hungry | study", hungry | study)

        # not (논리값 -> bool) True -> False / False -> True
        sleepy = True
        print("sleepy", sleepy)
        print("not sleepy", not sleepy)  # 안 졸리다, 깨어있다~
        boring = False
        print("boring", boring)
        print("not boring", not boring)
        # print("not boring", !boring) -> ! 연산자 없음...

        # and, or, not -> not (1), and (2), or (3) <- 우선순위 외우면 좋음.

        print("not True and False or not False", not True and False or not False)
        print("(not True) and False or (not False)", False and False or True)
        print("((not True) and False) or (not False)", False or True)
        # 논리 연산도 ()를 통해서 강제로 우선순위를 정해줄 수 있음.
        # 논리 연산을 복잡하게 하는 것에 익숙하지 않다 / 못하겠다
        # 1. 괄호 사용하기 2. 변수로 끊어서 연산하기

        # 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저임)
        # 비교 연산자를 통해서 값을 비교하고 이것을 통해 True 또는 False 결과값(Bool 값이 나옴)
        # 그 후에 논리 연산자가 그것을 받아서 처리함
        # 산술 -> 비교 -> 논리 연산자 순. (그래도 괄호와 변수로 표현된 건 먼저 처리가 된 상태임)
        print("10 == 10 and 10 != 5 :", 10 == 10 and 10 != 5)
        print("(10 == 10) and (10 != 5) :", True and True)  # True.
        print("10 > 5 or 10 < 3", 10 > 5 or 10 < 3)  # True
        print("5 + 5 > 8 and 3 - 2 < 0", 5 + 5 > 8 and 3 - 2 < 0)
        print("(5 + 5) > 8 and (3 - 2) < 0", 5 + 5 > 8 and 3 - 2 < 0)
        print("not 10 > 5", not 10 > 5)
        print("not 7 + 3 > 5", not 7 + 3 > 5)

        # 정수, 실수, 문자열을 불(참,거짓)으로 만들기 / 판별
        '''
        정수, 실수, 문자열 -> 불(bool) => bool(1)
        '''
        print("bool(1)", bool(1))
        print("bool(0)", bool(0))
        print("bool(-1)", bool(-1))  # 정수, 실수나 => 숫자에서는 True/False 기준은 0이면 False. 0이 아니면 True
        print("bool(0.1)", bool(0.1))
        # number -> bool ???? number != 0

        # 문자열
        print("bool('아무거나')", bool("아무거나"))  # True
        print("bool('abadfafa')", bool("abadfafa"))  # True
        print("bool('')", bool(""))  # False => 큰따옴표 혹은 작은따옴표로 감싸진 것만 있을 때
        # string -> bool ???? len(string) > 0 # length(길이)

    def Python_Basic_02(self):
        # 문자열
        text = "Hell study"
        print(text);

        # 한글 문자열
        kor_text = "살려줘"
        print(kor_text);

        # 작은 따음표를 이용한 문자열
        single_text = 'Heel'
        print(single_text);

        # 큰 따음표를 이용한 문자열
        double_text = "hell"
        print(double_text);

        # 작은 따음표 '''
        sigle_multi_text = '''
            나보기가 역겨워 가실 때에는
            말 없이 고이 보네 드리오리다.
        '''
        print(sigle_multi_text)

        # 큰 따음표 """
        double_multi_text = """
            동해 물과 백두산이 마르고 닳도록
            하느님이 보우하사 우리나라 만세
        """
        print(double_multi_text)

        # 선언문이 없을 때의 '''는 주석처럼 사용이 가능하다.

    def Python_Basic_03(self):
        # 리스트와 튜플
        ## 리스트 : 1개 이상의 연속된 값들의 묶음
        '''
        지금까지 배운 변수와 다른 값들 -> 값을 한 개씩 다뤘음
        '''
        a = 10
        b = 20
        print(a, b)

        # 30개의 숫자를 저장 (1~30)
        '''
        a1 = 1
        a2 = 2
        ...
        a30 = 30
        '''

        # 리스트(List) : 목록 -> 값을 일렬로 (순서가 있게) 늘어놓은 형태

        # 리스트 만들기
        '''
        * 변수에 값을 저장할 때 [ ](대괄호)로 묶어주면 리스트가 됨. 각 값은 ,(콤마)로 구분
        * 리스트 = [값1, 값2, ...]
        '''
        fruits = ["사과", "배", "귤"]
        print(fruits)
        numbers = [10, 40, 27]
        print(numbers)

        # 리스트에 여러 가지 자료형 저장
        teacher = ["김강사", 180, 70.9, True]  # 리스트-나열 -> 다 같은 타입이 되도록 제한.
        print(teacher)  # 파이썬에서의 리스트는 여러 가지 자료형(타입)들을 편하게 넣을 수 있음.

        # 빈 리스트 만들기
        '''
        * 빈 리스트를 만들 때는 [ ] 만 사용하거나, list()를 사용하면 됨.
        * 리스트 = []
        * 리스트 = list()
        '''
        a = []
        print("a :", a)
        b = list()
        print("b :", b)

        # range를 사용하여 리스트 만들기
        '''
        range는 연속된 숫자를 생성하는 기능
        range(10) # 시작은 0부터 하고, 끝은 입력한 값 직전. (10->9)
        0 ~ 9까지의 수의 나열
        '''
        print(range(10))  # range(n) : 0부터 n 직전까지의 숫자를 생성
        # range(0, 10) <- 앞으로 사용 예정일 range로 대기 상태.
        print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 수를 나열한 리스트를 만들 때
        # 리스트 = list(range(횟수)) : 횟수 -> 횟수 - 1의 값까지 숫자를 만들겠다 (0부터 시작해서)

        # 시작점과 끝점이 모두 있는 range
        r = range(8, 14)  # range(시작점, 끝점) : 시작점으로부터 시작하고, 끝점-1까지 반복되는 정수들의 집합
        print(r)
        print(list(r))  # 8~13까지 연속되는 정수의 리스트를 가지고 싶다?? range(8, 13+1=14) => range(8, 14) => list(...)
        # 시작점(포함), 끝점(포함X)

        # 시작점, 끝점, 증가폭 range
        r2 = range(100, 1000, 100)  # list(range(시작, 끝, 증가폭)) => 증가폭만큼 늘어나면서 숫자 리스트를 생성
        print(r2)
        print(list(r2))  # [100, 200, 300, 400, 500, 600, 700, 800, 900]
        print(list(range(100, 950, 100)))  # 끝점을 초과하면 멈추는 개념.

        r3 = range(1000, 100, -100)  # 증가폭은 음수를 쓸 수 있다
        print(list(r3))
        r4 = range(1000, 99, -100)  # 증가폭은 음수를 쓸 수 있다
        print(list(r4))
        r5 = range(10, 0, 1)  # 10 -> 시작점에서 검사를 해보니까 끝점을 추월해버림.
        print(list(r5))  # []

        # 튜플 (tuple)
        '''
        * 리스트처럼 요소(원소, element)들이 있다
        * 튜플은 요소를 수정할 수 없음. 읽기 전용 (read-only)
        * 리스트가 []라면, 튜플은 ()입니다. -> 각 값은 ,(콤마, 쉼표)로 구분.
        * 변수 한 개에 => 여러 값을 (괄호 없이) ,로 구분해서 넣으면 => 역시나 튜플
        * 튜플 = (값1, 값2, 값3..)
        * 튜플 = 값1, 값2, 값3...
        '''
        # 숫자가 5개 들어있는 튜플
        a1 = (23, 38, 12, 11, 7)
        print("a1 :", a1)
        a2 = 23, 38, 12, 11, 7
        print("a2 :", a2)
        a3 = "python", 123, 123.45, True
        print("a3 :", a3)  # 튜플도 리스트처럼 자료형의 혼합이 가능하다

        # range를 사용해서 튜플 만들기
        # list(...) => range => list
        # tuple(...) => range => tuple
        print(tuple(range(1, 100)))
        # tuple(range(끝점))
        # tuple(range(시작점, 끝점))
        # tuple(range(시작점, 끝점, 증가폭))

        # tuple을 list로 변환하고, list를 tuple로 변환하고 싶으면?
        a = list(range(10))  # [0.... 9]
        print(a)
        b = tuple(a)
        print(b)  # (0....9)
        c = tuple(range(5, 25, 5))
        print(c)
        d = list(c)
        print(d)

        # 리스트와 튜플로 변수 만들기
        '''
        * 리스트 또는 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있음
        * 이 때 (만들려는) 변수의 개수와 리스트(튜플)의 요소 개수는 같아야 함
        '''
        l = [1, 2, 3]
        a, b, c = l
        print("a:", a, "b:", b, "c:", c)
        t = ("dog", "cat", "cow", "bird")
        d, e, f, g = t
        print("d:", d, "e:", e, "f:", f, "g:", g)
        d, e, f, g = ("dog", "cat", "cow", "bird")  # d, e, f, g = t
        d, e, f, g = "dog", "cat", "cow", "bird"  # d, e, f, g = t
        # 파이썬에서는 왼쪽 변수의 수와 오른쪽 값의 수가 맞으면 한 번에 변수에 값을 대입해줄 수 있다
        # unpacking -> tuple unpacking

        a, b, c = [1, 2, 3]  # 리스트를 분해해서 각각의 변수에 집어넣는것? : 리스트 언팩킹.

        v = 10, 100, 1000  # 튜플 -> 묶어서 넣는 것 -> pack -> packing -> 튜플 패킹
        l = [10, 100, 1000]  # 리스트 패킹


