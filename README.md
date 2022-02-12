# 조 편성 프로그램

## 📌 Summary

**몇 가지 취향에 관한 설문 응답을 토대로 비슷한 취향을 가진 사람들끼리 조를 편성해 주는 프로그램**입니다. 동아리 활동을 하던 당시 몇백 명이나 되는 동아리원들을 대상으로 친목을 위한 조를 빠르게 편성하기 위해 직접 개발하였습니다.

스스로 일상생활에서 필요성을 느껴 개발함으로써 많은 사람에게 도움이 되었다는 사실에 큰 보람을 느꼈습니다. 또한 그다지 익숙하지 못했던 Python에 조금 더 익숙해질 수 있었던 계기였습니다.

사용 방법은 다음과 같습니다.

    1. 조모임에 참여하는 사람들의 응답 결과지를 담은 엑셀 파일을 준비한다.
    
    2. 해당 엑셀 파일에서 친목팀 임원진에 해당되는 행(Row)은 모두 삭제한다.
    
    3. 이름, 성별, 프로그램에서 반영할 항목에 해당되는 열(Column)만 남기고 나머지 열은 모두 삭제한다.
       이때 반드시 이름이 첫 번째 열이고 성별이 두 번째 열이어야 한다.
       (EX. 이름, 성별, 술자리 선호도, 밥자리 선호도, 노래방 선호도, 술자리 분위기)
       
    4. 엑셀 파일의 확장자를 .txt로 바꾸고, 파일의 이름을 "data_general"로 바꾼다.
    
    5. 해당 파일을 본 프로그램의 소스 코드와 같은 디렉토리(경로)에 넣는다.

<br />

## 🤔 Background

서울대학교 햇빛봉사단이라는 동아리에서 12기 친목팀장으로 활동할 당시, 몇백 명이나 되는 동아리원들을 대상으로 친목을 위한 조 편성을 해야 했던 적이 있습니다. 그런데 지금까지 친목팀장을 맡았던 분들은 이 작업을 전부 수작업으로 진행했었다는 말을 듣고, 이 작업을 최대한 자동화할 수는 없을까 고민하게 되었습니다. 물론 누구를 누구랑 붙여달라는 등의 몇 가지 요구사항을 반영하려면 결국 수작업은 필요하겠지만, 기본적으로 취향이 비슷한 사람들끼리 먼저 뭉쳐두는 것 정도는 프로그래밍으로 충분히 가능하다고 생각했습니다. 이것이 바로 이 프로그램을 구현하게 된 배경입니다.

<br />

## 🔍 Meaning

컴퓨터공학부를 나왔기 때문에 학교를 다니면서 정말 여러 종류의 프로그램을 개발해본 것 같습니다. 그러나 실제로 필요성을 피부로 느끼고 개발했다기보다는 과제나 프로젝트의 일환으로 개발한 것이 대부분이었습니다. 한 학기라는 짧은 기간에 다른 과목들과의 시간 분배를 매번 고민하면서 과제나 프로젝트를 해나간다는 느낌이 강했기 때문입니다. 그러다 보니 실제로 제가 필요해서 무언가를 개발해본 경험은 의외로 많지 않았습니다.

그런 면에서 이 프로그램은 개발이 가져다주는 진정한 즐거움을 알게 해주었습니다. 물론 프로그램의 로직 자체가 굉장히 화려하거나 복잡한 것은 아니지만, 현실의 문제를 제가 직접 피부로 느끼고 이를 개발을 통해 해결했다는 사실 자체가 저 자신의 분야에 대해 만족감을 느끼기에 아주 충분했기 때문입니다. 이런 데서 느끼는 사소한 보람 하나하나가 지금까지도 제가 개발의 길을 걷고 있는 이유 중 하나이지 않을까 싶습니다.

한편, 이 프로그램을 개발하면서 Python에 한층 더 익숙해진 것도 좋은 결실이었습니다. 당시에는 Python을 학습한 지 얼마 되지 않았어서 아직은 Python으로 개발을 하는 것에 익숙지 않았는데, 현실의 문제를 해결한다는 목적을 두고 공부하다 보니 더 빠르게 언어를 학습할 수 있었던 것 같습니다.

<br />

## 🔨 Technology Stack(s)

Python
