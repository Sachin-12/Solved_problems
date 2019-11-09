class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:

    def getImportance(self,employees, id):
        map_ = {}
        for em in employees:
            map_[em.id] = em
        return self.dfs(map_, id)
    
    def dfs( self,map_, id):
        sum = map_[id].importance
        for sub_id in map_[id].subordinates:
            sum += self.dfs(map_, sub_id)
        return sum

emp_info = Employee
Array=[emp_info(1,5,[2,3])]
Array.append(emp_info(2,3,[]))
Array.append(emp_info(3, 3, []))
# print(Array)
sol = Solution()
res = sol.getImportance(Array,1)
print(res)



