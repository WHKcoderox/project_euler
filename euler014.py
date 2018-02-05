collatz_lengths = {'1':1} # store lengths of previously calculated values in a hashtable
# since 1 is the finish, '1' has only one term in the sequence.

def collatz(num):
	if num%2:
		return num*3 + 1
	else:
		return num//2
		
def dynamic_find_sequence(num):
	global collatz_lengths
	if str(num) in collatz_lengths.keys(): # if already calculated, return that.
		return collatz_lengths[str(num)]
	else:
		# not yet calculated, calculate for next term in sequence.
		collatz_lengths[str(num)] = dynamic_find_sequence(collatz(num)) + 1 # add current term to sequence
		return collatz_lengths[str(num)]

# main
collatz_lengths = {'1':1} # store lengths of previously calculated values in a hashtable
# since 1 is the finish, '1' has only one term in the sequence.

highest = 1
answer = 1
# start from 2, end at 1M.
for i in range(2, 10**(6)):
  seqlen = dynamic_find_sequence(i)
  if seqlen > highest:
    answer = i
    highest = seqlen
print(answer)
