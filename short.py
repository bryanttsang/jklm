# make a smaller dictionary to consume less cpu

# load dictionary
f = open("new.txt", "r")
d = f.read().split("\n")
f.close()

occur = [0] * 16 # there are at most 15 unique letters in a word excluding the following set
exclude = {'k', 'w', 'x', 'y', 'z'}

'''
# number of words with x unique letters excluding exclude
for word in d:
    occur[len(set(word).difference(exclude))] += 1
print(occur)

# cumulative version
for x in range(15, 0, -1):
    occur[x] += occur[x+1]
print(occur)
'''

d.sort(key = lambda word: len(set(word).difference(exclude)), reverse = True)
d = d[:25318] # at least 10 unique letters excluding exclude

#print("occurance of q: %s" % sum(1 for word in d if 'q' in word))
#print("occurance of j: %s" % sum(1 for word in d if 'j' in word))

f = open("short.txt", "w")
for word in d:
    f.write("%s\n" % word)
f.close()
