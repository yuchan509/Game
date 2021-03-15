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
# 전체적으로 게임이 계속 진행되는지 구분하는 플래그 변수
# 이 변수는 게임을 그만 하겠다라고 선택하면 그때서야  False
play_game    = True
# 시도횟수 선언및 초기화
while play_game:
  tryCnt       = 0
  import random
  ai_number    = random.randint(1, 100)
  print( f'ai_number : {ai_number}')
  isSuccess    = False
  while not isSuccess: 
    while True: 
      guest_number = input( msg ).strip()
      if not guest_number:
        print('정확하게 입력하세요')
        continue    
      if not guest_number.isnumeric():
        print('"{0}"는 숫자가 아니거나, 대상이 아닙니다'.format(guest_number))
        continue    
      guest_number = int(guest_number)    
      if guest_number < 1 or guest_number > 100:    
        print('허용하는 값의 범위를 넘어섰습니다.')
        continue         
      break
    
    tryCnt += 1
    # TODO step6
    '''
      판정 : 작으면 작다, 크면 크다라고 출력을 하고 다시 입력 대기를 한다
      기준 : AI의 숫자와 플레이어의 입력값을 비교, 
            - AI > PL  => 작다
            - AI < PL  => 크다
            - AI == PL => 같다
    '''
    if ai_number > guest_number:# 작다
      print('작다')
      pass
    elif ai_number < guest_number:# 크다
      print('크다')
      pass
    else:# 같다
      # 정답을 맞췄다
      # 플레그 변수를 수정 => 위치가 어디가 되던 바깥쪽 while문에 영향을 준다
      isSuccess = True
      pass

    if isSuccess: 
      point = 0 if tryCnt > 10 else (10 - tryCnt)*10
      print(f'총 {tryCnt}회 시도 해서 {point}점을 획득하였습니다. 다시하시겠습니까?')
      while True:
        choice = input( 'yes:다시 게임시작, no:게임 종료' ).strip().lower()
        if choice == 'yes' or choice == 'y':
          break
          pass
        elif choice == 'no' or choice == 'n':
          play_game = False # 그만하자
          break
          pass
        else:
          print('정확하게 입력하세요')
          pass


# 게임 종료: good bye~!!->exit()종료
print( 'good bye~!!' )