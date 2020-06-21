class BrowserHistory:
    
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.path = [""] * 100  
        self.path[0] = homepage
        self.cur = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.cur += 1
        self.path[self.cur] = url
        t = self.path[:self.cur+1]
        self.path = t + [""] * (100 - self.cur)
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.cur = self.cur - steps
        if self.cur < 0:
            return self.path[0]
        return self.path[self.cur]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        if self.cur+steps <= len(self.path) and self.path[self.cur+steps]!="":
            self.cur += steps
            if self.cur > len(self.path):
                return None
            return self.path[self.cur]

if __name__ == "__main__":
    #BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    #browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
    #browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
    #browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
    #browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    #browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
    #browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
    #browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
    #browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
    #browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    #browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

    # "leetcode.com" -> "google.com" -> "facebook.com" ->"youtube.com"
    #                                                  -> "linkedin.com"
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    print(browserHistory.path, browserHistory.cur)
    print(browserHistory.back(1)) # "facebook.com"
    print(browserHistory.back(1)) # return "google.com"
    print(browserHistory.forward(1))   # "facebook.com"
    browserHistory.visit("linkedin.com")
    print(browserHistory.forward(2)) # "linkedin.com"
    print(browserHistory.back(2)) # "google.com"
    print(browserHistory.back(7))# leetcode.com """
    print(browserHistory.path, browserHistory.cur)
    #["BrowserHistory","visit",      "visit",           "visit",     "back","back","forward",  "visit",   "forward","back","back"]
    #[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],  [1],    [1],   ["linkedin.com"], [2],   [2],   [7]]

    #[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]


    ["BrowserHistory","visit", "back",  "back",  "forward",  "forward",  "visit","visit",   "back"]
    [["zav.com"],["kni.com"], [7],    [7],       [5],        [1]  ,  ["pwrrbnw.com"],["mosohif.com"],[9]]

    [null,null,           "zav.com","zav.com",  "kni.com",   "kni.com",             null,null,    "zav.com"]

    [null,null             ,"zav.com","zav.com","","",null,null,"zav.com"]
