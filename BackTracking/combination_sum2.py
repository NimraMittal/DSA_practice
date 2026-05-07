def combination_sum(candidates, target):
    res = []
    candidates.sort()
    def backtrack(start, path, csum):
        if csum == target:
            res.append(path[:])
            return
        if csum > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i+1, path, csum+candidates[i])
            path.pop()
        
    backtrack(0,[],0)
    return res
    
print(combination_sum([1,2,3,1,2,4,4,2], 7))
# [1,1,2,2,2,3,4,4]