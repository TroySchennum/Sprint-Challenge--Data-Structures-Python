class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        i= 0
        self.index = i:i+2
    def append(self, item):
        if len(self.data) == self.capacity:
            
            self.data[self.index] = item
        else:
            self.data.append(item)



        # how to change index value in a list
        # increment_address_one = (address + 1) % Length   
        # self.storage.append(item)
        # self.size += 1
        

        # if self.storage == (self.capacity - 1):
        #     self.size -= 1
        #     self.storage.pop()
            

    def get(self):
        # return self.storage
        return self.data
    