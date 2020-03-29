#Importing pyplot
from matplotlib import pyplot as plt

x = (1,2,3,4,5)
y = (1,2,3,4,5)
x2 = (1,2,3,4,5)
y2 = (5,4,3,2,1)

#Plotting to our canvas
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('Thomas Cross Lines') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')
plt.legend() 
plt.grid(True,color='k')

#Showing what we plotted
plt.show()