'''
作者：wushenghao666
1、wordcloud库能有效剔除一些无效词，可视化表示
2、公式：(未用代码实现)
   same_words 为两篇文章单词出现次数前十中相同的有效词词数
   similarity = same_words / 10
   就是把一些介词、人称、连词等剔除掉
   建立一个集合不断试错完善
   像began，started极度相近的词合在一起计算
   还有单复数...
'''
import wordcloud,time

excludes = {'i','the','and','a','to','of','had','that','was',\
            'but','just','what','as','at','such','do','have','in',\
            'be','can','my',"don't",'only','how','why','with','they',\
            'some','few'}#"虚词"集

def fenge():#画分割线=-=
    print('{}'.format('分割线'.center(51,'=')))

def ciyun(a,txt):#生成词云
    w = wordcloud.WordCloud(width=1000,height=700,\
        background_color='white',max_words=15)
    w.generate(txt)
    if a==1:
        w.to_file('test1.png')
    if a==2:
        w.to_file('test2.png')

def getText(a):#读文件
    if a==1:
        txt = open('test1.txt','r').read()
        fenge()
        print('test1.txt的出现次数前10的词是：')
    if a==2:
        txt = open('test2.txt','r').read()
        fenge()
        print('test2.txt的出现次数前10的词是：')
        
    txt = txt.lower()#预处理：变成小写，把符号变成空格
    for ch in '!"#$%&()*+,-./:;<>=?@[\\]^_‘{}|~`':
        txt = txt.replace(ch,' ')
    return txt

def tongji(a,b=0):
    Txt = getText(a)
    
    if b==0: #词云只在第一次统计的时候生成
        ciyun(a,Txt)

    words = Txt.split()#统计词啦！
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1

    if b==1:#第二次统计剔除无效词
        for word in excludes:
            del counts[word]
            
    items = list(counts.items())#排序
    items.sort(key=lambda x:x[-1], reverse=True)
    
    for i in range(10):#输出
        word, count = items[i]
        print('{:<11}{:>5}'.format(word, count))
    
def introduction():#打印前言
    print('本程序可统计两篇文章中的出现次数前10的词及其相似度')
    print('执行本程序前，请先将你所需要的文件放在本文件的同一文件夹内')
    print('并命名为"test1.txt"和"test2.txt"，执行好了随便输入一个字符并摁回车')
    print('注：本程序只支持英文')
    input()

def ending():#打印后言
    time.sleep(3)
    print('O∩_∩O哈哈~')
    print('看词云图和剔除后统计文章的相似度应该一目了然了！')
    print('对于公式我就不用代码实现了')
    fenge()
    time.sleep(3)
    print('输入任意字符退出程序')
    input()
    
try:#主程序，第一次（全统计，生成词云）
    introduction()
    tongji(1)
    tongji(2)
    fenge()
    print('已在文件夹中生成两个词云图')
    
except:#异常处理
    print('请查看您的文件名有没弄错')
    print('程序6.6秒后退出')
    time.sleep(6.6)
    
else:#主程序，第二次（剔除无效词统计）
    print('是否剔除无效词在进行统计？是请输入"Y"，否请输入其他字符')
    y=input()
    if y in ['Y','y']:
        tongji(1,1)
        tongji(2,1)
        ending()
    else:
        print('输入任意字符退出程序')
        input()
