import pandas # Pandas is used to bring csv data into your python file
import matplotlib.pyplot as plt
# Matlob is used to draw graphs, charts from data(data visualisation library)
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('/Users/apuroop/python/Projects/Iphoneprice/iphone_price.csv')
#plt.scatter(data['version'], data['price'])
# Scatter plots use horizontal and vertical axes to plot data points
#plt.show()
model = LinearRegression()
model.fit(data[['version']],data[['price']]) # Model fit with data
# Convert values to 2d array nusing [[]]
print(model.predict([[13]]))
