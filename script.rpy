# Define the character images and UI elements
image character = "character.png"
image bgmain = "bgmain.png"
image basic = "basic.png"
image characterbox = "characterbox.png"
image saying = "saying.png"
image background = "background.png"
image background_vpn_on = "background_vpn_on.png"
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
image alien_massage_1_1 = "alien_message_1.png"
image alien_massage_1_2 = "alien_message_1-1.png"
image alien_massage_1_3 = "alien_message_1-2.png"
image alien_massage_1_4 = "alien_message_1-3.png"
image alien_massage_2_1 = "alien_message_2-1.png"
image alien_massage_2_2 = "alien_message_2-2.png"
image alien_massage_2_3 = "alien_message_2-3.png"
image alien_massage_2_2_angry1 = "alien_message_2-2-angry1.png"
image alien_message_2_2_angry2 = "alien_message_2-2-angry2.png"
image alien_message_3_1 = "alien_message_3-1.png"
image alien_message_3_2 = "alien_message_3-2.png"
image alien_message_3_3 = "alien_message_3-3.png"
image alien_message_hack_bad1 = "alien_message_1-4.png"
image alien_message_hack_bad2 = "alien_message_1-5badend.png"
image alien_message_oldfriend0 = "alien_message_1-3-1.png"
image alein_message_oldfriend1 = "alien_message_1-3-2.png"
image alein_message_oldfriend2 = "alien_message_1-3-3-3.png"
image alein_message_oldfriend3 = "alien_message-1-3-3-4.png"
image alein_message_oldfriend4 = "alien_message_1-3-3-5.png"
image alein_message_oldfriend5 = "alien_message_1-3-3-6.png"
image alien_do_not_exist = "aliens_do_not_exist.png"
image message_alert = "message_alert.png"
image agent_message1 = "agent1.png"
image agent_message2 = "agent2.png"
image agent_message3 = "agent3.png"
image agent_message4 = "agent4.png"
image agent_message5 = "agent5.png"
image agent_message6 = "agent6.png"
image breakwindow = "breakwindow.png"
image marsattack = "marsattack.png"
image pizzaguy = "pizzaguy.png"
image alienboss = "alienboss.png"
image raptilianagent = "raptilian.png"
image babymoon = "babymoon.png"
image moon = "character.png"
image babysui = "babysui.png"
image sui = "sui.png"
image pizzadeliver = "realpizzadeliver.png"
image black = "black.png"
image ending = "ending.png"
image pastremember = "pastremember.png"
image UFOinside = "UFOinside.png"

define n = Character(color = "#FFFFFF")
define moon = Character(name = "당신", color = "#00FF00")
define alien = Character(name = "??", color = "#A374DB", image = "sui.png")
define sui = Character(name = "혜성", color = "#A374DB", image = "sui.png")
define alienboss = Character(name = "외계대장", color = "#ff00ff", image = "alienboss.png")
define pizzadeliver = Character(name = "????", color = "#ffff00")
define raptilianagent = Character(name = "랩틸리언", color = "#ffff00", image = "raptilian.png")
define babyalien = Character(name = "??", color = "#A374DB", image = "babysui.png")

init:
    $ moonsaying = ""

screen mainsaying:
    text "[moonsaying]" xpos 950 ypos 370 size 18

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
    show screen mainsaying
    jump meetalien
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
            elif "피자" in input and ("주문" in input or "시키" in input or "시킨" in input):
                moonsaying = "먼저 전화를 해야해"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    n "\"네, 포톤피자입니다. 무엇을 도와드릴까요?\""
    python :
        while(True):
            input = renpy.input(">> ")
            if "주" in input and "피자" in input:
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

    hide aliennews
    show news_comment:
        xpos 55
        ypos 30
    $ moonsaying = "이상한 사람이 있네\n검색해볼까"
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
            elif "돌아" in input or "뒤로" in input or "홈" in input or "나" in input:
                moonsaying = "댓글이 신경쓰이는걸"
            else:
                moonsaying = "그렇게는 못해"
    
    hide news_comment
    show search_one:
        xpos 55
        ypos 30
    python:
        while(True):
            input = renpy.input(">> ")
            if "빅상민" in input:
                moonsaying = "이 사람은 뭐지?"
                break
            if "돌아" in input or "뒤로" in input or "홈" in input or "나" in input:
                moonsaying = "카페가 신경쓰이는걸"
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "*꿀꺽*\n마운틴듀는 최고야"
            else:
                moonsaying = "그렇게는 못해"
    hide search_one
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
    n "카페에 가입하니 메세지가 와있습니다."
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
    $ moonsaying = "강력한 우주의 힘?\n일단 검색창으로 돌아가자"
    n "아무 키나 클릭하여 진행하세요"
    python:
        while(True):
            input = renpy.input(">> ")
            if "접속" in input or "들어" in input or "돌아" in input or "바탕화면" in input:
                moonsaying = "한번 접속해볼까\n분명 주소가..."
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
            if "누가" in input or "누군" in input or "알려" in input or "빅상민" in input or "canyouhearmefellas" in input:
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
        hide alien_massage_1_4
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
                if "네" in input or "응" in input or "그래" in input or "그렇" in input or "그럴" in input or "알겠" in input or "ㅇ" in input or "듣" in input or "들" in input:
                    moonsaying = "한번 들어보자"
                    hearchoice = 1
                    break
                elif "아니" in input or "안" in input or "않" in input or "싫" in input or "안해" in input or "ㄴ" in input or "안듣는다" in input or "안들" in input or "듣지" in input:
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
            show alien_message_oldfriend0:
                xpos 55
                ypos 30
            $ moonsaying = "나도 그런 친구가 있었지"
            n "아무 키나 클릭하여 진행하세요"
            hide alien_message_oldfriend0
            show alein_message_oldfriend1:
                xpos 55
                ypos 30
            $ moonsaying = "갑자기 나를 떠나버린 그녀석..."
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
            hide alien_message_2_2_angry2
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
                if "네" in input or "응" in input or "그래" in input or "그렇" in input or "그럴" in input or "알겠" in input or "ㅇ" in input or "듣" in input or "들" in input:
                    moonsaying = "한번 들어보자"
                    hearchoice = 1
                    break
                elif "아니" in input or "안" in input or "않" in input or "싫" in input or "안해" in input or "ㄴ" in input or "안듣는다" in input or "안들"  in input or "듣지" in input:
                    moonsaying = "난 듣기 싫은데"
                    hearchoice = 2
                    break
                else:
                    moonsaying = "그렇게는 못해"
        hide alien_message_3_3
        if hearchoice == 1:
            show alien_message_oldfriend0:
                xpos 55
                ypos 30
            $ moonsaying = "갑자기 떠난 친구라"
            n "아무 키나 클릭하여 진행하세요"
            hide alein_message_oldfriend0
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
            hide alein_message_oldfriend5
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
            hide alien_message_hack_bad2
            jump destroyed
    jump secretagent
    return

label secretagent:
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
            if "읽" in input or "보" in input or "본" in input or "확인" in input or "디스코드" in input or "디코" in input or "메세지" in input or "메시지" in input:
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
    $ moonsaying = "위험한 곳이라...\n난 현실보다 더 익숙하지만 \n말이야"
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
            if count > 4:
                kdn = 1
                break
            if ("vpn" in input or "VPN" in input or "프록시" in input or "구름" in input) and ("사용" in input or "켜" in input or "키" in input or "켠" in input or "킨" in input):
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
        hide background
        jump kidnap
        return
    hide background
    show background_vpn_on:
        xpos 55
        ypos 30
    n "당신은 vpn을 켰다. 왠지 안전해진 기분이 든다"
    $ moonsaying = "슬슬 10분이..."
    n "*쿠웅*"
    $ moonsaying = "뭐야?"
    python:
        while(True):
            input = renpy.input(">> ")
            if ("창문" in input or "커튼" in input) and ("열" in input or "연" in input):
                moonsaying = "창문을 열어보자"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "지금 그럴 때가 아니야"
            else:
                moonsaying = "그렇게는 못해"
    n "창문을 열자 밖에는 커다란 UFO가 떠있습니다."
    jump meetalien
    return

label meetalien:
    hide background_vpn_on
    show basic:
        xpos 55
        ypos 30
    $ moonsaying = "외계인? \n어디서 본거같은데"
    n "UFO에서 내린 외계인은 어딘가 익숙한 모습을 하고 있습니다."
    show sui:
        xpos 355
        ypos 220
    alien "반가워. 날 따라와."
    python:
        follow = 0
        input = renpy.input(">> ")
        if "따라가지" in input or "타지" in input or "않" in input or "도망" in input:
            follow = 1
            moonsaying = "따라가야 할 것 \n같은 기분이..."
        elif "따라" in input or "타" in input or "탄" in input :
            follow = 2
            moonsaying = "외계인을 따라가자"
        else :
            follow = 1
    if follow == 1 :
        n "당신은 알 수 없는 힘에 이끌려 외계인을 따라갑니다."
    if follow == 2 :
        n "당신은 외계인을 따라 UFO에 탑승합니다."
    
    hide background
    show UFOinside:
        xpos 55
        ypos 30
    hide sui
    show sui:
        xpos 355
        ypos 220
    $ moonsaying = "내부는 이렇게 생겼구나"
    alien "도와줘서 고마워."
    $ moonsaying = "사람?"
    alien "난 10년 전에 지구에서 만난 사람을 찾고 있어"
    $ moonsaying = "10년 전이라니"
    alien "우리 종족이 지구에 오기 전, 선발대를 몇 명 보내 지구의 인간을 조사했어"
    $ moonsaying = ""
    alien "나는 그 중 한명이었고."
    alien "나는 지구에서 한 사람을 만났어."
    alien "그 사람은 나에게 우정과 사랑을 가르쳐줬지."
    alien "하지만 대부분의 선발대는 인간의 폭력적인 면을 본 것 같아."
    alien "난 그들에게 폭력적이고 위험한 인간의 이야기를 많이 들었어."
    alien "우리의 대장은 지구인이 위험하다고 생각해."
    alien "인류의 과학 수준이 우리를 따라잡기 전에 처리하고 싶어하지."
    alien "하지만 나는 지구인에게서 다른 모습들을 봤어."
    alien "내가 오래전 봤던 그 인간!"
    alien "그 인간을 데려가면 대장은 지구에 대한 공격을 멈출거야."
    $ input = renpy.input(">> ")
    if "좋" in input or "알" in input or "데려" in input or "가자" in input or "간다" in input:
        $ moonsaying = "좋아. 그 인간을 찾아가자."
        alien "먼저 대장한테 가자."
    else :
        $ moonsaying = "별로 그러고싶지 않은데"
        alien "무슨 소리를 하는거야?"
        alien "인류가 멸망하는걸 보고싶지 않다면 서둘러"
        alien "먼저 대장한테 가자."

    # 외계대장 얼굴
    $ moonsaying = "저게 그 대장?"
    hide sui
    show sui:
        xpos 140
        ypos 220
    show alienboss:
        xpos 570
        ypos 220
    alienboss "돌아왔군, 혜성."
    sui "네, 대장님."
    alienboss "그리고 반갑다, 지구인."
    $ moonsaying = renpy.input(">> ")
    alienboss "공격 개시까지 얼마 남지 않았다."
    alienboss "그 사람을 찾아오지 않는다면 공격을 감행할 것이다."

    $ moonsaying = "배달? 여기로?"
    n "*띵동*"
    sui "이게 무슨 소리지?"
    python:
        opendoor = 0
        while(True):
            input = renpy.input(">> ")
            if "열지" in input or "안" in input or "않" in input:
                opendoor = 1
                moonsaying = "문을 열지 않는게 \n좋아보이는데"
                break
            elif "연" in input or "열" in input :
                opendoor = 2
                moonsaying = "배달이다!"
                break
            else:
                moonsaying = "그렇게는 못해"
    alienboss "지구에는 이런 문화가 있는 것인가"
    $ moonsaying = "뭐...라고...!?"
    if opendoor == 1:
        pizzadeliver "이렇게 된 이상 무단침입이다!"
    elif opendoor == 2:
        pizzadeliver "하하, 속았지!"
    show raptilianagent:
        xpos 355
        ypos 220
    raptilianagent "우리는 대한민국 정부 소속 랩틸리언 부대다!"
    $ moonsaying = "그 찌라시 기사가 \n사실이었다니..."
    raptilianagent "우리 영공을 침해한 너희들을 모조리 박살내버리겠다!"
    alienboss "용감하게 싸워라, 유누성의 전사들이여!"
    $ moonsaying = "유누...성?"
    alienboss "저 도마뱀들을 전부 박살내는거다!"
    $ moonsaying = "잠깐만! \n유누성이라면 분명..!"
    n "*퍽*"
    $ moonsaying = "으윽"
    n "당신은 어디선가 날아온 파편을 맞고 기절했습니다"
    jump past
    return

label past:
    # 과거회상 시작
    hide UFOinside with dissolve
    show pastremember with dissolve:
        xpos 55
        ypos 30
    hide alienboss
    hide sui
    hide raptilianagent
    hide character
    show babymoon:
        xpos 970
        ypos 50
    show babysui:
        xpos 355
        ypos 220
    $ moonsaying = "왜 그래? \n오늘따라 말이 없네"
    babyalien "..."
    $ moonsaying = "뭐...라고...!?"
    babyalien "나... 고향으로 돌아가야 한대..."
    $ moonsaying = "무슨 소리야?"
    babyalien "내가 보고싶으면 하늘에서 가장 밝은 별인 유누성을 찾아줘."
    $ moonsaying = "그럼 평생 \n못보는거잖아!"
    babyalien "나도 너가 생각날 때마다 지구를 바라볼게."
    $ moonsaying = "몰라! \n너 미워!"
    babyalien "잠깐! 기다려!"
    hide pastremember with dissolve
    show UFOinside with dissolve:
        xpos 55
        ypos 30
    hide babysui
    hide babymoon
    show character:
        xpos 970
        ypos 50
    show sui:
        xpos 140
        ypos 220
    show alienboss:
        xpos 570
        ypos 220
    show raptilianagent:
        xpos 355
        ypos 220
    $ moonsaying = "설마 혜성이 찾던 \n사람이..."
    n "당신은 다시 의식을 찾았습니다."
    $ moonsaying = "*커다란 소리*"
    n "지구의 평화를 위해 빨리 이 사실을 알려야 합니다!"
    $ moonsaying = "분명 학교폭력을 \n멈추는 방법이..."
    n "주변의 소리가 너무 커서 싸움을 멈추기 쉽지 않아 보입니다."
    python:
        count = 0
        kdn = 0
        while(True):
            if count > 4:
                kdn = 1
                break
            input = renpy.input(">> ")
            if "멈춰" in input :
                kdn = 2
                break
            else :
                moonsaying = "목소리가 \n닿지 않아"
            count += 1
    if kdn == 1:
        jump rip
    elif kdn == 2:
        jump stopfight
    return

label stopfight:
    
    $ moonsaying = "멈춰!"
    n "순식간에 주변이 조용해졌습니다."
    $ moonsaying = ""
    moon "더 이상 싸울 필요는 없어요!"
    moon "내가 유누성인이 찾던 그 사람이고, 유누성인들은 화친을 위해 지구에 온거니까요!"
    raptilianagent "이게 무슨 도마뱀소리야?"
    moon "유누성인들은 우정과 사랑을 가르쳐준 인간을 찾아왔어요."
    moon "그 사람을 찾는다면 지구인과 유누성인의 화합이 가능할 것이라 믿고요."
    moon "기절한 순간 기억났어요. 어렸을 때 분명 유누성이라는 이름을 들은 적이 있다는걸."
    sui "설마..!"
    moon "혜성아, 나 기억났어."
    moon "너가 가버린 뒤로 난 방에만 틀어박혀있었지."
    moon "이젠 더이상 방 안에만 있지 않을거야."
    moon "너가 내 날개다!"
    sui "대장님, 이 인간이 제가 말한 그 사람입니다."
    sui "말투가 인터넷 많이 한 사람처럼 다소 어색하고 피자배달부 말고는 얘기해본 적이 없는 사람처럼 목소리가 다소 갈라지긴 했지만!"
    sui "방금도 보셨다시피 저희의 전투를 말 한마디로 끝내지 않았습니까!"
    alienboss "...과연"
    alienboss "좋아. 유누성인과 지구인은 오늘부터 친구다."
    alienboss "그리고..."
    alienboss "도마뱀머리들?"
    raptilianagent "국가안보를지키기위해오늘도이한몸희생하는위대하고고귀한랩틸리언대원 이라고 불러라!"
    alienboss "..."
    alienboss "그대들은 정부의 사람인가?"
    raptilianagent "그렇다!"
    alienboss "그렇다면 나를 정부에게 안내해라."
    alienboss "윤우성대통령과 직접 대화를 하겠다."
    alienboss "인간. 너도 함께 가지 않겠나?"
    moon "당연하지!"
    jump happyend
    return

label happyend:
    n "*띵동*"
    raptilianagent "이번엔 우리가 아닌데"
    hide sui
    hide alienboss
    hide raptilianagent
    show pizzadeliver:
        xpos 355
        ypos 220
    n "포톤피자에서 주문한 피자가 이제야 도착했습니다."
    n "배달이 오래 걸려 미안하다고 연거푸 고개를 숙이네요."
    n "그래도 덕분에 파인애플 피자를 오랜 친구에게 소개시켜 줄 수 있게 되었습니다!"
    hide pizzadeliver
    show sui:
        xpos 355
        ypos 220
    n "혜성도 파인애플 피자가 마음에 드는 모양인지 오랜 시간 동안 노려보고 있습니다."
    n "저 독특한 손동작은 유누성인들이 매우 맛있을 때 하는 동작이 틀림 없습니다!"
    hide characterbox
    hide character
    hide saying
    hide screen mainsaying
    hide background
    hide UFOinside
    scene ending
    hide bgmain
    hide sui
    show sui with dissolve:
        xpos 540
        ypos 20
    show moon with dissolve:
        xpos 280
        ypos 20
    show raptilianagent with dissolve:
        xpos 800
        ypos 20
    n "지구는 곧 세 종족, 아니, 더 많은 종족들이 함께 살아가는 새로운 세상이 될 것입니다."
    n "서로를 이해하는 데에 꽤 오랜 시간이 걸리겠지만"
    n "결국 우리는 서로를 사랑하게 될 것입니다!"
    n "HAPPY END \n다 함께 방 안으로"
    return

label destroyed:
    show basic:
        xpos 55
        ypos 30
    $ moonsaying = "무슨 일이야?"
    n "*콰앙*"
    n "창문 밖에서 갑자기 폭발음이 들렸습니다"
    python:
        while(True):
            input = renpy.input(">> ")
            if ("창" in input or "커" in input or "커" in input) and ("보" in input or "열" in input or "연" in input):
                moonsaying = "창문을 열어보자"
                break
            elif "마운틴듀" in input and ("마신" in input or "마시" in input or "먹" in input):
                moonsaying = "지금 그럴 때가 아니야"
            else:
                moonsaying = "창 밖의 소리가 신경쓰이는걸"
    hide characterbox
    hide character
    hide saying
    hide screen mainsaying
    hide background
    hide bgmain
    scene marsattack

    n "창문을 열어보니 하늘을 뒤덮은 UFO와 폐허가 된 도시가 보입니다."
    n "창문을 열어보니 하늘을 뒤덮은 UFO와 폐허가 된 도시가 보입니다.\n외계인들의 침공으로 인류는 멸망했습니다."
    n "BAD END \n드디어 방 밖으로"
    return

label kidnap:
    show basic:
        xpos 55
        ypos 30
    $ moonsaying = "피자가 왔나?"
    n "*띵동*"
    pizzadeliver "페퍼로니 피자 배달왔습니다"
    menu :
        "문을 연다." :
            $ moonsaying = "배고팠는데 잘됐네"
            n "아무 키나 클릭하여 진행하세요"
            hide characterbox
            hide character
            hide saying
            hide screen mainsaying
            hide basic
            hide bgmain
            scene pizzaguy
            raptilianagent "ㅎㅇ?"
            
        "문을 열지 않는다." :
            $ moonsaying = "난 파인애플 피자를 \n시켰는데..?"
            n "아무 키나 클릭하여 진행하세요"
            hide characterbox
            hide character
            hide saying
            hide screen mainsaying
            hide basic
            hide bgmain
            scene kidnap
            n "*와장창*"

    n "당신은 국가안보를지키기위해활동하는국가의비밀요원 랩틸리언에게 납치당했습니다."
    n "당신은 랩틸리언에게 납치당했습니다.\n그 뒤로 당신의 모습을 본 사람은 아무도 없었습니다."
    n "BAD END \n영원히 방 안에"  
    return

label rip:
    hide characterbox
    hide character
    hide saying
    hide screen mainsaying
    hide basic
    hide bgmain
    scene black
    raptilianagent "야! 인간을 죽이면 어떡해!"
    raptilianagent "인간이 저렇게 나약할줄은 몰랐지!"
    raptilianagent "초광자머신건 다섯 발 정도 맞았다고 죽을건 뭐야?"
    n "당신은 유누성인과 랩틸리언의 전투에 휘말려 사망했습니다."
    n "두 종족은 당신의 죽음을 10초정도 애도하고 전투로 돌아갔으며"
    n "당신이 지구가 어떻게 변했는지 알 길은 영영 사라지고 말았습니다."
    n "BAD END \n불 꺼진 방"
    return