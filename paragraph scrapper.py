import requests,bs4,csv as CSV
def webscrapper(webpage):
    with open(webpage,'r',encoding='utf-16') as file:
        soup=bs4.BeautifulSoup(file)
        paragraph=soup.select('p')
        for i in paragraph:
            yield i.getText()
def excell():
    csv=open('sentence.csv','a',newline='' ,encoding='utf-16')
    outputWriter = CSV.writer(csv)
    page=webscrapper(input('filename: '))
    for i in page:
        k=i.split('።')
        for z in k:
            if len(z)>30:
                outputWriter.writerow([z])
    csv.close()
                
    
def spaceKiller():
    csv=open('sentence1.csv','a',newline='' ,encoding='utf-16')
    read=open('sentence2.txt','r',newline='' ,encoding='utf-16')
    outputWriter = CSV.writer(csv)
    k=read.readline()
    while k!='':
        if len(k.strip())>30:
            outputWriter.writerow([k.strip()])
        k=read.readline()
    csv.close()
    
    
spaceKiller()
