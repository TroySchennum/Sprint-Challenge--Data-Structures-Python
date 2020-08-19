class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.index = 0

    def append(self, item):
        
        if self.index < self.capacity - 1:
            self.data[self.index] = item
            self.index += 1
        elif self.index == self.capacity - 1:
            self.data[self.index] = item
            self.index = 0

                #  if len(self.data) == self.capacity - 1:
                #     self.index + 1
        # for i in range(self.capacity):
        #     self.data.append(item)    
        # else:
        #     self.data.append(item)
        # if self.index == (self.capacity):
        #     self.index = 0
        #     self.data[self.index] = item
        # else:
        #     self.data.append(item)



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
    

if __name__ == "__main__":
    rb = RingBuffer(10)
    for i in range(11):
        rb.append(i)
    print(rb.get())