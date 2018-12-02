# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.
#
# Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
#
# Each person's availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.
#
# In your implementation assume that the time slots in a person's availability are disjointed, i.e, time slots in a person's availability don't overlap. Further assume that the slots are sorted by slots' start time.
#
# Implement an efficient solution and analyze its time and space complexities.
#
# Examples:
#
# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]
#
# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.array.integer slotsA
#
# 1 <= slotsA.length <= 100
# slotsA[i].length = 2
# [input] array.array.integer slotsB
#
# 1 <= slotsB.length <= 100
# slotsB[i].length = 2
# [input] integer
#
# [output] array.integer

#======================================

# goal: given duration, find earliest time that works for both user A and B
#
#input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#        slotsB = [[0, 15], [60, 70]]
#        dur = 8
#output: [60, 68]
#
# input - array.array.integers (slotsA, slotsB), positive integer (duration)
# output - array of integer
#
# ===============================
#
#
#

def meeting_planner_old(slotsA, slotsB, dur):

  output = get_earliest_available_time(slotsA, slotsB, dur)

  return output

def get_earliest_available_time_old(slotsA, slotsB, dur):
  i = 0
  j = 0
  output = []

  # compute for the earliest time available
  while i < len(slotsA) and j < len(slotsB):
    time_available = min(slotsB[j][1], slotsA[i][1]) - max(slotsA[i][0], slotsB[j][0])
    # if found, comput the range that works for both
    if time_available >= dur:
      start_time = max(slotsA[i][0], slotsB[j][0])
      end_time = start_time + dur
      output = [start_time, end_time]
      return output

    if slotsB[j][0] - slotsA[i][1] > 0:
      i += 1
    else:
      j += 1

  return output

# ======================== Review 3 ======================

def meeting_planner(slotsA, slotsB, dur):
  idx_slot_a = 0
  idx_slot_b = 0
  length_slot_a = len(slotsA)
  length_slot_b = len(slotsB)

  while idx_slot_a < length_slot_a and idx_slot_b < length_slot_b:
    start_time = max(slotsA[idx_slot_a][0],slotsB[idx_slot_b][0])
    end_time = min(slotsA[idx_slot_a][1],slotsB[idx_slot_b][1])

    overlap = end_time - start_time

    if overlap >= dur:
      return [start_time, start_time + dur]

    if overlap < 0:
      idx_slot_a += 1
    else:
      idx_slot_b += 1

  return []
