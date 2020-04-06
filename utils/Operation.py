# OS操作, 传入表达式/答案/正确率保存到文件
import os
import time

# 文件保存位置
if not os.path.exists('./docs'):
    os.mkdir('./docs')


# 保存题目 传入序列号以及题目
def save_exercise(expressions_list):
    exercise_file = './docs/Exercises.txt'
    try:
        with open(exercise_file, 'w+', encoding='utf-8') as f:
            for line in expressions_list:
                f.write('{}\n'.format(line))
        f.close()
    except IOError:
        print('Exercise.txt create failed. Please check again')


# 保存答案 传入序列号以及答案
def save_answer(answers_list):
    answer_file = './docs/Answer.txt'
    try:
        with open(answer_file, 'w+', encoding='utf-8') as f:
            for line in answers_list:
                f.write('{}\n'.format(line))
    except IOError:
        print('Answer.txt create failed. Please check again')


# 保存比较结果 传入正确列表以及错误列表
def save_inspect(correct_list, wrong_list):
    inspect_file = './docs/Grade.txt'
    try:
        with open(inspect_file, 'w+', encoding='utf-8') as f:
            f.write(f'Correct: {len(correct_list)}{correct_list}\n'
                    f'Wrong: {len(wrong_list)}{wrong_list}\n'
                    f'Accuracy: {round(len(correct_list)/len(wrong_list), 4) * 100}%\n')
    except IOError:
        print('Grade.txt create failed. Please check again')


if __name__ == '__main__':
    save_exercise(['1+1', '2+3'])
