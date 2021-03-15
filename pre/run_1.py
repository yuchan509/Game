# TODO step1
# 게임이 시작하면 Enjoy Custom Game World"라는 문구를 출력한다.
game_start_prompt = 'Enjoy Custom Game World'
print( game_start_prompt )


# TODO step2
'''
- "게임 제목을 입력하세요, 단 20자 이내로 입력 가능합니다." 
 라는 문구를 출력한다.

- 플레이어가 입력할때까지 무제한으로 대기한다
- 아무것도 입력하지 않고 엔터를 치면(조건1) "정확하게 입력하세요" 라고 출력하고 
  다시 입력 대기한다.

- 20자 이상 입력하고 엔터를 치면(조건2), "20자가 초과되었습니다." 라고 출력하고,
  다시 입력 대기한다.

- 20자 이내로 입력하고 엔터를 치면(조건3) gameTitle이라는 변수에 게임 제목을
  담고 다음 단계로 이동한다 -> 반복문을 빠져나간다.
'''

msg = "게임 제목을 입력하세요, 단 20자 이내로 입력 가능합니다."
while True:
    # 입력대기, 프로그램은 순차적으로 진행되다가 여기서 블락되어 있다
    gameTitle = input(msg)
    #print( type(gameTitle), f'[{gameTitle}]', len(gameTitle) )
    #break
    # 입력값 체킹
    #if len(gameTitle) == 0:
    if not gameTitle:   # 아무것도 입력하지 않고 엔터를 치면(조건1) "정확하게 입력하세요" 라고 출력하고 다시 입력 대기한다
        pass
    elif len(gameTitle) > 20:  # 20자 이상(>) 입력하고 엔터를 치면(조건2), "20자가 초과되었습니다." 라고 출력하고, 다시 입력 대기한다.
        pass
    else:        # 20자 이내로 입력하고 엔터를 치면(조건3) gameTitle이라는 변수에 게임 제목을 담고 다음 단계로 이동한다 -> 반복문을 빠져나간다
        # 이 반복문을 빠져나갈 근거가 마련되었다
        break
        pass





# TODO step3



# TODO step4



# TODO step5



# TODO step6