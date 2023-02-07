# removal_condition = 'age >= 23'
# result = removal_condition.split(' ')
# print(result)

student_list = []
attribute_name = ['student_id', 'name', 'department', 'sex', 'age', 'nationality', 'grade']  # 길이 7, index 6
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
        for i in range(len(student_list) - 1):
            if student_list[i][0] != student_id:
                continue
            else:
                student_list.pop(i)
                return False


find_count = 0
int_num = [0, 4, 6]

removal_condition = 'student_id < 20120000'
strarr = removal_condition.split(' ')
initialization()
print(len(student_list))
student_list2 = student_list[:]
for i in range(len(attribute_name) - 1):
    if strarr[0] == attribute_name[i] and i in int_num:
        for j in range(len(student_list2)):
            if strarr[1] == '==':  # 0, 4 int형일 경우
                if int(strarr[2]) == student_list2[j][i]:
                    if find_count > 0 and j >= 1:
                        student_list.pop(j - find_count)
                        find_count += 1
                    else:
                        student_list.pop(j)
                        find_count += 1
            elif strarr[1] == '>=':
                if int(strarr[2]) <= student_list2[j][i]:  # 2010
                    if find_count > 0 and j >= 1:
                        student_list.pop(j - find_count)
                        find_count += 1
                    else:
                        student_list.pop(j)
                        find_count += 1
            elif strarr[1] == '<=':
                if int(strarr[2]) >= student_list2[j][i]:
                    if find_count > 0 and j >= 1:
                        student_list.pop(j - find_count)
                        find_count += 1
                    else:
                        student_list.pop(j)
                        find_count += 1
            elif strarr[1] == '<':
                if int(strarr[2]) > student_list2[j][i]:
                    if find_count > 0 and j >= 1:
                        student_list.pop(j - find_count)
                        find_count += 1
                    else:
                        student_list.pop(j)
                        find_count += 1
            elif strarr[1] == '>':
                if int(strarr[2]) < student_list2[j][i]: # 2010
                    if find_count > 0 and j >= 1:
                        student_list.pop(j-find_count)
                        find_count += 1
                    else:
                        student_list.pop(j)
                        find_count += 1
            else:
                print("잘못된 접근입니다.")
print(len(student_list))
print('\n')
# student_list 새로 정의된 상태 (removal)
# f = open('C:/Users/수연/Desktop/파이썬_부스트코스/__MACOSX/._student_information.txt', 'w')
for i in range(len(student_list)-1):
    result = ', '.join(map(str, student_list[i]))
    print(result)