# 传入表达式保存到文件, 批改文件, 计算文件到答案
import os

# 文件保存位置
if not os.path.exists('../docs'):
    os.mkdir('../docs')


def save_exercise(sequence, title):
    exercise_file = '../docs/Exercises.txt'
    try:
        with open(exercise_file, 'a+', encoding='utf-8') as f:
            f.write(f'四则运算 题目{sequence}: {title}\n')
    except:
        print('Exercise.txt create failed. Please check again')


def save_answer(sequence, answer):
    answer_file = '../docs/Answer.txt'
    try:
        with open(answer_file, 'a+', encoding='utf-8') as f:
            f.write(f'答案{sequence}: {answer}\n')
        f.close()
    except:
        print('Answer.txt create failed. Please check again')


def inspect(correct_list, wrong_list):
    inspect_file = '../docs/Grade.txt'
    try:
        with open(inspect_file, 'a+', encoding='utf-8') as f:
            f.write(f'Correct: {len(correct_list)}({correct_list})\n'
                    f'Wrong: {len(wrong_list)}({wrong_list})\n')
            f.close()
    except:
        print('Grade.txt create failed. Please check again')


def calculate():
    pass


if __name__ == '__main__':
    inspect([1, 2, 3], [4, 5, 6])
