class Jar:
    n=0
    def __init__(self,capacity=12):
        if capacity<=0:
            raise ValueError("Invalid")
        self.capacity=capacity


    def __str__(self):
        cookie="🍪"
        return f"{cookie*self.n}"

    def deposit(self, n):
        if self.capacity>=self.n + n:
            self.n=self.n + n
        else:
            raise ValueError("Invalid")

    def withdraw(self, n):
        if self.n<n:
            raise ValueError("Nom nom nom")
        self.n-=n

    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self,capacity):
        self._capacity=capacity
    @property
    def size(self):
        return self.n

