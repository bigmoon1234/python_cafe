from text import line
from text import title
from menu import Menu
from order import Order
from sales import Sales

menu = Menu()
order = Order(menu.menucall())
sales = Sales()

while True :
    line()
    title()
    print('*작업관리*')
    line()
    print('M/m : 메뉴관리')
    print('O/o : 주문관리')
    print('S/s : 매출확인')
    print('X/x : 프로그램 종료')
    line()
    ans = input('작업 선택 : ')
    line()
    if ans=='M' or ans=='m' :
        menu.menu()
        pass
    elif ans=='O' or ans=='o' :
        order.order()
        pass
    elif ans=='S' or ans=='s' :
        sales.salescall()
    elif ans=='x' or ans=='X' :
        print('프로그램 종료')
        break
    else:
        print('잘못입력하셨습니다. 다시 입력해주세요.')
    line()
line()