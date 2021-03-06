# Busiest Time in The Mall
# The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You're given data extracted from the mall's door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here's an example of a data point: [ 1440084737, 4, 0 ].
#
# Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
#
# Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.
#
# Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  data = [ [1487799425, 14, 1],
#                  [1487799425, 4,  0],
#                  [1487799425, 2,  0],
#                  [1487800378, 10, 1],
#                  [1487801478, 18, 0],
#                  [1487801478, 18, 1],
#                  [1487901013, 1,  0],
#                  [1487901211, 7,  1],
#                  [1487901211, 7,  0] ]
#
# output: 1487800378 # since the increase in the number of people
#                    # in the mall is the highest at that point
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.array.integer data
#
# 1 <= data.length <= 100
# [output] integer

# solution from review #2
def find_busiest_period(data):
  current_best_num_people = 0
  current_best_epoch = 0

  current_num_people = 0
  for idx, element in enumerate(data):
    if element[2] == 0:
      current_num_people -= element[1]
    else:
      current_num_people += element[1]

    if is_at_the_end_of_epoch(data,idx):
      if current_best_num_people < current_num_people:
        current_best_num_people = current_num_people
        current_best_epoch = element[0]
  return current_best_epoch

def is_at_the_end_of_epoch(data,idx):
  try:
    if data[idx+1][0] == data[idx][0]:
      return False
    return True
  except:
    return True
# =====================================
# def find_busiest_period_review(data):
#   current_best_epoch = 0
#   current_best_visitors = 0

#   temp_epoch = 0
#   temp_visitors = 0
#   for index, item in enumerate(data):
#     if not temp_epoch == item[0]:
#       if temp_visitors > current_best_visitors:
#         current_best_visitors = temp_visitors
#         current_best_epoch = temp_epoch
#       temp_epoch = item[0]

#     if item[2] == 1:
#       temp_visitors += item[1]
#     else:
#       temp_visitors -= item[1]

#   if temp_visitors > current_best_visitors:
#     current_best_visitors = temp_visitors
#     current_best_epoch = temp_epoch

#   return current_best_epoch

if __name__ == '__main__':
  data = [ [1487799425, 14, 1],
          [1487800378, 10, 1]]

  print(find_busiest_period(data))