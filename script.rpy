# Define the character images and UI elements
image character = "character.png"
image bgmain = "bgmain.png"
image basic = "basic.png"
image characterbox = "characterbox.png"
image saying = "saying.png"
image background = "background.png"
image neine = "neine.png"
image aliennews = "aliennews.png"
image news_comment = "news_comments.png"
image search_one = "search_one.png"

define n = Character(color = "#FFFFFF")

init:
    $ moonsaying = ""
    $ presaying = ""

screen mainsaying:
    text "[moonsaying]" xpos 950 ypos 370 size 18

screen sayinglog:
    text "[presaying]" xpos 100 ypos 570 size 22

# Start the game
label start:
    jump tutorial
    return

label tutorial:
    scene bgmain
    show basic:
        xpos 55
        ypos 30
    show characterbox:
        xpos 870
        ypos 30
    show character:
        xpos 970
        ypos 50
    show saying:
        xpos 930
        ypos 330
    show screen sayinglog
    show screen mainsaying
    n "당신은 어두운 방에서 눈을 떴습니다."
    n "침대 옆의 열린 창문으로 적당히 시원한 공기와 함께 푸른 밤하늘이 눈에 들어옵니다. "
    n "눈 앞에는 잡동사니가 잔뜩 쌓인 책상과 은은하게 푸른 빛을 내는 컴퓨터 화면이 보입니다. "
    n "커맨드를 입력하여 컴퓨터 앞으로 가보세요."
    n "커맨드는 명사 + 동사로 이루어져 있습니다."
    n "여러 번의 명령을 해도 좋으니 최대한 간결한 문장을 사용하세요."
    python :
        while(True):
            input = renpy.input(">> ")
            if "컴퓨터" in input and ("가다" in input or "간다" in input or "이동" in input or "움직" in input):
                moonsaying = "배가 고프군"
                break
            else:
                moonsaying = "그렇게는 못해"
    n "당신의 움직임에 잡동사니 더미 안의 마우스가 흔들린 듯 화면에 불이 켜집니다."
    $ moonsaying = "어린 시절 나를 갑자기 \n떠난 그 친구가 생각나네"
    n "하루를 시작할 시간입니다!"
    $ moonsaying = "그때의 충격으로 나는 \n방 안에 틀어박히고 말았지"
    n "당신은 하루의 모든 시간을 방 안에서 보냅니다."
    $ moonsaying = "그 친구는 어디로 갔을까?"
    n "어느새 당신의 작은 방은 세상의 전부가 되어버린 지 오래고, 당신은 이 일과에 익숙해진지 오래입니다."
    $ moonsaying = "일단 밥부터 먹자"
    n "하루를 시작하기 위해서는 위장을 든든히 채워 둬야겠죠. 뇌도 깨울 겸, 피자 가게에 전화를 걸어 피자를 시켜봅시다."
    python :
        while(True):
            input = renpy.input(">> ")
            if "피자" in input and "전화" in input:
                moonsaying = "포톤피자죠?"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    n "\"네, 포톤피자입니다. 무엇을 도와드릴까요?\""
    $ presaying = "\"네, 포톤피자입니다. 무엇을 도와드릴까요?\""
    python :
        while(True):
            input = renpy.input("\n>> ")
            if "주문" in input and "피자" in input:
                moonsaying = "파인애플 피자가 좋겠어"
                presaying = ""
                break
            else:
                moonsaying = "그렇게는 못해"
    n "\"아…항상 시키시는 그분이시군요. 주소는 이미 알고 있으니 말씀하지 않으셔도 됩니다.\n광자보다 빠르게 보내드리겠습니다, 감사합니다!\""
    n "피자를 기다리며 당신은 컴퓨터 앞에 앉아 하루의 일과를 시작합니다."
    $ mainsaying = ""
    jump news
    return

label news:
    $ moonsaying = "심심한데"
    # 컴퓨터 화면 추가
    hide basic
    show background:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if "인터넷" in input:
                moonsaying = "뉴스라도 볼까"
                break
            elif ("전원" in input or "컴퓨터" in input) and ("끄" in input or "끈" in input or "꺼" in input):
                moonsaying = "난 심심하다고"
            elif "직박구리" in input:
                moonsaying = "지금은 별로 안땡기는데"
            elif "디스코드" in input or "디코" in input:
                moonsaying = "아무런 연락이 없어"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    # 기사 종류 선택 화면 추가
    hide basic
    show neine:
        xpos 55
        ypos 30
    python:
        input = renpy.input(">> ")
        while(True):
            if("외계인" in input or "우주" in input or "현풍" in input):
                moonsaying = "외계인? 흥미롭군"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "손이 미끄러졌다!"
                break
    n "당신은 외계인 뉴스를 읽기 시작합니다."
    # 뉴스 화면 추가
    hide neine
    show aliennews:
        xpos 55
        ypos 30

    python:
        while(True):
            input = renpy.input(">> ")
            if "댓글" in input and ("보" in input or "본" in input):
                moonsaying = "댓글도 볼까"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    # 댓글 화면 추가
    hide aliennews
    show news_comment:
        xpos 55
        ypos 30
    $ moonsaying = "이상한 사람이 있네"
    n "당신은 외계인 뉴스의 댓글을 읽기 시작합니다."
    python:
        while(True):
            input = renpy.input(">> ")
            if "canyouhearmefellas" in input and "검색" in input:
                moonsaying = "이 사람은 누구지?"
                break
            elif ("TMTTM" in input or "Kim_3458" in input) and "검색" in input:
                moonsaying = "별 내용이 없네"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    # 검색 화면 추가
    hide news_comment
    show search_one:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if "끝" in input or "홈" in input or "돌아" in input or "바탕화면" in input:
                moonsaying = "그 사람은 뭐였지?"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    return
