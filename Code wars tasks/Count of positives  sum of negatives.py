def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    elif arr == [0]:
        return 0
    pros = 0
    cons = 0
    for x in arr:
      if x > 0:
          pros += 1
      if x < 0:
          cons += x
    return [pros, cons]