import random
import csv
import time

# data = csv.reader(open('guessword.csv',encoding='utf-8'))
# ans = csv.reader(open('guesswordanswer.csv',encoding='utf-8'))

# for i in data:
#     print(i)
# print(data)
# question = data[[1]]
# print(question)
def guessword():
    cd = input('按任意键开始，输入‘q’退出')
    while(cd !='q'):
        run()
        cd = input('输入任意键开始，输入‘q’退出')
    print("bye~")

def run():
    
    id = random.randint(1,500)
    answer = input(getquestion(id))
    truth = getanswer(id)
    if(answer == truth):
        print('恭喜回答正确\n')
    else:
        print('回答错误，正确答案时：' + truth+'\n')

def getquestion(id):
    cnt = 1
    with open('../resource/guessword.csv',encoding='utf-8') as csvfile :
        data = csv.reader(csvfile)
        for i in (data):
            if(cnt == id):
                return i[1]
            cnt+=1
    return "没有找到"+str(id)
    
def getanswer(id):
    cnt = 1
    with open('../resource/guesswordanswer.csv',encoding='utf-8') as csfile :
        ans = csv.reader(csfile)
        for i in ans:
            if(cnt == id):
                return i[1]
            cnt+=1
    return "没有找到"+str(id)
    
# print(time.time())
random.seed(time.time())
guessword()