from text import line

class Sales:
    def salescall(self):
        totallist = list()
        f=open('cafe/sales.txt','r')
        lis = f.readlines()
        for li in lis :
            liar = li.split(',')
            savesale ={
                'mobile' : liar[0],
                'name' : liar[1],
                'price' : int(liar[2]),
                'cnt' : int(liar[3])
            }
            totallist.append(savesale)
        f.close()
        self.salesprint(totallist)

    def salesprint(self, ltotal):
        line()
        total = 0
        for i, x in enumerate(ltotal):
            sum = x['price'] * x['cnt']
            mobile = '*'*4+'-'+x['mobile'][4:]
            print(f'{mobile} : {x['name']}  {x['price']}원 {x['cnt']}개        ...{sum}원')
            total += sum
        line()
        print('총 매출  ',total,'원')