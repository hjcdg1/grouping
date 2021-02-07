import random
from collections import namedtuple

# 프로그램 설명
print('\n' + "=" * 130 + '\n' + '''
본 프로그램이 정상적으로 작동하려면 다음 절차를 따라야 합니다.

    1. 조모임에 참여하는 사람들의 응답 결과지를 담은 엑셀 파일을 준비한다.
    
    2. 해당 엑셀 파일에서 친목팀 임원진에 해당되는 행(Row)은 모두 삭제한다.
    
    3. 이름, 성별, 프로그램에서 반영할 항목에 해당되는 열(Column)만 남기고 나머지 열은 모두 삭제한다.
       이때 반드시 이름이 첫 번째 열이고 성별이 두 번째 열이어야 한다.
       (EX. 이름, 성별, 술자리 선호도, 밥자리 선호도, 노래방 선호도, 술자리 분위기)
       
    4. 엑셀 파일의 확장자를 .txt로 바꾸고, 파일의 이름을 "data_general"로 바꾼다.
    
    5. 해당 파일을 본 프로그램의 소스 코드와 같은 디렉토리(경로)에 넣는다.
''' + '\n' + "=" * 130 + '\n')

input("위 설명을 이해하였으면 아무 키나 입력하고 엔터를 치세요. \n\n>>> ")

attrs_input = input('\n' + "=" * 130 + '\n' + '''
위 설명의 3번에서 남긴 열들에 해당되는 항목들(이름과 성별까지 포함)을 "차례대로" 입력해주세요.

단, 각 항목은 띄어쓰기로 구분해주시고 꼭 영어로 입력해주세요.

(EX. "name sex liquor rice karaoke mood"라고 입력 후 엔터)

>>> ''')
print('\n' + "=" * 130 + '\n')
attrs_list = attrs_input.strip().split()
attrs_len = len(attrs_list)

priority_input = input('\n' + "=" * 130 + '\n' + '''
방금 입력한 항목들 중, 이름과 성별을 제외한 나머지 항목들의 중요도를 "차례대로" 입력해주세요.

단, 각 항목은 띄어쓰기로 구분해주시고 숫자(정수 혹은 실수)로 입력해주세요.

(EX. "3 2 1 4"라고 입력 후 엔터)

>>> ''')
print('\n' + "=" * 130 + '\n')
priority_list = priority_input.strip().split()
for i in range(0, len(priority_list)) :
    priority_list[i] = float(priority_list[i])

# Person 클래스의 정의
Person = namedtuple("Person", attrs_list)

# 엑셀 내용 로드 ('data_general.txt'는 임원진을 제외한 단원들의 응답 결과지이다.)
person_list = []
with open('data_general.txt', 'r') as f :
    f.readline()    # 첫 줄은 버린다.
    while True :
        line = f.readline()
        if not line :
            break
        a = line.split("\t")
        args = [a[0].strip(), a[1].strip()]
        for i in range(2, attrs_len) :
            args.append(float(a[i]))
        person = Person(*args)
        person_list.append(person)
random.shuffle(person_list)

# 초기화
K = int(input("몇 개의 조로 나눌 생각인가요? : "))
S = len(person_list) // K
groups = []
group_size = []
group_man_size = []
center_list = []
person_dist_list = []
for i in range(0, K) :
    groups.append([])
    group_size.append(0)
    group_man_size.append(0)
    center_list.append(None)
print(('\n' + "=" * 130 + '\n' + '''
임원진을 제외하고 조모임에 참여하는 사람의 수는 {0}명입니다.

그리고 당신은 그 사람들을 {1}개의 조로 나누기로 결정했습니다.

그러므로 한 조에는 대략 {2}명이 들어가게 됩니다.

본 프로그램에서는 순수히 선호도의 유사도만 고려되었습니다.

따라서 다음과 같은 사항들은 직접 수작업을 통해 반영해야 합니다.

    1. 같은 조가 되고 싶은 사람 (인당 1명까지만 반영하는 걸 권고)
 
    2. 다른 조가 되고 싶은 사람 (반드시 반영하는 걸 권고)
 
    3. 각 조에서의 남녀 성비 맞추기
''' + '\n' + "=" * 130 + '\n').format(len(person_list), K, S))
input("결과를 보시려면 아무 키나 입력하고 엔터를 치세요. \n\n>>> ")
print("\n\n\n\n")

def distance(a, b) :
    d = 0.0
    for i in range(2, attrs_len) :
        d += (priority_list[i-2] * (a[i] - b[i])) ** 2
    return d

def distance_list(person, center_list) :
    dist = []
    for i in range(0, K) :
        dist.append(distance(person, center_list[i]))
    return dist

def find_center(group) :
    values = []
    for i in range(2, attrs_len) :
        values.append(0)
        for person in group :
            values[i-2] += person[i]
        values[i-2] /= len(group)
    args_list = ["", ""]
    for value in values :
        args_list.append(value)
    center = Person(*args_list)
    return center

def check(old, new) :
    a = 0.0
    for i in range(0, K) :
        a += distance(old[i], new[i])
    a /= K
    return a < 0.0000000001

def variance(group, center) :
    v = 0.0
    for person in group :
        v += distance(person, center)
    v /= len(group)
    return v

# k개의 중심점 임의 선택
number_list = list(range(0, K * S))
for i in range(0, K) :
    number = random.choice(number_list)
    number_list.remove(number)
    center_list[i] = person_list[number]
    groups[i].append(person_list[number])
    group_size[i] += 1
    if person_list[number][1] == "남" :
        group_man_size[i] += 1

# 모든 사람 각각에 대하여 중심점들과의 거리를 계산
for person in person_list :
    dist_list = distance_list(person, center_list)
    person_dist_list.append(dist_list)

# k개의 군집 구성
for i, person in enumerate(person_list) :
    if person in center_list :
        continue

    min_dist = min(person_dist_list[i])
    min_index = person_dist_list[i].index(min_dist)

    while group_size[min_index] >= S :
        if i >= K * S :
            break
        person_dist_list[i][min_index] = 100000000.0
        min_dist = min(person_dist_list[i])
        min_index = person_dist_list[i].index(min_dist)

    groups[min_index].append(person)
    group_size[min_index] += 1
    if person[1] == "남" :
        group_man_size[min_index] += 1

# Iteration
iter = 0
while True :
    # center_list 수정
    old_center_list = list(center_list)
    for i in range(0, K) :
        center_list[i] = find_center(groups[i])
    if check(old_center_list, center_list) :
        break

    # 초기화
    groups = []
    group_size = []
    group_man_size = []
    for i in range(0, K):
        groups.append([])
        group_size.append(0)
        group_man_size.append(0)

    # 모든 사람 각각에 대하여 중심점들과의 거리를 계산
    person_dist_list = []
    for person in person_list :
        dist_list = distance_list(person, center_list)
        person_dist_list.append(dist_list)

    # k개의 군집 구성
    for i, person in enumerate(person_list) :
        if person in center_list:
            continue

        min_dist = min(person_dist_list[i])
        min_index = person_dist_list[i].index(min_dist)

        while group_size[min_index] >= S :
            if i >= K * S:
                break
            person_dist_list[i][min_index] = 100000000.0
            min_dist = min(person_dist_list[i])
            min_index = person_dist_list[i].index(min_dist)

        groups[min_index].append(person)
        group_size[min_index] += 1
        if person[1] == "남":
            group_man_size[min_index] += 1

    iter += 1

# 결과 출력
for i, group in enumerate(groups) :
    print("=" * 60)
    print("<{0}조>".format(i+1))
    print("인원수: {0}, 편차: {1}".format(len(group), variance(group, center_list[i])))
    print("남자: {0}, 여자: {1}".format(group_man_size[i], len(group) - group_man_size[i]))
    print("")
    for p in group :
        args_list = []
        for i in range(0, attrs_len) :
            args_list.append(p[i])
        print(*args_list)
    print("=" * 60)
    print()
print("{}번의 반복으로 얻어낸 결과입니다.".format(iter))
