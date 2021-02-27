import threading
from time import sleep

class Fork:
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.picked = 0

    def pick_up(self):
        self.lock.acquire()
        self.picked = 1

    def put_down(self):
        self.lock.release()
        self.picked = 0

    def is_picked(self):
        return self.picked


class Philosopher(threading.Thread):
    def __init__ (self, n, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.n = n
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.eating = 0

    def run(self):
        while True:       
            if forks[self.left_fork].n < forks[self.right_fork].n:
                forks[self.left_fork].pick_up()
                forks[self.right_fork].pick_up()
            else:
                forks[self.right_fork].pick_up()
                forks[self.left_fork].pick_up()
            self.eat()
            forks[self.right_fork].put_down()
            forks[self.left_fork].put_down()
            self.think()
            
    def eat(self):
        self.eating = 1

    def think(self):
        sleep(0)



philosopher_count = 5

forks = []

for i in range(philosopher_count):
    forks.append(Fork(i))

philosophers = []

for i in range(philosopher_count):
    philosophers.append(Philosopher(i, i, (i+1)%philosopher_count))

for p in philosophers:
    p.start()

iterations = 1

while True:
    sleep(1)
    print("breakfast", iterations)
    iterations += 1
    for p in philosophers:
        print(f"{p.n + 1} - {p.eating}")
