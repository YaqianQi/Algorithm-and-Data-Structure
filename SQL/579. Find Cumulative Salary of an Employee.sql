"""
input:
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 1  | 2     | 30     |
| 1  | 3     | 40     |
| 1  | 4     | 60     |

output: 
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |

way: 
| Id | A.Month | A.Salary|B.Month |B.Salary |
| 1  | 4     | 60     | | 3     | 40     | 
| 1  | 4     | 60     | | 2     | 30     | 
| 1  | 4     | 60     | | 1     | 20     | 
| 1  | 3     | 40     | | 2     | 30     |
| 1  | 3     | 40     | | 1     | 20     |
| 1  | 2     | 30     | | 1     | 20     |

"""


SELECT   A.Id, MAX(B.Month) as Month, SUM(B.Salary) as Salary
FROM     Employee A, Employee B
WHERE    A.Id = B.Id AND B.Month BETWEEN (A.Month-3) AND (A.Month-1)
GROUP BY A.Id, A.Month
ORDER BY Id, Month DESC