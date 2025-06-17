def solution(num, total):
  
    # x, x+1, x+2, ... x+num-1 ---> (num)개 합 = total
    # num/2 * (2*x + (num-1)) = total
    # 2*total = num * (2*x + (num-1))
    # 2*x + (num-1) = 2*total/num
    # x = (2*total/num - num + 1)/2
    
    start = (2*total/num - num + 1)/2
    return [start + i for i in range(num)]
