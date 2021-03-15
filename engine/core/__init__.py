from engine import ENV_TITLE_MAX_LEN, ENV_PNAME_MAX_LEN, VERSION
PI = 3.14

# TODO 함수지향적 프로그램 STEP1
def game_step1():
    print('game_step1 call') 
    game_start_prompt = 'Enjoy Custom Game World'
    print( game_start_prompt )
    pass

# TODO 함수지향적 프로그램 STEP2
def game_step2():
    print('game_step2 call') 
    gameTitle = None    
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
    # 함수 내부에서 세팅된 게임 제목은 다른 함수에서 사용하므로
    # 리턴해줘야 한다(함수 밖으로 빼야 한다)
    return gameTitle


# TODO STEP3
def game_step3():
    player_name = None
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
    return player_name

# TODO STEP4
def game_step4( gameTitle, player_name ):
    p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN
    print( '-'*p_max_len )
    print( f'-{gameTitle:^25}-' )
    print( f'-{VERSION:^25}-' )
    print( f'-{("welcome " + player_name):^25}-' )
    print( '-'*p_max_len )
    print( '\n게임이 시작됩니다. AI가 숫자를 준비합니다.\n' )
    pass

# TODO STEP5
def game_step5( msg ):
    guest_number = None
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
    return guest_number

# TODO STEP6
def game_step6( tryCnt, ai_number, guest_number  ):
    isSuccess = False
    play_game = True
    if ai_number > guest_number:# 작다
        print('작다')
    elif ai_number < guest_number:# 크다
        print('크다')
    else:
        isSuccess = True

    if isSuccess: 
        point = 0 if tryCnt > 10 else (10 - tryCnt)*10
        print(f'총 {tryCnt}회 시도 해서 {point}점을 획득하였습니다. 다시하시겠습니까?')
        while True:
            choice = input( 'yes:다시 게임시작, no:게임 종료' ).strip().lower()
            if choice == 'yes' or choice == 'y':
                break
            elif choice == 'no' or choice == 'n':
                play_game = False
                break
            else:
                print('정확하게 입력하세요')
        
    return isSuccess,play_game