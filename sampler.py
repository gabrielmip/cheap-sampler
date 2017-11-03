import os, sys, random

def countFileLines (fin):
    initialFilePointer = fin.tell()
    fin.seek(0)
    nlines = 0 
    for line in fin:
        nlines += 1
    fin.seek(initialFilePointer)
    return nlines


inputFilename = sys.argv[1]
outputFilename = sys.argv[2]
targetSampleSize = int(sys.argv[3])

fin = open(inputFilename)
fout = open(outputFilename, 'w')

collectionLength = countFileLines(fin)

containsDocument = [False] * collectionLength
currentSampleSize = 0 

while currentSampleSize < targetSampleSize:
    newCandidateIndex = random.randint(0, collectionLength)
    if not containsDocument[newCandidateIndex]:
        containsDocument[newCandidateIndex] = True
        currentSampleSize += 1

fin.seek(0)
documentIndex = 0 
for line in fin:
    if containsDocument[documentIndex]:
      fout.write(line)
    documentIndex+=1

fin.close()
fout.close()

