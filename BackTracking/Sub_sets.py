def subset(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)

            path.pop()

    backtrack(0,[])

    return result

print(subset([2,3,4,5]))