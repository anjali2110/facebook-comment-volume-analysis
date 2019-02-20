# facebook-comment-volume-analysis


ABSTRACT
Data in the social networking services is increasing day by day. So, there is heavy requirement to study the highly dynamic behaviour of the users towards these services. This work is a preliminary work to study and model the user activity patterns. We had targeted the most active social networking service ‘Facebook’ importantly the ‘Facebook Pages’ for analysis. The task here is to estimate the whether a given target category is positively or negatively correlated rest of the attribute. The analysis is done by modelling the comment patterns using The proposed project employs text mining and spans across language processing using TextBlob  technique.

INTRODUCTION
The massive deployment and utilization of social media has opened many options for citizens to publicly express their opinions but this itself has many challenges in interpreting these opinions or views in terms of a computer machine. At the same time, there is always a necessity to understand the people opinions has grown because of the frequent use of social media platforms (where attention is more than anywhere else). The analytics researches yet have an effective way to make sense of this mass conversation and interact meaningfully with thousands of others. “The proposed project employs text mining techniques and spans across language processing. The key objectives are to understand the thought process of the general public and the system aims to evaluate the opinions (positive/negative) and also attempts to understand the social media data. For”this project only facebook platform is targeted,.

Work Plan: 
We are going to work with TextBlob packages of python instead of NLTK for NLP, a simplified/augmented interface to NLTK) . Currently we are using PatternAnalyser . We can find  the lexicon for pattern analyzer  inside the library: textblob\en\en-sentiment.xml.

TEXTBLOB\en\en-sentiment has a class with name of PatternAnayser under BaseSentimentAnalyzer.




 


Results and Evaluation”
The”dataset for the system consists of the Facebook Corpus which is being modified continuously with the addition of new comments from all over the world. This data is obtained by using Facebook Developer Credentials and consequent authentication mechanism. Once the connection is established, the comments can be obtained as per the set limit, in this case 100 Comments. The data preprocessing steps consisted of the following steps after the necessary data has been extracted: 
1. Converting all the text to lowercase 
2. Removing the links 
3. Removing tabs 
4. Removing blank places 
5. Removing unwanted English stop words. 
6. Removing irrelevant characters, punctuations, whitespace, URLs, numbers. 
7. Replacing blank space and @UserName 
They are based on the most recent comments being done by the users worldwide given a input or two (if compared). The main function of the system is to classify the comments as positive, negative or neutral along and provide a visual representation of the aggregate of the sentiments expressed by the users. The results also represent the evolution of the system from showing merely the polarity of English comments For visualization of the results, a pie chart is used which shows the overall sentiment of a facebook on a scale from -1 to 1. 

Positive Sentiments:
Negative Sentiments:
Neutral sentiments:
 



CONCLUSION AND FUTURE WORK
The basic framework for the system has been designed and implemented at this stage – basic polarity detection, dictionary structure and content, and visualization structure. Also other Artificial Intelligence or Machine Learning methods such as Decision trees, K- Nearest Neighbors, Naïve Bayes, Neural Networks, Support Vector Machines, Linear/Quadrant discriminator etc. can also be utilized for automating the analytics process, the performance of such methods could be evaluated for efficiency. Other”mining techniques”such as Classification, Clustering or Fuzzy Methods for sentiment analysis can also be tested.  Also Word Cloud analysis can be done to analyze the final results or just the frequent words in the positive or negative tweets or the associations among them. 
“This study has several applications such as – 
a. Feedback over products and marketing for businesses. “
b.”Gauging public opinion on policies or any other valuable aspects and building support bases for domain experts(marketing, media, politics, research, medical, e-commerce, finance, government, education etc.). 
c. Enable researchers to conduct natural experiments and test social hypothesis.”


