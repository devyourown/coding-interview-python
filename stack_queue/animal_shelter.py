import time
from collections import deque

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.dog_q = deque()
        self.cat_q = deque()
        self.time_log = {}

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_q.append(animal)
        elif isinstance(animal, Cat):
            self.cat_q.append(animal)
        self.time_log[animal] = time.time()

    def dequeue_any(self):
        if not self.dog_q or not self.cat_q:
            if self.dog_q:
                return self.dog_q.popleft()
            if self.cat_q:
                return self.cat_q.popleft()
            raise Exception('Empty Queue')
        if self.time_log[self.dog_q[0]] < self.time_log[self.cat_q[0]]:
            return self.dog_q.popleft()
        return self.cat_q.popleft()

    def dequeue_dog(self):
        if not self.dog_q:
            raise Exception('Empty Queue')
        del self.time_log[self.dog_q[0]]
        return self.dog_q.popleft()

    def dequeue_cat(self):
        if not self.cat_q:
            raise Exception('Empty Queue')
        del self.time_log[self.cat_q[0]]
        return self.cat_q.popleft()