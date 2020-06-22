from collections import defaultdict
import bisect
# binary search 
class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        value_lst = self.dic[key]
        if not value_lst:
            return ""
        i = bisect.bisect(value_lst, (timestamp, chr(123)))
        return value_lst[i-1][-1] if i else ""

if __name__ == "__main__":
    inputs1 = ["TimeMap","set","get","get","set","get","get"]
    inputs2 = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    
    #Output: [null,null,"bar","bar",null,"bar2","bar2"]
    kv = TimeMap()
    kv.set("foo", "bar", 1)   
    print(kv.get("foo", 1))
    print(kv.get("foo", 3))
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))
    print( kv.get("foo", 5))
    
    """
    input1 = ["TimeMap","set","set","get","get","get","get","get"]
    input2 = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

    kv = TimeMap()
    kv.set("love","high",10)   
    kv.set("love","low",20) 
    print(kv.get("love",5))
    print(kv.get("love",10))
    print(kv.get("love",15))
    print(kv.get("love",20))
    print(kv.get("love",25))
    #kv.set("foo", "bar2", 4)
    #print(kv.get("foo", 4))
    #print( kv.get("foo", 5))
    #["TimeMap","set","get","get","set","get","get"]
    #[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]"""
