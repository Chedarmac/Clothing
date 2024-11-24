import numpy as np
import pandas
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns
from lxml.objectify import annotate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

#Data loading
data = pd.read_csv(r"C:\Users\igwec\OneDrive\Documents\Portfolio Work\Clothing\clothing_p.csv")

print(data.head())
print()
#Dataset Summary
print(data.info())

#Dataset shape
print(data.shape)

#Statistical summary
print(data.describe())

#Null and duplicate values

print("Null values: ")
print()
print(data.isna().sum())

print("print duplicated values: ")
print()
print(data.duplicated().sum())

#EDA

sns.histplot(data, x = "Age", kde = True)
plt.title ("Age distribution of customers")
plt.xlabel("Age")
plt.ylabel("Volume of Customer")
plt.show()

#category
data["Category"].value_counts().plot(kind = "pie")
plt.title("Product categories by volume")
plt.show()
#Review Rating

sns.boxplot(data, x = "Review Rating")
plt.title("Customer Review distribution")
plt.xlabel("Review rating")
plt.show()

#Previous purchases

sns.displot(data, x = "Previous Purchases")
plt.xlabel("Previous Purchases")
plt.title("Distribution of previous purchases among customers")
plt.show()



#purchase amount
sns.histplot(data, x = "Purchase Amount (USD)")
plt.title("Purchase amount (USD) distribution")
plt.xlabel("Purchase Amount ($)")
plt.show()

#Age Group

sns.countplot(data, x = "Age Group")
plt.title("Age Group by count")
plt.xlabel("Age Group")
plt.show()

#Subscription Status

sns.countplot(data, x = "Subscription Status")
plt.xlabel("Subscription Status")
plt.ylabel("Yes or no")
plt.title("Subscription status")
plt.show()


# for multivriate analysis
sns.barplot(data, x="Gender", y= "Purchase Amount (USD)", estimator= "mean")
plt.xlabel("Gender")
plt.ylabel("Purchase Amount ($)")
plt.title("Gender and Purchase Amount")
plt.show()

#Category and mean purchases

sns.barplot(data, x = "Category", y = data["Purchase Amount (USD)"], estimator="mean", ci=None)
plt.show()

#Age group and frquency of purchases.
sns.boxplot(data, x="Age Group", y="Previous Purchases", hue= "Age Group")
plt.title("Age Groups & previous purchase distribution")
plt.show()

#Loyalty group and frequency of purchases

sns.boxplot(data, x= "Customer Loyalty", y = "Review Rating", hue="Customer Loyalty")
plt.title("Customer Loyalty and Review rating")
plt.show()


#previous purchases and purchase amount

sns.scatterplot(data, x= "Review Rating", y= "Purchase Amount (USD)")
plt.title("Relationship between previous purchases and Purchase Amount")
plt.show()
