class Jar:
    def init(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity
        self._size = 0

    def str(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        if self._size + n > self._capacity:
            raise ValueError("Jar is full")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        if n > self._size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size