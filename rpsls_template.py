#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��μ�ܲ
���ڣ�2022/5/12
"""

import random
def name_to_number (name):
     if name == 'rock':
         return 0
     elif name=='spock':
         return 1
     elif name=='paper':
         return 2
     elif name=='lizard':
          return 3
     elif name=='scissors':
          return 4
     else:
         print('Error:No Correct Name')

def number_to_name(number):
    if number in range(0,5):
        if number==0:
             return'rock'
        elif number==1:
             return'spock'
        elif number==2:
             return'paper'
        elif number==3:
             return'lizard'
        elif number==4:
             return'scissors'
        else:
            print('please input number n the range 0 to 4')

def rpsls(player_choice):
    print()
    print('�����ѡ��',player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print('����ѡ�����',comp_choice)
    if player_number-comp_number in range(-4,-2)or range(1,3):
        print('��һ�ʤ')
    elif player_number-comp_number in range(-2,0)or range(3,5):
        print('������ʤ')
    elif player_number-comp_number==0:
        print('ƽ��')
    else:
        print('error!')

print('"��Ϸ��ʼ"')
rpsls("rock")
rpsls("spock")
rpsls("paper")