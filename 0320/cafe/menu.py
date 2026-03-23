from text import line, title

class Menu:
    def __init__(self):
        self.menulist = list()
    #메뉴 저장하기
    def menuadd(self):
        while True:
            line()
            title()
            print('*메뉴 추가*')
            name = input('메뉴명을 입력하세요(X/x입력시 메뉴추가 종료) : ')
            line()
            if name == 'x' or name == 'X':
                print('메뉴추가를 종료합니다.')
                self.saveprint()
                break
            while True :
                price = input('가격을 입력하세요 : ')
                try:
                    price = int(price)
                    break
                except ValueError:
                    print('잘못 입력하셨습니다. 다시 입력해주세요.')
            newmenu = {
                'name' : name,
                'price' : price,
                'cnt' : 0
            }
            self.menulist.append(newmenu)
            print(f'{name} : {price} 메뉴를 추가했습니다.')

    #메뉴 수정하기
    def menuupdate(self):
        while True:
            line()
            title()
            print('*메뉴수정*')
            line()
            if len(self.menulist) == 0 :
                print('수정할 메뉴가 없어 메뉴수정을 종료합니다.')
                break
            num = input('메뉴 번호를 입력해주세요(X/x입력시 메뉴수정 종료) : ')
            line()
            if num == 'x' or num == 'X':
                print('메뉴수정을 종료합니다.')
                break
            try :
                num = int(num)-1
            except ValueError:
                print('메뉴 번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
                continue

            if len(self.menulist)<num :
                print('해당 메뉴는 없습니다. 다시 입력해주세요.')
                continue
            else:
                remenu = self.menulist[num]
                print(f'{num+1} : {remenu['name']} : {remenu['price']}원')
                rename = remenu['name']
                reprice = remenu['price']
                yn = input('메뉴명을 바꾸시겠습니까?(y/n) : ')
                if yn == 'y':
                    rename = input('메뉴명을 입력하세요 : ')
                yn = input('가격을 바꾸시겠습니까?(y/n) : ')
                if yn == 'y':
                    reprice = int(input('가격을 입력하세요 : '))
                remenu ={
                    'name' : rename,
                    'price' : reprice,
                    'cnt' : 0
                }
                self.menulist[num] = remenu
                line()
                print(f'{remenu['name']} : {remenu['price']}원')
                print('수정이 완료되었습니다!')
                line()
    
    #메뉴 삭제하기
    def menudel(self):
        while True:
            self.menuprint()
            line()
            title()
            print('*메뉴삭제*')
            line()
            if len(self.menulist) == 0 :
                print('삭제할 메뉴가 없어 메뉴삭제를 종료합니다.')
                break
            num = input('메뉴 번호를 입력해주세요(X/x입력시 메뉴삭제 종료) : ')
            line()
            if num == 'x' or num == 'X':
                print('메뉴삭제를 종료합니다.')
                self.saveprint()
                break
            try :
                num = int(num)-1
            except ValueError:
                print('메뉴 번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
                continue
            if len(self.menulist)<num or num<=0 :
                print('해당 메뉴는 없습니다. 다시 입력해주세요.')
                continue
            del self.menulist[num]
            print('해당 메뉴를 삭제했습니다.')
            self.saveprint()
            
    #메뉴 출력하기
    def menuprint(self):
        self.menulist = self.menucall()
        line()
        title()
        print('*메뉴출력*')
        line()
        for i, x in enumerate(self.menulist):
            print(f'{i+1}. {x['name']} : {x['price']}원')

    #파일에서 메뉴 불러오기
    def menucall(self) :
        menulist = list()
        f = open("cafe/menu.txt", "r")
        lis = f.readlines()
        for li in lis :
            liar = li.split(',')
            savmenu = {
                'name' : liar[0],
                'price' : int(liar[1]),
                'cnt' : int(liar[2])
            }
            menulist.append(savmenu)
        f.close()
        return menulist
    
    #메뉴 저장
    def menusave(self):
        f = open("cafe/menu.txt", 'w')
        for x in self.menulist:
            res = x['name']+','+str(x['price'])+','+str(x['cnt'])+'\n'
            # print(res)
            f.write(res)
        f.close()

    #저장하고 출력
    def saveprint(self):
        self.menusave()
        self.menuprint()

    def menu(self):
        #global menulist
        self.menulist = self.menucall()
        while True:
            line()
            title()
            print('*메뉴관리*')
            line()
            print('C/c 메뉴추가')
            print('U/u 메뉴수정')
            print('D/d 메뉴삭제')
            print('P/p 메뉴출력')
            print('X/x 메뉴관리종료')
            line()
            a= input('작업선택 : ')
            line()
            if a=='C' or a=='c':
                self.menuadd()
            elif a=='U' or a=='u':
                self.menuprint()
                self.menuupdate()
                self.saveprint()
            elif a=='D' or a=='d':
                self.menudel()
            elif a=='P' or a=='p':
                self.menuprint()
            elif a=='X' or a=='x':
                print('메뉴관리 종료.')
                self.menusave()
                break
            else :
                print('잘못입력하셨습니다. 다시 입력해주세요.')
            line()
        return