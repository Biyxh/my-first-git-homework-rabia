def threeNumberSum1(array, targetSum):
    ans = []
    for i in range(len(array) - 2):
        firstNum = array[i]
        for j in range(i+1, len(array) - 1):
            secondNum = array[j]
            for k in range(j+1, len(array)):
                thirdNum = array[k]
                if firstNum + secondNum + thirdNum == targetSum:
                    ans.append([firstNum, secondNum, thirdNum])
    return ans