# Let A[1::n] be an array of positive integers (A is not sorted).
# Pinocchio claims that there exists an O(n)-time algorithm that decides
# if there are two integers in A whose sum is 1000. Is Pinocchio right,
# or will his nose grow? If you say Pinocchio is right, explain how it can
# be done in O(n) time.

import random

n = 261
array = [i + random.randint(0, 1000) for i in range(n)]
random.shuffle(array)

hash_table = {}
halves = []
target_val = 1000

def order_of_1_operation_val_in_hash_map(val):
	try:
		hash_table[val]
		return True
	except:
		return False

for val in array:
	remaining_half = target_val - val

	if order_of_1_operation_val_in_hash_map(remaining_half):
		halves.append([val, remaining_half])
	
	hash_table[val] = val

for left, right in halves:
	print(f"Left: {left} Right: {right}")
	assert left + right == target_val
