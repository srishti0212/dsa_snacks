def two_sum(arr, target):
    # for i in range(0,len(arr)):
    #     for j in range(i, len(arr)):
    #         if arr[i] + arr[j] == target:
    #            print(arr[i], arr[j])
    map = {}
    for i in range(0, len(arr) - 1):
        map[1] = 'hello'
        print(map[1])
        if 1 in map:
            print('found it')
        complement = target - arr[i]
        if complement in map:
            print(arr[i], complement)
        else:
            map[complement] = i
            



two_sum([1,2,3,4,5,6,7], 7)

