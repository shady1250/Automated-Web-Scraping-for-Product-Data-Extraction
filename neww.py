import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
f=open("sample.txt","r+")
x=f.read();
y=word_tokenize(x)
z=set(y)
z=list(z)

for i in range(0,len(y),1):
    n=x.count(y[i]);
    print(y[i],n);
    
    
f.close();

