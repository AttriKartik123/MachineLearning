import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

bars = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

pie_labels = ['Apple', 'Banana', 'Mango', 'Orange']
pie_values = [30, 25, 25, 20]

# Create 3 graphs in one window
plt.figure(figsize=(10,4))

# 1️⃣ Line Graph
plt.subplot(1,3,1)
plt.plot(x, y)
plt.title("Line Graph")

# 2️⃣ Bar Graph
plt.subplot(1,3,2)
plt.bar(bars, values)
plt.title("Bar Graph")

# 3️⃣ Pie Chart
plt.subplot(1,3,3)
plt.pie(pie_values, labels=pie_labels, autopct='%1.1f%%')
plt.title("Pie Chart")

# Show all graphs
plt.show()