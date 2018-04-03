#matplot test1
'''import numpy as np
from matplotlib.pyplot import *

x = np.linspace(-np.pi,np.pi,256)
c,s = np.cos(x * x),np.sin(x)
subplot(211)
plot(x,c,'ro',label = '$sin(x)$')
plot(x,s,label = 'cos(x^2)')
xlabel('x')
ylabel('y')
legend()
title('This is a title test')
show()

t1 = np.arange(0.0,5.0,0.02)
t2 = np.arange(0,0.5,0.1)
subplot(212)
plot(t1,np.exp(-t1)*np.cos(2 * np.pi *t1),'bo',t2,'k')
show()
print(t1)
'''

#matplot test2
import numpy as np
import matplotlib.pyplot as plt
mu,sigma = 100, 15
x = mu + sigma * np.random.randn(100)
plt.hist(x,50,normed = 1,facecolor = 'r')
plt.xlabel('IQ')
plt.ylabel('Frequence')
plt.title('Histogram of IQ')
plt.text(60,0.025,r'$\mu=100,\ \sigma = 15$')
plt.axis([40,160,0,0.04])
plt.show()



