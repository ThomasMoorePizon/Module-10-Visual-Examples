#Importing pyplot
from matplotlib import pyplot

x = (1,2,3,4,5)
y = (1,5,3,2,5)
x2 = (1,2,3,4,5)
y2 = (5,12,3,7,1)

#Plotting to our canvas
pyplot.plot(x,y,'r',label='line one', linewidth=10)
pyplot.plot(x2,y2,'y',label='line two',linewidth=10)
pyplot.title('Thomas Cross Lines') 
pyplot.ylabel('Y axis') 
pyplot.xlabel('X axis')
pyplot.legend() 
pyplot.grid(True,color='k')

#Showing what we plotted
pyplot.show()