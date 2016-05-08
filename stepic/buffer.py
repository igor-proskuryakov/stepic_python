class Buffer:

    def __init__(self):
        self.nums=[]
        self.l = 0

    def add(self, *a):
        self.sum = 0
        for i in a:
            self.nums.append(i)
            self.l+=1
            if self.l == 5:
                for j in self.nums:
                    self.sum +=j
                print(self.sum)
                self.sum=0
                self.l=0
                self.nums=[]
    def get_current_part(self):
        return self.nums
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]