def inputing():
    score=[]
    print('please enter the number of subjects')
    len=int(input('subjects:'))
    print('please enter students score')
    for i in range(len):
        score.append(int(input('subject'+str(i+1)+"=")))
    return score
def total():
    score=inputing()
    total=0;
    for i in range(len(score)):
        total+=score[i]
    total-=smallest(score)
    return total,len(score)-1
def smallest(score):
    small=score[0]
    for i in range(len(score)):
        if score[i]<small:
            small=score[i]
    return small
def main():
    totaling,length=total()
    average=totaling/length
    print("the average is :",average)
 
main()
