import json
from textblob import TextBlob as tb


def process_or_store(comm):
    print(json.dumps(comm))
def percentage(part, whole):
    return 100*float(part)/float(whole)
import matplotlib.pyplot as plt



subjectivity =0
positive= 0
negative=0
neutral=0
polarity=0
lines=0

chk=tb("Lot of respect is there for Professor Stephen Hawking but at  the same time very disappointed to know that he had no faith in God and his existence.")
print(chk.sentiment.polarity)


with open('comments.txt', encoding='utf-8') as f:
    for line in f:
        # use a try-except block since we occasionally get language not supported errors
        #print(line)
        analysis=tb(line)
        lines+=1
        print(analysis.sentiment.polarity)
        polarity +=analysis.sentiment.polarity
        subjectivity +=analysis.sentiment.subjectivity 
        if(analysis.sentiment.polarity==0):
            neutral+=1
        elif (analysis.sentiment.polarity>0):
            positive+=1
        elif (analysis.sentiment.polarity<0):
            negative+=1
positive=percentage(positive,lines)
negative=percentage(negative,lines)
neutral=percentage(neutral,lines)
positive=format(positive,'0.2f')
negative=format(negative,'0.2f') 
neutral=format(neutral,'0.2f')
print("Positive",positive, " Score",polarity," Negative",negative,"Neturat",neutral,"Subjectivity ",subjectivity )    
labels=['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
sizes=[positive,neutral,negative]
color=['yellowgreen','gold','red']
patches,texts=plt.pie(sizes,colors=color,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("How people are reacting to the post on facebook")
plt.axis('equal')
plt.tight_layout()
plt.show()
           