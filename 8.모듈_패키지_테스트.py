# 이 파일은 모듈/패키지에대한 테스트 파일
'''
1.
모듈/패키지 만들기
    - 모듈 : *.py
    - 패키지 : 디렉토리
        - 패키지 밑에는 __init__.py를 통상 생성한다
        - 해당 파일은 하위 호환때문에 생성(python 3.3이하는 필수)
        - 2.7과의 호환이다.
        - 의미 패키지 자체를 대변하는 모듈
2.
모듈/패키지 가져와서 내 코드에서 사용하는 모든표현
'''
# 모듈가져오기
# 경로를 따질때는 반드시 엔트리포인트로부터 계산
# from 패키지.패키지.패키지....모듈 import 변수,함수,클레스,... or *
# from 패키지.패키지.패키지....패키지 import 변수,함수,클레스,... or *
# import 패키지.패키지.....모듈 as 닉네임
# import 패키지.패키지.....패키지 as 닉네임
# import 모듈
# import 패키지
from engine.core.game_core import PI3, add, A
print( PI3 )
add()
A()
# 패키지.패키지 => __init__.py에서 가져온다
from engine.core import PI
print( PI)
# 패키지.모듈
import engine.prompt as pt
print(pt.PI5)
pt.sub()
# 패키지
import engine
print(engine.PI2)
# 모듈
import run
print( run.msg )