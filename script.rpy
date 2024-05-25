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
image cafe_before_enroll = "cafe_before_enroll.png"
image cafe_after_enroll = "cafe_after_enroll.png"
image message1 = "message1.png"
image message2 = "message2.png"
image message3 = "message3.png"
image message4 = "message4.png"
image message5 = "message5.png"
image message6 = "message6.png"
image lovechat_background = "lovechat_background.png"
image alien_message_basic = "alien_message_basic.png"
image alien_message_basic2 = "alien_message_basic2.png"
image alien_massage_1_1 = "alien_massage_1.png"
image alien_massage_1_2 = "alien_massage_1-1.png"
image alien_massage_1_3 = "alien_massage_1-2.png"
image alien_massage_1_4 = "alien_massage_1-3.png"
image alien_massage_2_1 = "alien_massage_2-1.png"
image alien_massage_2_2 = "alien_massage_2-2.png"
image alien_massage_2_3 = "alien_massage_2-3.png"
image alien_massage_2_2_angry1 = "alien_massage_2-2-angry1.png"
image alien_message_2_2_angry2 = "alien_message_2-2-angry2.png"
image alien_message_3_1 = "alien_message_3-1.png"
image alien_message_3_2 = "alien_message_3-2.png"
image alien_message_3_3 = "alien_message_3-3.png"
image alien_message_hack_bad1 = "alien_message_1-4.png"
image alien_message_hack_bad2 = "alien_message_1-5badend.png"
image alein_message_oldfriend1 = "alien_message_1-3-2.png"
image alein_message_oldfriend2 = "alien_message_1-3-3-3.png"
image alein_message_oldfriend3 = "alien_message-1-3-3-4.png"
image alein_message_oldfriend4 = "alien_message_1-3-3-5.png"
image alein_message_oldfriend5 = "alien_message_1-3-3-6.png"
image alien_do_not_exist = "alien_do_not_exist.png"
image message_alert = "message_alert.png"
image agent_message1 = "agent1.png"
image agent_message2 = "agent2.png"
image agent_message3 = "agent3.png"
image agent_message4 = "agent4.png"
image agent_message5 = "agent5.png"
image agent_message6 = "agent6.png"

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
    n "브라우저를 열자 뉴스 기사들이 화면을 채웁니다."
    n "시간 때울 겸 하나 읽어봐도 괜찮겠네요. 읽고 싶은 뉴스를 골라봅시다. "
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
    hide search_one
    show neine:
        xpos 55
        ypos 30
    n "기사를 나가자 곧 또다른 화면이 보입니다."
    jump cafe
    return

label cafe:
    hide basic
    show cafe_before_enroll:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if "가입" in input:
                moonsaying = "먼저 카페에 가입하자"
                break
            elif "클릭" in input or "보" in input or "본" in input or "열" in input or "연" or "들어" in input :
                moonsaying = "글을 보기 위해선\n회원가입이 필요해"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide cafe_before_enroll
    show cafe_after_enroll:
        xpos 55
        ypos 30
    n "카페에 가입해니 메세지가 와있습니다."
    hide cafe_after_enroll
    show message1:
        xpos 55
        ypos 30
    $ moonsaying = "누구지?"
    n "아무 키나 클릭하여 진행하세요"
    hide message1
    show message2:
        xpos 55
        ypos 30
    $ moonsaying = "그걸 어떻게..."
    n "아무 키나 클릭하여 진행하세요"
    hide message2
    show message3:
        xpos 55
        ypos 30
    $ moonsaying = "위대한 외계존재?"
    n "아무 키나 클릭하여 진행하세요"
    hide message3
    show message4:
        xpos 55
        ypos 30
    $ moonsaying = "사이빈가?"
    n "아무 키나 클릭하여 진행하세요"
    hide message4
    show message5:
        xpos 55
        ypos 30
    $ moonsaying = "사이트? 통신?"
    n "아무 키나 클릭하여 진행하세요"
    hide message5
    show message6:
        xpos 55
        ypos 30
    $ moonsaying = "강력한 우주의 힘?"
    n "아무 키나 클릭하여 진행하세요"
    python:
        while(True):
            input = renpy.input(">> ")
            if "끝" in input or "홈" in input or "돌아" in input or "바탕화면" in input:
                moonsaying = "한번 접속해볼까"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide message6
    show neine:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if "makeitup.com" in input:
                moonsaying = "분명 코드가..."
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide neine
    show lovechat_background:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if input == "424242" :
                moonsaying = "누구지?"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "코드가 틀렸어"
    hide lovechat_background
    show alien_message_basic:
        xpos 55
        ypos 30
    n "아무 키나 클릭하여 진행하세요"
    hide alien_message_basic
    show alien_message_basic2:
        xpos 55
        ypos 30
    n "아무 키나 클릭하여 진행하세요"
    jump chat
    return

label chat:
    python:
        chatchoice = 0
        while(True):
            input = renpy.input(">> ")
            if "누가" in input or "누군" in input or "알려" in input:
                moonsaying = "사실대로 말하자"
                chatchoice = 1
                break
            elif "아무" in input or "무작위" in input:
                moonsaying = "정보를 받은건 숨기는게 좋겠어"
                chatchoice = 2
                break
            elif "해킹":
                moonsaying = "세게 나가볼까?"
                chatchoice = 3
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide alien_message_basic2
    if chatchoice == 1:
        show alien_massage_1_1:
            xpos 55
            ypos 30
        n "아무 키나 클릭하여 진행하세요"
        hide alien_massage_1_1
        show alien_massage_1_2:
            xpos 55
            ypos 30
        $ moonsaying = "만나자고?\n이거 그린라이트인가?"
        n "아무 키나 클릭하여 진행하세요"
        hide alien_massage_1_2
        show alien_massage_1_3:
            xpos 55
            ypos 30
        $ moonsaying = "우리집 앞?\n여긴 어떻게 안거야?"
        n "아무 키나 클릭하여 진행하세요"
        hide alien_massage_1_3
        show alien_massage_1_4:
            xpos 55
            ypos 30
        $ moonsaying = "해줘야 할 일?"
        n "아무 키나 클릭하여 진행하세요"
    elif chatchoice == 2:
        show alien_massage_2_1:
            xpos 55
            ypos 30
        n "아무 키나 클릭하여 진행하세요"
        hide alien_massage_2_1
        show alien_massage_2_2:
            xpos 55
            ypos 30
        $ moonsaying = "진지한 이야기?"
        python:
            hearchoice = 0
            while(True):
                input = renpy.input(">> ")
                if "네" in input or "응" in input or "그래" in input or "그렇" in input or "그럴" in input or "알겠" in input or "ㅇ" in input or "듣는다" in input or "들어본다" in input or "들어보자" in input:
                    moonsaying = "한번 들어보자"
                    hearchoice = 1
                    break
                elif "아니" in input or "안" in input or "않" in input or "싫" in input or "안해" in input or "ㄴ" in input or "안듣는다" in input or "안들어본다" in input or "안들어보자" in input or "안들어보겠" in input or "듣지":
                    moonsaying = "난 듣기 싫은데"
                    hearchoice = 2
                    break
                else:
                    moonsaying = "그렇게는 못해"
        hide alien_massage_2_2
        if hearchoice == 1:
            show alien_massage_2_3:
                xpos 55
                ypos 30
            n "아무 키나 클릭하여 진행하세요"
            $ moonsaying = "오랜 친구라\n어릴 적 친구가 생각나네"
            n "아무 키나 클릭하여 진행하세요"
            hide alien_massage_2_3
            show alein_message_oldfriend1:
                xpos 55
                ypos 30
            $ moonsaying = "나도 그런 친구가 있었지"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend1
            show alein_message_oldfriend2:
                xpos 55
                ypos 30
            $ moonsaying = "좋아\n찾는걸 도와주자"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend2
            show alein_message_oldfriend3:
                xpos 55
                ypos 30
            $ moonsaying = "지금?\n어디에서 보자는 거지?"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend3
            show alein_message_oldfriend4:
                xpos 55
                ypos 30
            $ moonsaying = "해킹이라니..."
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend4
            show alein_message_oldfriend5:
                xpos 55
                ypos 30
            $ moonsaying = "조금 무서운데\n뭐 별일이야 없겠지"
            n "아무 키나 클릭하여 진행하세요"
        elif hearchoice == 2:
            show alien_massage_2_2_angry1:
                xpos 55
                ypos 30
            $ moonsaying = "어...\n혹시 화났나?"
            n "아무 키나 클릭하여 진행하세요"
            hide alien_massage_2_2_angry1
            show alien_message_2_2_angry2:
                xpos 55
                ypos 30
            $ moonsaying = "뭐...라고...!?"
            n "아무 키나 클릭하여 진행하세요"
            jump destroyed
    elif chatchoice == 3:
        show alien_message_3_1:
            xpos 55
            ypos 30
        $ moonsaying = ""
        n "아무 키나 클릭하여 진행하세요"
        hide alien_message_3_1
        show alien_message_3_2:
            xpos 55
            ypos 30
        n "아무 키나 클릭하여 진행하세요"
        hide alien_message_3_2
        show alien_message_3_3:
            xpos 55
            ypos 30
        python:
            hearchoice = 0
            while(True):
                input = renpy.input(">> ")
                if "네" in input or "응" in input or "그래" in input or "그렇" in input or "그럴" in input or "알겠" in input or "ㅇ" in input or "듣는다" in input or "들어본다" in input or "들어보자" in input:
                    moonsaying = "한번 들어보자"
                    hearchoice = 1
                    break
                elif "아니" in input or "안" in input or "않" in input or "싫" in input or "안해" in input or "ㄴ" in input or "안듣는다" in input or "안들어본다" in input or "안들어보자" in input or "안들어보겠" in input or "듣지":
                    moonsaying = "난 듣기 싫은데"
                    hearchoice = 2
                    break
                else:
                    moonsaying = "그렇게는 못해"
        hide alien_message_3_3
        if hearchoice == 1:
            show alein_message_oldfriend1:
                xpos 55
                ypos 30
            $ moonsaying = "나도 그런 친구가 있었지"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend1
            show alein_message_oldfriend2:
                xpos 55
                ypos 30
            $ moonsaying = "좋아\n찾는걸 도와주자"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend2
            show alein_message_oldfriend3:
                xpos 55
                ypos 30
            $ moonsaying = "지금?\n어디에서 보자는 거지?"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend3
            show alein_message_oldfriend4:
                xpos 55
                ypos 30
            $ moonsaying = "해킹이라니..."
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend4
            show alein_message_oldfriend5:
                xpos 55
                ypos 30
            $ moonsaying = "조금 무서운데\n뭐 별일이야 없겠지"
            n "아무 키나 클릭하여 진행하세요"
        elif hearchoice == 2:
            show alien_message_hack_bad1:
                xpos 55
                ypos 30
            $ moonsaying = "어...\n혹시 화났나?"
            n "아무 키나 클릭하여 진행하세요"
            hide alien_message_hack_bad1
            show alien_message_hack_bad2:
                xpos 55
                ypos 30
            $ moonsaying = "뭐...라고...!?"
            n "아무 키나 클릭하여 진행하세요"
            jump destroyed
    jump secretagent
    return

label secretagent:
    hide alien_message_basic
    show background:
        xpos 55
        ypos 30
    $ moonsaying = "남는시간동안 뭘 해볼까"
    n "낯선 자와의 대화가 끝나고, 당신은 하던 일을 마저 하기로 합니다."
    python:
        while(True):
            input = renpy.input(">> ")
            if "인터넷" in input:
                moonsaying = "인터넷을 더 둘러보자"
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
    hide background
    show alien_do_not_exist:
        xpos 55
        ypos 30
    $ moonsaying = "이건 뭐지?"
    n "인터넷을 키자 낯선 화면이 보입니다."
    hide alien_do_not_exist
    show message_alert:
        xpos 55
        ypos 30
    $ moonsaying = "새로운 메세지?"
    python:
        while(True):
            input = renpy.input(">> ")
            if "읽" in input or "보" in input or "본" in input or "확인" in input:
                moonsaying = "누구지?"
                break
            elif ("전원" in input or "컴퓨터" in input) and ("끄" in input or "끈" in input or "꺼" in input):
                moonsaying = "메시지가 신경쓰이는걸"
            elif "나가" in input or "나간" in input or "돌아" in input or "바탕화면" in input:
                moonsaying = "메시지가 신경쓰이는걸"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide message_alert
    show agent_message1:
        xpos 55
        ypos 30
    $ moonsaying = "어떻게 지내냐니...\n일단 그럭저럭이라고 대답하자"
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message1
    show agent_message2:
        xpos 55
        ypos 30
    $ moonsaying = "흉흉하다고?"
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message2
    show agent_message3:
        xpos 55
        ypos 30
    $ moonsaying = "위험한 곳이라...\n난 현실보다 더 익숙하지만 말이야"
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message3
    show agent_message4:
        xpos 55
        ypos 30
    $ moonsaying = "구름? 무슨 소리지?"
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message4
    show agent_message5:
        xpos 55
        ypos 30
    $ moonsaying = "이게 무슨 소리야?\n물어봐야겠어"
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message5
    show agent_message6:
        xpos 55
        ypos 30
    $ moonsaying = "대화가 끊겼다..."
    n "아무 키나 클릭하여 진행하세요"
    hide agent_message6
    show background:
        xpos 55
        ypos 30
    $ moonsaying = "방금의 대화가 신경쓰이네"
    python:
        count = 0
        kdn = 0
        while(True):
            input = renpy.input(">> ")
            if count >= 5:
                kdn = 1
                break
            if ("vpn" in input or "VPN" in input or "프록시" in input or "구름" in input) and ("사용" in input or "켜" in input or "키" in input):
                moonsaying = "vpn을 사용하자"
                break
            elif "나가" in input or "나간" in input or "돌아" in input or "바탕화면" in input:
                moonsaying = "대화가 신경쓰이는걸"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
            count += 1
    if kdn == 1:
        jump kidnap
        return

    return

label destroyed:
    n "아직 안만듬 ㅅㄱ"
    return

label kidnap:
    n "아직 안만듬 ㅅㄱ"
    return