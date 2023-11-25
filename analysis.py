#this code will take the text as an input from a text file and give the percentages of positive and negative content
#importing the necessary modules
import vaderSentiment.vaderSentiment as vs
import matplotlib.pyplot as plt

#opening the text file and opening it in read mode
text_data = open("C:\\Users\\HP\\Desktop\\PycharmProjects\\MINI\\read.txt", encoding='utf-8').read()

#create an instance of Sentiment Intensity Analyzer
analyzer =vs.SentimentIntensityAnalyzer()

#calculate the polarity scores of the given text
sentiment = analyzer.polarity_scores(text_data)

#these line extract the positive,negative scores from
# 'sentiment' and stores them in a seperate variable
positive_prob = sentiment['pos']
negative_prob = sentiment['neg']
# neutral_prob = sentiment['neu']
# c_score=sentiment['compound']

#printing the values
print("Positive probability:", positive_prob)
print("Negative probability:", negative_prob)
# print("compound score:", c_score)

# Labels for the pie chart
labels = ['Positive', 'Negative',]

# Colors for the pie chart slices
colors = ['lightblue', 'red']

# Create the pie chart
plt.pie([positive_prob, negative_prob], labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Analysis')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

# Display the pie chart
plt.show()



