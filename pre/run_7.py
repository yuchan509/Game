ENV_TITLE_MAX_LEN = 20
ENV_PNAME_MAX_LEN = 15
VERSION           = 'v 1.0'

# 본 s/w의 엔트리 포인트(시작점)
# 함수내의 변수들은 지역변수가 된다 -> 이것을 대한 데이터 처리부분이 고려할 부분.
def main():
  game_step1()
  game_step2()
  game_step3()
  game_step4()
  while True:
    game_step5()
    game_step6()
  pass

# TODO STEP1
def game_step1():
  pass

# TODO STEP2
def game_step2():
  pass

# TODO STEP3
def game_step3():
  pass

# TODO STEP4
def game_step4():
  pass

# TODO STEP5
def game_step5():
  pass

# TODO STEP6
def game_step6():
  pass

if 0:
  game_start_prompt = 'Enjoy Custom Game World'
  print( game_start_prompt )
  
  gameTitle = "Match Number Game"
  if not gameTitle:
    msg = f"게임 제목을 입력하세요, 단 {ENV_TITLE_MAX_LEN}자 이내로 입력 가능합니다."
    while True:
        gameTitle = input(msg).strip()
        if not gameTitle:
          print("정확하게 입력하세요")
          continue      
        if len(gameTitle) > ENV_TITLE_MAX_LEN:
          print(str(ENV_TITLE_MAX_LEN) + "자가 초과되었습니다.")
          continue
        break

    print( '게임 제목은', gameTitle )
  
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
  
  p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN
  print( '-'*p_max_len )
  print( f'-{gameTitle:^25}-' )
  print( f'-{VERSION:^25}-' )
  print( f'-{("welcome " + player_name):^25}-' )
  print( '-'*p_max_len )
  print( '\n게임이 시작됩니다. AI가 숫자를 준비합니다.\n' )
  
  msg          = "1<= x <=100 에서 값을 하나 선택하세요"
  play_game    = True
  while play_game:
    tryCnt       = 0
    import random
    ai_number    = random.randint(1, 100)
    # print( f'ai_number : {ai_number}')
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
      if ai_number > guest_number:# 작다
        print('작다')
        pass
      elif ai_number < guest_number:# 크다
        print('크다')
        pass
      else:
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
            play_game = False
            break
            pass
          else:
            print('정확하게 입력하세요')
            pass
  
  print( 'good bye~!!' )

# 이 프로그램을 내가 호출하면( __name__ => "__main__") 작동, 
# 남이 호출하면( __name__ => "파일이름")(모듈 가져오기(import)) 작동않한다
if __name__ == "__main__":
  main()