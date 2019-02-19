import pandas as pd
reviews=pd.read_csv('ign.csv')
#print(reviews.head())
#print(reviews.shape)

#print(reviews.iloc[0:5,:])

reviews = reviews.iloc[:,1:]

#print(reviews.head())
#print(reviews.index)

some_reviews = reviews.iloc[10:20,]
#print(some_reviews.head())

#print(reviews.loc[:5,"score"])
#print(reviews.loc[:5,["score", "release_year"]])

#print(reviews[["score", "release_year"]])

#Series
s1 = pd.Series([1,2])
#print(s1)
s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"])
#print(s2)
#print(pd.DataFrame([s1,s2]))

frame = pd.DataFrame(
    [
        [1,2],
        ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"])
#print(frame)
#print(reviews.corr())

#DataFrame Math with Pandas
#print(reviews["score"] / 2)

#Boolean Indexing in Pandas
score_filter = reviews["score"] > 7
#print(score_filter)
filtered_reviews = reviews[score_filter]
#print(filtered_reviews.head())

xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
#print(filtered_reviews.head())
import matplotlib.pyplot as plt
#Pandas Plotting
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

#reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")
#plt.show()


























