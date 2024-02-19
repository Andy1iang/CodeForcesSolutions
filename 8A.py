# https://codeforces.com/problemset/problem/8/A

forward = False
backward = False

orderedFlags = input()
revFlags = orderedFlags[::-1]

firstSeq = input()
secondSeq = input()

# checking if the first sequence is possible
if firstSeq in orderedFlags:
    try:
        # clipping off everything in the first sequence and before
        orderedFlags = orderedFlags[orderedFlags.find(
            firstSeq)+len(firstSeq)::]
        if secondSeq in orderedFlags:  # checking if the second sequence is possible
            forward = True
    except:
        pass

# doing the same for reversed flag sequence
if firstSeq in revFlags:
    try:
        revFlags = revFlags[revFlags.find(firstSeq)+len(firstSeq)::]
        if secondSeq in revFlags:
            backward = True
    except:
        pass
