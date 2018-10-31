# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.
# Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
# Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.
# In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.
# Implement an efficient solution and analyze its time and space complexities.

# Examples:

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]

# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12
# Constraints:

# [time limit] 5000ms

# [input] array.array.integer slotsA

# 1 ≤ slotsA.length ≤ 100
# slotsA[i].length = 2
# [input] array.array.integer slotsB

# 1 ≤ slotsB.length ≤ 100
# slotsB[i].length = 2
# [input] integer

# [output] array.integer


def meeting_planner(slotsA, slotsB, dur):
  output = []

  availability = get_availability(slotsA, slotsB)
  max_time_available = availability[0]
  max_time_index_a = availability[1]
  max_time_index_b = availability[2]

  if max_time_available >= dur:
    output = get_time_slot(slotsA[max_time_index_a], slotsB[max_time_index_b], dur)

  return output

def get_availability(slots_a, slots_b):
  i = 0
  j = 0

  current_max = -1
  current_max_index_i = -1
  current_max_index_j = -1

  while i < len(slots_a) and j < len(slots_b):
    available = -1

    end_time_a = slots_a[i][1]
    start_time_a = slots_a[i][0]

    end_time_b = slots_b[j][1]
    start_time_b = slots_b[j][0]

    if (end_time_b >= end_time_a) and (start_time_b >= start_time_a):
      available = end_time_a - start_time_b
    elif (end_time_b < end_time_a) and (start_time_b >= start_time_a):
      available = end_time_b - start_time_b
    elif (end_time_b < end_time_a) and (start_time_b < start_time_a):
      available = end_time_b - start_time_a

    if available > 0:
      if available > current_max:
        current_max = available
        current_max_index_i = i
        current_max_index_j = j
      j += 1
    else:
      i += 1


  return [available, current_max_index_i, current_max_index_j]

def get_time_slot(slot_a, slot_b, dur):
  start_time = slot_a[0]
  if slot_b[0] - slot_a[0] > 0:
    start_time += (slot_b[0] - slot_a[0])

  end_time = start_time + dur

  return [start_time, end_time]

if __name__ == '__main__':
  example1_a = [[10,50],[60,120],[140,210]]
  example1_b = [[0,15],[60,70]]
  example1_dur = 8