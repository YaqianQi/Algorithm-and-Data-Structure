class Solution:
    def accountsMerge(self, accounts):
        """ 
                0,1,2,3
        root = [1,1,2,3]
        
        "johnsmith@mail.com": 0
        "johnsmith@mail.com"
        p1 = 2
        p2 = 0
        p2 = p1 
        [["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]]
        """
        def find(roots, i):
            while i != roots[i]:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        
        
        n = len(accounts)
        roots = [0] * n
        for i in range(n):
            roots[i] = i
        from collections import defaultdict 
        d = defaultdict(int)
        for i in range(n):
            for j in range(len(accounts[i])):
                email = accounts[i][j]
                if email in d:
                    person = d[email]
                    p1 = find(roots, i)
                    p2 = find(roots, person)
                    if p1 != p2:
                        roots[p2] = p1
                else:
                    d[email] = i
                 
        users = defaultdict(list)
        for i, account in enumerate(accounts):
            parent = find(roots, i)
            emails = sorted(account[1:])
            lst = users[parent]
            lst.append(emails)
            users[parent] = lst
        print(users)
            
        res = []
        for user, emails in users.items():
            t = [user]
            for email in emails:
                t+= [email]
            res.append(t)
        return res
account =  [["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]]
print(Solution().accountsMerge(account))