student_list = []
attribute_name = ['student_id', 'name', 'department', 'sex', 'age', 'nationality', 'grade'] # 길이 7, index 6
attribute_type = ['int', 'char', 'char', 'char', 'int', 'char', 'int']


def initialization():
    f = open('C:/Users/수연/Desktop/파이썬_부스트코스/__MACOSX/._student_information.txt', 'r')
    lines = f.readlines()
    for line in lines:
        addition(line)


def addition(str):
    std = str.strip().split(', ')
    # 20118888, Dongyup Shin, Computer Science, M, 26, KOR, 3.84
    # 속성 유형을 변경. ex) '20118888' -> int형 20118888으로 변경
    student_id = 0
    if '20' in std[0]:
        student_id = int(std[0])
    if len(std[1]) > 20:
        return False
    if len(std[2]) > 50:
        return False
    if len(std[3]) > 1:
        return False
    if len(std[5]) > 3:
        return False
    student_age = int(std[4])
    student_grade = float(std[6])
    student_list.append((student_id, std[1], std[2], std[3], student_age, std[5], student_grade))
    # 같은 student_id 있을 때 추가하지 않고, false 반환하기
    if len(student_list) > 0:
        for i in range(len(student_list)-1):
            if student_list[i][0] != student_id:
                continue
            else:
                student_list.pop(i)
                return False


def statistic(str, attr): # str: ['student_id', '>=', '20118889'], attr: 'age'
    find_sum = 0
    find_count = 0
    int_num = [0, 4, 6] # age, grade
    for i in range(len(attribute_name)-1):
        if str[0] == attribute_name[i]: # student_id == attribute_name[0]
            for j in range(len(student_list) - 1):  # 리스트의 길이-1 만큼
                if i in int_num: # int
                    if str[1] == '==':
                        if int(str[2]) == student_list[j][i]: # 20118889 == student_list[0][0]
                            find_sum += student_list[j][i] # find_sum += 20118889
                            find_count += 1
                        else:
                            continue
                    elif str[1] == '>=':
                        if int(str[2]) <= student_list[j][i]: # 20118889 <= student_list[1][0]
                            if attr == 'age':
                                find_sum += student_list[i][4] # find_sum += student_list[1][4]
                                find_count += 1
                            elif attr == 'grade':
                                find_sum += student_list[i][6]
                                find_count += 1
                        else: # 조건 수가 list 속성보다 클 경우.
                            continue
                    elif str[1] == '<=':
                        if int(str[2]) >= student_list[j][i]:
                            find_sum += student_list[j][i]
                            find_count += 1
                        else:
                            continue
                    elif str[1] == '>':
                        if int(str[2]) < student_list[j][i]:
                            find_sum += student_list[j][i]
                            find_count += 1
                        else:
                            continue
                    elif str[1] == '<':
                        if int(str[2]) > student_list[j][i]:
                            find_sum += student_list[j][i]
                            find_count += 1
                        else:
                            continue
                    else:
                        print("잘못된 접근입니다.")
                else:  # str형, student_id일 경우
                    if str[2] == student_list[j][i]:
                        find_count += 1
                    else:
                        continue
        else:
            continue
    char_list = ['name', 'department', 'sex', 'nationality']
    if attr in char_list:
        print(f'Statistics of {attr}\nCount: {find_count}')
    else:
        print(f'Statistics of {attr}\nSum: {find_sum}\tCount: {find_count}\tAverage: {find_sum / find_count}')


def removal(str):  # ex) nationality == AUS -> ['nationality', '==', 'AUS']
    if str == '':
        student_list.clear()
        return True

    find_count = 0
    int_num = [0, 4]
    i = 0
    j = 0

    for i in range(len(attribute_name)-1):  # 0~6
        for j in range(len(student_list)-1):  # 0~6
            if str[0] == attribute_name[i] and i in int_num:
                if str[1] == '==':  # 0, 4 int형일 경우
                    if int(str[2]) == student_list[j][i]:
                        student_list.pop(j)
                        find_count += 1
                    else:
                        continue
                elif str[1] == '>=':
                    if int(str[2]) <= student_list[j][i]:
                        student_list.pop(j)
                        find_count += 1
                    else:
                        continue
                elif str[1] == '<=':
                    if int(str[2]) >= student_list[j][i]:
                        student_list.pop(j)
                        find_count += 1
                    else:
                        continue
                elif str[1] == '>':
                    if int(str[2]) < student_list[j][i]:
                        student_list.pop(j)
                        find_count += 1
                    else:
                        continue
                elif str[1] == '<':
                    if int(str[2]) > student_list[j][i]:
                        student_list.pop(j)
                        find_count += 1
                    else:
                        continue
                else:
                    print("잘못된 접근입니다.")
            elif str[0] == attribute_name[i] and i not in int_num:
                if str[2] == student_list[j][i]:
                    student_list.pop(j)
                    find_count += 1
                else:
                    continue
            else:
                continue
        if find_count < 1:
            return False
        if j == len(student_list)-1:  # j가 리스트를 다 돌았을 경우
            return True

initialization()

print(len(student_list))
removal_condition = 'student_id < 20100000'
if removal_condition == '':
    removal(removal_condition)
else:
    result = removal_condition.split(' ')
    removal(result)
print(len(student_list))

# result = input("input a condition: ") # 조건
# condition = result.split(' ') # ex: ['student_id', '>=', '20110000']
# attribute = input("input a attribute: ") # 속성 이름
# statistic(condition, attribute)
