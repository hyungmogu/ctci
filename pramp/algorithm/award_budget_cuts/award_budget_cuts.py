# Award Budget Cuts
# The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they're facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they'd like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won't be impacted.
#
# Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).
#
# Analyze the time and space complexities of your solution.
#
# Example:
#
# input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
#
# output: 47 # and given this cap the new grants array would be
#            # [2, 47, 47, 47, 47]. Notice that the sum of the
#            # new grants is indeed 190
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.double grantsArray
#
# 0 <= grantsArray.length <= 20
# 0 <= grantsArray[i]
# [input] double newBudget
#
# [output] double

#================ From Mock Interview =====================

def find_grants_cap(grantsArray, newBudget):

  total_count = len(grantsArray)
  count_below_cutline = 0
  sum_budgets_below_cutline = 0

  cutline = newBudget / float(total_count)

  temp_set = set([])

  # check and see which is below the cutline
  while there_is_a_budget_below_cutline(grantsArray , cutline, temp_set):
    for budget in grantsArray:
      if budget <= cutline and budget not in temp_set:
        sum_budgets_below_cutline += budget
        count_below_cutline += 1
        temp_set.add(budget)

        cutline = (newBudget - sum_budgets_below_cutline) / float(total_count - count_below_cutline)

  return cutline

def there_is_a_budget_below_cutline(grantsArray, cutline, temp_set):
  for budget in grantsArray:
    if budget <= cutline and budget not in temp_set:
      return True
  return False

  # =============== From Review =========================

def find_grants_cap_improved(grantsArray, newBudget):

  total_count = len(grantsArray)
  count_below_cutline = 0
  sum_budgets_below_cutline = 0

  cutline = newBudget / float(total_count)

  temp_set = set([])

  grantsArray = sorted(grantsArray)

  # check and see which is below the cutline
  for budget in grantsArray:
    if budget <= cutline:
      sum_budgets_below_cutline += budget
      count_below_cutline += 1

      cutline = (newBudget - sum_budgets_below_cutline) / float(total_count - count_below_cutline)

  return cutline

#=============== From Review 2 ==================

def find_grants_cap(grantsArray, newBudget):
  if len(grantsArray) == 0 or len(grantsArray) == 1:
    return newBudget

  grantsArray = sorted(grantsArray)

  cutline = newBudget / float(len(grantsArray))

  cnt_grant_below_cap = 0
  for grant in grantsArray:
    if grant < cutline:
      newBudget -= grant
      cnt_grant_below_cap += 1
      cutline = newBudget / float(len(grantsArray) - cnt_grant_below_cap)
    else:
      break

  return cutline

if __name__ == '__main__':
  grantsArray = [2]
  newBudget = 190
  print(find_grants_cap(grantsArray, newBudget))
