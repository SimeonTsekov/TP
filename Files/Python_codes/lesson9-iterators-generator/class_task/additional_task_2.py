class Building:

    def __init__(self, floor_break):
        self.floor_break = floor_break
        self.floors = 100
        self.floor_current = 0
        self.interval = 14
   
    def breaks(self):
        if(self.floor_current >= self.floor_break):
            return 1
        else:
            return 0

    def break_1(self):      
        if(self.breaks()):
            print("The first egg broke on floor ", self.floor_current)
            if(self.floor_current < 13):
                self.floor_current = 0
            else:
                self.floor_current -= (self.interval-1)
            self.interval = 1
            return self.floor_current
        
        else:
            print("The first egg didn\'t break on floor ", self.floor_current)
            if(self.floor_current > 96):
                self.floor_current = 100
            else:
                self.floor_current += self.interval
                self.interval -= 1
            self.break_1()

    def break_2(self):
        if(not(self.breaks())):
            print("The second egg didn\'t break on floor ", self.floor_current)
            self.floor_current += self.interval
            self.break_2()
        
        else:
            print("The floor, on which the egg brakes is ", self.floor_current)
            return self.floor_current

break_floor = int(input("Enter break floor (it must be a number): "))

while(break_floor < 0 or break_floor > 100):
    break_floor = int(input("Enter break floor (it must be a number): "))

building = Building(break_floor)
building.break_1()
building.break_2()
