import sampledata

#Lecture 2 Slide 22 In Lecture with linked list. 
def SortedIntersectPythonList(p1, p2):
    queryresults = []
    for elemSam in p1:
        for elemFrodo in p2:
            if (elemSam == elemFrodo):
                queryresults.append(elemSam)
    return queryresults

#Lecture 2 Slide 26
def SortedIntersectConjunctiveQueriesPythonList(listTerms):
    sorted(listTerms, key=len)


#print(sampledata.postingListSam)
#print(sampledata.postingListFrodo)

listTerms = [sampledata.postingListSam, sampledata.postingListFrodo, sampledata.postingListBlue]

print(listTerms)

listTerms = sorted(listTerms, key=len)

print("sorted")
print(listTerms)
#print(SortedIntersectPythonList(sampledata.postingListSam, sampledata.postingListFrodo))