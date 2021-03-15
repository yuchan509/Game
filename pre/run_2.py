# TODO step0
# 환경 변수, 임계값, 실험값 -> 상수로 표기
# 이런 환경을 컨트롤하는 값들은 외부에서 조절할수 있게 설정(일반적)
ENV_TITLE_MAX_LEN = 20
ENV_PNAME_MAX_LEN = 15

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
msg = f"게임 제목을 입력하세요, 단 {ENV_TITLE_MAX_LEN}자 이내로 입력 가능합니다."
# 게임 제목을 20자 이내로 넣을때만 반복문을 빠져나가고, 
# 조건을 부합하지 못하면 그전에 체크 당해서 continue로 인해 다시 
# 반복문 조건 체크 입력대기로 이동하게 된다
while True:
    # 함수나 클레스 내부에서 만든 변수가 아닌 이상은 
    # 하나의 파이썬 내부에서는 전역변수로 자유롭게 사용이 가능함 
    gameTitle = input(msg).strip()
    if not gameTitle:
      print("정확하게 입력하세요")
      continue      
    elif len(gameTitle) > ENV_TITLE_MAX_LEN:
      print(str(ENV_TITLE_MAX_LEN) + "자가 초과되었습니다.")
      continue
    break

print( '게임 제목은', gameTitle )

# TODO step3
'''
- 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
- 입력에 대한 체크 포인트는 Step2와 동일하다
- 플레이어에 대한 닉네임은 player_name이라는 변수에 보관한다
'''
msg         = "플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다" % ENV_PNAME_MAX_LEN
player_name = None
while True:
  # 사용자가 입력에 대한 습관으로 공백을 본인도 모르게 입력하는 경우가 있다
  # => 개발자 입장에서는 공백을 처리해 줘야 한다 => 공백제거
  tmp         = input(msg).strip()
  if not tmp:# 입력값이 없다
    print('정확하게 입력하세요')
    pass
  elif len(tmp) > ENV_PNAME_MAX_LEN:# 15자가 넘었다
    print( '닉네임은 {}자 이내로 입력하세요'.format(ENV_PNAME_MAX_LEN) )
    pass
  else:# 정상입력
    player_name = tmp
    break
    pass  

print('플레이어의 닉네임', player_name)


# TODO step4



# TODO step5



# TODO step6