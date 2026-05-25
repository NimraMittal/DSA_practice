class solution:
    def beautifulSubsets(self,nums,k):
        self.count = 0
        def backtrack(index,path):
            if len(path) >0:
                self.count += 1

                for i in range(index,len(nums)):
                    valid = True
                    for num in path:
                        if abs(num - nums[i]) == k:
                            valid = False
                            break
                    if valid:
                        path.append(nums[i])
                        backtrack(i+1, path)
                        path.pop()
            
        backtrack(0,[])
        return self.count