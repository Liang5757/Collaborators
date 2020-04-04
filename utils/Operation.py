# OS操作, 传入表达式/答案/正确率保存到文件
import os

# 文件保存位置
# if not os.path.exists('../docs'):
#     os.mkdir('../docs')


# 保存题目 传入序列号以及题目
def save_exercise(expressions_str):
    exercise_file = '../docs/Exercises.txt'
    try:
        with open(exercise_file, 'w+', encoding='utf-8') as f:
            for line in expressions_str:
                f.write('{}\n'.format(line))
    except IOError:
        print('Exercise.txt create failed. Please check again')


# 保存答案 传入序列号以及答案
def save_answer(answers_str):
    answer_file = '../docs/Answer.txt'
    try:
        with open(answer_file, 'w+', encoding='utf-8') as f:
            for line in answers_str:
                f.write('{}\n'.format(line))
    except IOError:
        print('Answer.txt create failed. Please check again')


# 保存比较结果 传入正确列表以及错误列表
def inspect(correct_list, wrong_list):
    inspect_file = '../docs/Grade.txt'
    try:
        with open(inspect_file, 'w+', encoding='utf-8') as f:
            f.write(f'Correct: {len(correct_list)}{correct_list}\n'
                    f'Wrong: {len(wrong_list)}{wrong_list}\n'
                    f'Accuracy: {round(len(correct_list)/len(wrong_list), 4) * 100}%\n')
    except IOError:
        print('Grade.txt create failed. Please check again')


if __name__ == '__main__':
    save_exercise(['1+1', '2+3'])
    # a = ['1+1', '2+2']
    # for line in a:
    #     print(a.index(line) + 1, line)
