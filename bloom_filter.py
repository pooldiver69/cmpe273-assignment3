import math 
from hashlib import md5

class BloomFilter(object): 
  
    def __init__(self, count,fp_prob): 
      # m = -(n * lg(p)) / (lg(2)^2) 
      self.size = int(-(count * math.log(fp_prob))/(math.log(2)**2))
      # k = (m/n) * lg(2) 
      self.hash_count = int((self.size/count) * math.log(2))    
      self.bit_array = [0 for _ in range(self.size)]
  
    def add(self, item): 
      digests = [] 
      for i in range(self.hash_count): 
        key = int(md5(item.encode()).hexdigest(), 16)
        # print(key)
        digest =  key % self.size 
        digests.append(digest) 
        # print(digest)
        self.bit_array[digest] = 1
  
    def is_member(self, item): 
      for i in range(self.hash_count): 
        key = int(md5(item.encode()).hexdigest(), 16)
        digest =  key % self.size 
        if self.bit_array[digest] == 0: 
          return False
      return True