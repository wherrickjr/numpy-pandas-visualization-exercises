##Part 1 exercises
import numpy as np
import pandas as np
fruits_series = pd.Series(["kiwi", "mango", "strawberry", 
                           "pineapple", "gala apple", 
                           "honeycrisp apple", "tomato", 
                           "watermelon", "honeydew", "kiwi", 
                           "kiwi", "kiwi", "mango", 
                           "blueberry", "blackberry", 
                           "gooseberry", "papaya"])

## elements in fruits
len(fruits_series)
fruits_series.size
fruits_series.count()

##2 index from fruits
list(fruits_series.index)

##3 only the values

list(fruits_series.values)

##4 data type
fruits_series.dtype


##5 
fruits_series.head() #first 5
fruits_series.tails(3) #last 3
fruits_series.sample(2) #2 random

#6 info from .describe
fruits_series.describe()

## 7 unique string values from fruits
print(list(fruits_series.value_counts().index))
print(fruits_series.unique())

##8 how many times each unique is in the list
fruits_series.value_counts()

##9 string value that occurs most frequently
fruit_series.mode()

##10 string that is least frequent

fruits_series.value_counts().nsmallest(n=1, keep='all')
























fruits_series = pd.Series["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

import numpy as np
import pandas as pd

# Part II series
type(fruits_series)
fruits_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

1#capitalize fruits
fruits_series
fruits_series.str.capitalize()

#count the letter 'a' in all the string values (string vectorization)
fruits_series.str.count('a')

#3 number of vowels in each and every string
def vowel_count(input_list):
    count = 0
    vowels = list('aeiou')
    for item in input_list:
        if item.lower() in vowels:
            count += 1
    return count
sum(fruits_series.apply(vowel_count))
#4 code to get the longest string value
fruit_lengths = fruits_series.str.len().max()
fruit_lengths

#5 strings that have 5 or more characters
fruits_series[fruits_series.str.len() >= 5 ]

#6 fruits containing letter 'o'
fruits_series[fruits_series.str.count('o') > 1]

#7 code only values that have substring berry
fruits_series[fruits_series.str.contains('berry')]

#8 only values that have substring apple
fruits_series[fruits_series.str.contains('apple')]

#9 string that contains the most vowels
fruits_series[fruits_series.str.count('[aeiou]').max()]

###Part 3
letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

#1 letter that occurs most frequently
letters.mode()

#2 letter occurs least frequently

letters.value_counts().tail(1)

#3 how many vowels
letters.str.count('[aeiou]').sum()

##4 how many consonants
letters.str.count('[^aeiou]').sum()

##5 series that has all same letters but uppercased
letters.str.upper()

##6 bar plot of frequencies of 6 most common occuring letters
letters.value_counts().head(6).plot.bar(title='Letters',
rot = 0, color = 'darkcyan', ec = 'black', width = .7.set(xlabel = 'Letter',
ylabel = 'Frequency', yticks = (range(1, 16, 1))))

numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

#1 data type?
# string

#how many elements?

#3 change to float

#4
numbers.max()
#5
numbers.min()

#6 
numbers.max() - numbers.min()

#7
numbers_bin = pd.cut(numbers, 4)
numbers_bin.value_counts()

#8
numbers_bin = pd.cut(numbers, 4, labels=['Bin1', 'Bin2', 'Bin3', 'Bin4'])
numbers_bin.value_counts().loc[['Bin1', 'Bin2', 'Bin3', 'Bin4']].plot.bar(title= 'Bin Count',
rot = 0, color = 'Blue', ec= 'Black', width = .7).set(xlabel='Bin', ylabel = 'Total', yticks = range(1.10,1))


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
#1
exam_scores.size

#2
(
    exam_scores.max(),
    exam_scores.min(),
    exam_scores.mean(),
    exam_scores.emdian()
)

#3

#4


#5
bin_edges = [0, 60, 70, 80, 90, 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_grades = pd.cut(curved_grades, bins=bin_edges, labels = bin_labels)

#6
adfadf