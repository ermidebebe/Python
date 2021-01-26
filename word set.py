def main():
    file1=open(r'C:\Users\Ermi_D\Desktop\practice\practice.txt','r')
    file2=open(r'C:\Users\Ermi_D\Desktop\practice\practice2.txt','r')
    word1=set(file1.readline().split())
    word2=set(file2.readline().split())
    word3=word1 | word2
    word4=word1&word2
    word5=word1^word2
    word6=word1-word2
    word7=word2-word1
    print('unique words contained in both files are')
    for val in word3:
        print(val)
    print('The words that appear in both files are')
    for val in word4:
        print(val)
    print('the words that appear in file 1 only are')
    for val in word6:
        print(val)
    print('the words that appear in file 2 only are')
    for val in word7:
        print(val)
    print('the words that appear in either of two but not in both are')
    for val in word5:
        print(val)
    file1.close()
    file2.close()
main()
    
    
