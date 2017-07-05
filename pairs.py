#This program computes the combination of a set of letters.
let = 'ABCD'

pairs = [(let[a], let[b]) for a in range(len(let))
    for b in range(a, len(let))]

#Outputs the pairs
print(pairs)
