import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce.csv")

'''
EDA = Exploratory Data Analysis, to give you a general idea of what is going on with the data, what it says. 

sns.jointplot(x="Time on App", y="Yearly Amount Spent", data=df, alpha=0.5)
plt.show()

sns.jointplot(x="Length of Membership", y="Yearly Amount Spent", data=df, alpha=0.5)  #more correlation 
plt.show()

sns.pairplot(df, kind="scatter", plot_kws={'alpha': 0.4})
plt.show()
'''
sns.lmplot(x="Length of Membership", y="Yearly Amount Spent", data=df, scatter_kws={"alpha": 0.5}) ##creates a best fit line
plt.show()
