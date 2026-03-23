from text import line, title
from menu import Menu

class Order:
    def __init__(self, menulist):
        self.menulist = menulist
        self.ordercount = [0] * len(self.menulist)

    def orderadd(self):
        while True:
            Menu().menuprint()
            line()
            title()
            print('*주문추가*')
            line()
            name = input('주문할 메뉴명을 입력해주세요(x입력시 주문추가 종료) : ')
            if name=='x' : 
                print('주문 추가를 종료합니다.')
                break
            ch = False
            for i, x in enumerate(self.menulist):
                if x['name'] == name:
                    while True:
                        cnt = input('주문 수량을 입력해주세요 : ')
                        try:
                            cnt = int(cnt)
                            break
                        except ValueError:
                            print('수량을 잘못 입력하셨습니다. 다시 입력해주세요.')
                    self.ordercount[i] = cnt
                    ch=True
                    break
            if not ch : 
                print('해당 메뉴는 없습니다. 다시 입력해주세요.')
        

    def orderclear(self):
        line()
        print('*주문 내역')
        line()
        for i in range(len(self.ordercount)):
            if self.ordercount[i] > 0 :
                print(f'{i+1}. {self.menulist[i]['name']} : {self.ordercount[i]}개')
        while True:
            line()
            while True:
                num = input('주문을 취소할 메뉴 번호를 입력해주세요 (x입력시 취소 종료) : ')
                if num == 'x':
                    print('주문 취소를 종료합니다.')
                    break
                try :
                    num = int(num)-1
                    break
                except ValueError:
                    print('번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
            if num == 'x' :
                break
            elif self.ordercount[num] <= 0 :
                print('해당 메뉴는 주문을 하지 않았습니다.')
            elif num >= len(self.ordercount) :
                print('해당 메뉴는 없습니다.')
            else:
                self.ordercount[num] = 0
                print('해당 주문이 취소되었습니다.')

    def orderprint(self):
        line()
        print('*주문 내역')
        line()
        total = 0
        for i, x in enumerate(self.menulist):
            if self.ordercount[i] > 0:
                print(f'{x['name']} : {x['price']}원      ...{self.ordercount[i]}개')
                total += x['price'] * self.ordercount[i]
        line()
        print('                           총 금액    :  ',total,'원')

    def orderend(self):
        mobilenum = input('모바일 번호를 입력해주세요(-빼고입력해주세요.) : 010')
        self.orderprint()
        line()
        print('주문이 처리되었습니다.')
        line()
        f=open('cafe/sales.txt', 'a')
        for i, x in enumerate(self.menulist) :
            if self.ordercount[i]>0 :
                x['cnt'] += self.ordercount[i]
                self.ordercount[i] = 0
                f.write(f'{mobilenum},{x['name']},{x['price']},{x['cnt']}\n')
        f.close()

    def order(self):
        while True:
            line()
            title()
            print('*주문관리*')
            line()
            print('c : 주문 추가')
            print('d : 주문 취소')
            print('p : 주문 확인')
            print('e : 주문 완료')
            print('x : 종료')
            line()
            ans = input('작업선택 : ')
            if ans == 'c':
                self.orderadd()
            elif ans == 'd':
                self.orderclear()
            elif ans == 'p':
                self.orderprint()
            elif ans == 'e':
                self.orderend()
            elif ans == 'x':
                print("주문관리 종료.")
                break
            else :
                print('잘못입력하셨습니다. 다시 입력해주세요.')
            line()
        return