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
p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN
print( '-'*p_max_len )
print( f'-{gameTitle:^25}-' )
print( f'-{VERSION:^25}-' )
print( f'-{("welcome " + player_name):^25}-' )
print( '-'*p_max_len )
print( '\n게임이 시작됩니다. AI가 숫자를 준비합니다.\n' )


# TODO step5
# 위치 조정: 전체적으로 1회만 수행되면 된다
msg          = "1<= x <=100 에서 값을 하나 선택하세요"

import random
ai_number    = random.randint(1, 100)
# 사용자가 숫자를 맞출때까지, 무한 반복한다
isSuccess    = False
# 숫자를 맞췄는가? 
while not isSuccess: 
  # 숫자 입력에 대한 무한루프:1~100사이값을 입력받을때까지
  while True: 
    # 숫자 입력을 받았다
    guest_number = input( msg ).strip()
    if not guest_number: # 입력을 않하고 엔터
      print('정확하게 입력하세요')
      continue    
    if not guest_number.isnumeric(): # 숫자가 될수 없는 값을 넣고 엔터
      print('"{0}"는 숫자가 아니거나, 대상이 아닙니다'.format(guest_number))
      continue
    # 0~의 정수가 될수 있는 문자열만 여기도 도착
    # 크기 비교를 하기 위해서 타입을 정수로 변환
    guest_number = int(guest_number)
    #if 조건 or 조건:
    if guest_number < 1 or guest_number > 100:
    #if 1 > guest_number or guest_number > 100:
    #if guest_number < 1 or 100 < guest_number :
      # xx 하고, xx 하면   => and => 한개라도 False면 다 False
      # xx 하거나, xx 하면 => or => 한개라도 True면 다 True
      # 1보다 작거나, 100보다 크거나 하는 값을 넣고 엔터<-전제:입력값의 타입이 수치이다
      print('허용하는 값의 범위를 넘어섰습니다.')
      continue     
    # 정상적인 값을 입력하고 엔터
    break

# TODO step6
