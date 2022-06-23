import random,re,threading
print2=print
from rich import print
f=open("wordle-answers-alphabetical.txt",'r')
words=[i.replace('\n','') for i in f.readlines()]
esc=chr(0x1B)

f.close()
def wordly(starters=('plate','plate','plate','plate','anime','alert','alert')):
    
    mat=[0,0,0,0,0]
    #0 no info 1 character in answer 2 character at richt place
    secret=random.choice(words)
    odp=random.choice(starters)
    pos=[i for i in 'qwertyuiopasdfghjklzxcvbnm']
    commonN={'t':'h','e':'r','o':'n','a':'n'}
    commonB={'h':'t','r':'e','n':'o','n':'a'}
    
    posytionTrysF={
        0:{i:x for i,x in map(lambda x: [x,False],"qwertyuiopasdfghjklzxcvbnm")},
        1:{i:x for i,x in map(lambda x: [x,False],"qwertyuiopasdfghjklzxcvbnm")},
        2:{i:x for i,x in map(lambda x: [x,False],"qwertyuiopasdfghjklzxcvbnm")},
        3:{i:x for i,x in map(lambda x: [x,False],"qwertyuiopasdfghjklzxcvbnm")},
        4:{i:x for i,x in map(lambda x: [x,False],"qwertyuiopasdfghjklzxcvbnm")}
    }
    posytionTrys={0:[*pos],1:[*pos],2:[*pos],3:[*pos],4:[*pos]}
    posytionTrysF[0]['x']=True
    possible_s=[i for i in 'eyouai']
    nexter={
        0:[0,0],
        1:[0,0],
        2:[0,0],
        3:[0,0],
        4:[0,0]
    }

    def generate_answer(last,mat):
        c=0
        for i in last:
            if mat[c]==2:
                posytionTrys[c]=[i]
                if i=='q':
                    try:
                        posytionTrys[c+1].remove('e')
                        posytionTrys[c+1].remove('u')
                        posytionTrys[c+1].remove('i')
                    except:
                        pass

                if (i in commonN) and (c!=4):
                    if posytionTrysF[c+1][commonN[i]]==False:
                        posytionTrys[c+1].append(commonN[i])
                        
                if (i in commonB) and (c!=0):
                    if posytionTrysF[c-1][commonB[i]]==False:
                        posytionTrys[c-1].append(commonB[i])
                elif (i in 'setf') and (c!=4):
                    if posytionTrysF[c+1][i]==False:
                        posytionTrys[c+1].append(i)
                elif (i in 'setf') and (c!=0):
                    if posytionTrysF[c-1][i]==False:
                        posytionTrys[c-1].append(i)
            if mat[c]==1:
                posytionTrysF[c][i]=True
                while True:
                    try:
                        posytionTrys[c].remove(i)
                            
                    except:
                        break
            if mat[c]==0:
                if i in possible_s:
                    possible_s.remove(i)
                for j in range(5):
                    while True:
                        try:
                            posytionTrys[j].remove(i)
                        except:
                            break
                    posytionTrysF[j][i]=True
            c+=1
        f=[]
        for j in range(5):
            f.append("("+"["+"".join([i for i in posytionTrys[j]])+"]"+")")
 
        t=re.compile(r"("+r"".join(f)+")")
        posible=[]
        if any((match := t.match(x)) for x in words):
            posible.append(match.group(0))
        """        moslikly=[{}for i in range(5)]
        for i in posible:
            for j in range(5):
                moslikly[j][i[j]]+=1"""
        

        try:
            return random.choice(posible)
        except:
            return random.choice(words)

    l=0
    for i in range(6):
        while len(odp)!=5:
            odp=generate_answer(*y)
            #print()
            #print2(f'{esc}[1A\r',end='')
        c=0
        o=odp
        for j in o:
            if j in secret:
                mat[c]=1
            if secret[c]==o[c]:
                mat[c]=2
            c+=1
        c=0
        string=""
        for j in mat:
            if mat[c]==0:
                string+=o[c]
            if mat[c]==1:
                string+=f"[rgb(255,255,0)]"+o[c]+f'[/]'
            if mat[c]==2:
                string+=f"[green]"+o[c]+f'[/]'
            c+=1
        if mat==[2,2,2,2,2]:
            #print("[bold]"+secret+"[/]")
            #print('you win!  '+str(l))
            if l<=5:
                return True
            else:
                return False
        #print(string)
        y=[odp,mat]
        mat=[0,0,0,0,0]
        odp=''
        l+=1
wins={}
def do_w(starter,c):
    county=0
    for i in range(c):
        if wordly(starter)==True:
            county+=1
    wins[starter]=county
    return county,starter

county=0
prob=100


"""for index in range(30):
    th=[threading.Thread(target=do_w,args=[words[index*77+i],100]) for i in range(77)]
    [i.start() for i in th]
    o=0
    for i in th:
        i.join()
        print(f'left:{2310-len(wins.keys())}')
        o+=1

    
top3s=['','','']
top3=[0,0,0]
for i in wins:
    if top3[0]<wins[i]:
        top3[2]=top3[1]
        top3s[2]=top3s[1]
        top3[1]=top3[0]
        top3s[1]=top3s[0]
        top3[0]=wins[i]
        top3s[0]=i
print(top3s)"""
starterss=['plate', 'anime', 'alert']
"""for i in range(3):
    do_w(starterss[i],10_000)
print(wins)"""
c=0
for i in range(10_00):
    if wordly():
        c+=1
print(c/10_00)


