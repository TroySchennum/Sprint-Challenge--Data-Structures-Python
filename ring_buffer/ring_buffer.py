class RingBuffer:
    def __init__(self, capacity):
        # self.storage = []
        # self.size = 0
        self.capacity = capacity
        
        self.data = []

    def append(self, item):
        
        self.data.append(item)
        if len(self.data) == (self.capacity + 1):
            self.data.pop(0)
        # increment_address_one = (address + 1) % Length   
        # self.storage.append(item)
        # self.size += 1
        

        # if self.storage == (self.capacity - 1):
        #     self.size -= 1
        #     self.storage.pop()
            

    def get(self):
        # return self.storage
        return self.data
    