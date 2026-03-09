import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [2,4,6,8,10]

bars = ['A','B','C','D']
values = [5,7,3,8]

scatter_x = [1,2,3,4,5,6]
scatter_y = [5,7,8,7,6,9]

hist_data = [5,7,8,8,9,10,10,10,11,12,13]

pie_labels = ['Apple','Banana','Mango','Orange']
pie_values = [30,25,25,20]

box_data = [10,20,30,40,50,60,70]

# Create figure
plt.figure(figsize=(12,8))

# 1 Line Graph
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("Line Graph")

# 2 Bar Graph
plt.subplot(2,3,2)
plt.bar(bars,values)
plt.title("Bar Graph")

# 3 Scatter Plot
plt.subplot(2,3,3)
plt.scatter(scatter_x,scatter_y)
plt.title("Scatter Plot")

# 4 Histogram
plt.subplot(2,3,4)
plt.hist(hist_data)
plt.title("Histogram")

# 5 Pie Chart
plt.subplot(2,3,5)
plt.pie(pie_values,labels=pie_labels,autopct='%1.1f%%')
plt.title("Pie Chart")

# 6 Box Plot
plt.subplot(2,3,6)
plt.boxplot(box_data)
plt.title("Box Plot")

# Show all graphs
plt.tight_layout()
plt.show()