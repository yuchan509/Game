# TODO step0
# 환경 변수, 임계값, 실험값 -> 상수로 표기
# 이런 환경을 컨트롤하는 값들은 외부에서 조절할수 있게 설정(일반적)
ENV_TITLE_MAX_LEN = 20
ENV_PNAME_MAX_LEN = 15
VERSION           = 'v 1.0'

# TODO step1
# 게임이 시작하면 Enjoy Custom Game World"라는 문구가 출력된다
game_start_prompt = 'Enjoy Custom Game World'
print( game_start_prompt )

# TODO step2
'''
- "게임 제목을 입력하세요, 단 20자 이내로 입력 가능합니다." 
 라는 문구가 출력된다
- 플레이어가 입력할때까지 무제한으로 대기한다
- 아무것도 입력하지 않고 엔터를 치면(조건1) "정확하게 입력하세요" 라고 출력하고 
  다시 입력 대기한다
- 20자 이상 입력하고 엔터를 치면(조건2), "20자가 초과되었습니다." 라고 출력하고,
  다시 입력 대기한다.
- 20자 이내로 입력하고 엔터를 치면(조건3) gameTitle이라는 변수에 게임 제목을
  담고 다음 단계로 이동한다 -> 반복문을 빠져나간다
'''
gameTitle = "Match Number Game"
if not gameTitle:
  msg = f"게임 제목을 입력하세요, 단 {ENV_TITLE_MAX_LEN}자 이내로 입력 가능합니다."
  while True:
      gameTitle = input(msg).strip()
      if not gameTitle:
        print("정확하게 입력하세요")
        continue      
      #elif len(gameTitle) > ENV_TITLE_MAX_LEN:
      if len(gameTitle) > ENV_TITLE_MAX_LEN:
        print(str(ENV_TITLE_MAX_LEN) + "자가 초과되었습니다.")
        continue
      # 여기에 진입했다는 것은 정상적으로 입력을 완료했다는 뜻
      break

  print( '게임 제목은', gameTitle )

# TODO step3
'''
  - 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
  - 입력에 대한 체크 포인트는 Step2와 동일하다
  - 플레이어에 대한 닉네임은 player_name이라는 변수에 보관한다
'''
player_name = "guest"
msg         = "플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다" % ENV_PNAME_MAX_LEN
while not player_name:
  tmp         = input(msg).strip()
  if not tmp:
    print('정확하게 입력하세요')
    pass
  elif len(tmp) > ENV_PNAME_MAX_LEN:
    print( '닉네임은 {}자 이내로 입력하세요'.format(ENV_PNAME_MAX_LEN) )
    pass
  else:
    player_name = tmp
    break
    pass  

print('플레이어의 닉네임', player_name)


# TODO step4
'''
  ------------------------------
  -         게임 제목          -
  -          v 1.0             -
  -   welcome 플레어이름       - 
  ------------------------------
'''
# 한글이 차지하는 공간과 영문/영소/특수/숫자가 차지하는 공간이 달라서
# 영어 입력만 처리하겠금 일단 조치(가정)
# 프럼프트의 최대 가로길이를 고정적으로 계산해서 탄력적으로 출력한다
# 경계칸수(2) + 양쪽여백(2) + 문자열 사이여백(1) + ... + ...
p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN
print( '-'*p_max_len )
# 게임제목 디스플레이 %10s, {값:10}
#dp = '-{gameTitle:%s}-' % (p_max_len-2)
print( f'-{gameTitle:^25}-' )
print( f'-{VERSION:^25}-' )
print( f'-{("welcome " + player_name):^25}-' )
print( '-'*p_max_len )
# \n : 줄바꿈
print( '\n게임이 시작됩니다. AI가 숫자를 준비합니다.\n' )


# TODO step5
# 5-1. AI가 1~100사이의 임의의 수를 정수로 하나 랜덤하게 생성한다
import random
ai_number    = random.randint(1, 100)
# 5-2 "1<= x <=100 에서 값을 하나 선택하세요"
msg          = "1<= x <=100 에서 값을 하나 선택하세요"
# 5-3 사용자는 1 ~ 100 사이에 값을 입력한다
guest_number = input( msg )


# TODO step6
