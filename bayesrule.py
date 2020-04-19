"""
 Python 3
#   This is to draw a bayes rule frequency diagram. 
#April 19, 2020. Eric Rasmusen, erasmuse@Indiana.edu. Free for anyone to use. 
 
 This starts with the three numbers to input as data.
  I repeat this variable definition later, so the later code is more self-contained, but all you have 
  to do is change the values of n1, n2, and n3 to whatever you want. Then just run the code and two diagrams will pop out, 
  and both will be saved in your working directory, as temp1.png and temp.png. Delete or rename as you like. 
  
   All of this file is in terms of finding  the posterior Prob(infected|test yes). More generally, 
Bayes's Rule is for Prob (A|B). So think: A= infected, B = test yes, for your own application. 
"""
 
n1 = .05; prob_infected =  n1                 #This is prob(A)
n2 = .9; prob_test_yes_if_infected =  n2     #This is prob(A|B)
n3 = .8  ; prob_test_no_if_not_infected=  n3   #This is prob(not A|not B)
 
 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print("\n\n\n\n\n\n\n HERE'S THE BEGINNING ")#This is so I can tell when a new practice run of the code starts when I see teh console. 

###########################################################################################
#The first figure is a stick man that we will replicate 1000 times in the main figure
fig1,   ax1 = plt.subplots(figsize=(5, 5))
ax1.set_axis_off()
plt.axis("equal") #This makes the pixels equal on each axis, so a circle is not an ellipse.

width=40
chest=4
leg1 = plt.plot([0,1  ],[0, 3],linewidth=width,color='black') 
leg2 = plt.plot([1,2   ],[3, 0 ],linewidth=width,color='black') 
body = plt.plot([1,1   ],[3, chest  ],linewidth=width,color='black') 
arms = plt.plot([0,2   ],[chest-1, chest -1 ],linewidth=width,color='black') 
head  =plt.Circle((1, chest+ .7), radius=.7 , color='k',  linewidth=width, fill=False, clip_on=False)  #doesn’t clip at axes.
ax1.add_patch(head)
#http://www.learningaboutelectronics.com/Articles/How-to-draw-a-circle-using-matplotlib-in-Python.

plt.savefig("temp1.png", bbox_inches = "tight") 
plt.show()
##################################################################################

#Here is the second figure, the main one. 
#Here are the three numbers to input as data. I had  you input them at the top of this file.  
prob_infected =  n1            #This is prob(A)
prob_test_yes_if_infected =  n2     #This is prob(A|B)
prob_test_no_if_not_infected=  n3   #This is prob(not A|not B)

prob_not_infected= 1- prob_infected #This is prob(not A)
prob_test_no_if_infected =   1 - prob_test_yes_if_infected  #This is prob(not A|B)
prob_test_yes_if_not_infected= 1-  prob_test_no_if_not_infected  #This is prob(A|not B)

people = 1000
xlim = people/10;  ylim = people/100

fig2,   ax = plt.subplots(figsize=(10, 5))
plt.xlim(0,xlim ) 
plt.ylim(0, ylim   )

plt.plot([prob_infected*people/10 , prob_infected*people/10 ],[0, ylim],linewidth=4,color='green') 
plt.plot([0,prob_infected*people/10],[prob_test_no_if_infected *10 , prob_test_no_if_infected*10],linewidth=1,color='red') 
plt.plot([prob_infected*people/10, xlim],[prob_test_no_if_not_infected* 10 , prob_test_no_if_not_infected* 10 ],linewidth=1,color='blue') 

temp1 = 'Infected but test No:\n' + str(round(prob_infected* prob_test_no_if_infected*people)) + ' out of ' +  str(round(prob_infected*people)) + ' infected'
plt.annotate(temp1 ,
             xy=(prob_infected*people/20, prob_test_no_if_infected *5), color='red',  xycoords='data',
             xytext=(+10, -160), textcoords='offset points', fontsize=24,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

temp1 = 'Infected and test Yes:\n' + str(round( prob_infected* prob_test_yes_if_infected*people) ) + ' out of ' +  str(round (prob_infected*people)) + ' infected'
#Yes, temp1 duplicates the variable name. I like to do that for junk variables that are only used temporarily. 
plt.annotate(temp1 ,
             xy=(prob_infected*people/20,  5-prob_test_no_if_infected*5) , color='red',  xycoords='data',
             xytext=(+20, +250), textcoords='offset points', fontsize=24,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

temp1 = 'Not infected and test No:\n' + str(round( prob_not_infected* prob_test_no_if_not_infected*people) ) + ' out of ' +  str(round(prob_not_infected*people)) + ' not infected'
plt.annotate(temp1 ,
             xy=((1000+prob_infected*people)/20,   prob_test_no_if_not_infected*5) ,color ='blue',    xycoords='data',
             xytext=(+50, -200), textcoords='offset points', fontsize=24,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

temp1 = 'Not infected but test Yes:\n' + str(round( prob_not_infected* prob_test_yes_if_not_infected*people) ) + ' out of ' +  str(round(prob_not_infected*people)) + ' not infected'
plt.annotate(temp1 ,
             xy=((1000+prob_infected*people)/20 ,  5 + prob_test_no_if_not_infected*5), color='blue',   xycoords='data',
             xytext=(+40, +60), textcoords='offset points', fontsize=24,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

temp1 = 'The total number of people tested is 1,000.\n\n'+ \
'Prob(Infected|Yes) is ' +\
 '{0:.0%}'.format( prob_infected* prob_test_yes_if_infected*people/( prob_infected* prob_test_yes_if_infected*people + prob_not_infected* prob_test_yes_if_not_infected*people)) +  '\n\n'\
 +   '     = ' +str(round( prob_infected* prob_test_yes_if_infected*people) ) + ' out of ' +\
  str(round( prob_infected* prob_test_yes_if_infected*people + prob_not_infected* prob_test_yes_if_not_infected*people)) +\
 ' people testing Yes\n\n     = The ratio of the pink area to the\n           combined pink and blue areas.'
plt.text(102, 3  ,temp1, fontsize = 18)

ax.fill_between([0, prob_infected*people/10], [0, 0],[10, 10], color='None', alpha=0.2   )#I decided not to color this, but you can.
ax.fill_between([ 0, prob_infected*people/10], [prob_test_no_if_infected *10 ,prob_test_no_if_infected *10 ], [10,10], color='red', alpha=0.2   )
ax.fill_between([   prob_infected*people/10,100], [prob_test_no_if_not_infected *10 ,prob_test_no_if_not_infected *10  ], [10,10], color='blue', alpha=0.2   )

image1 = mpimg.imread('temp1.png') #This subroutine sticks in 1,000 stick figures. Optional.
for item in range(0,100):
    for jtem in range (0,10):
        ax.imshow(image1, aspect='auto', extent=(item, item+1.5 ,  jtem,   jtem+.8), alpha = .5)

plt.savefig("temp.png", bbox_inches = "tight") 
plt.show()
print("THAT'S THE END\n\n\n\n\n\n\n ")#This is so I can tell when a new practice run of the code starts when I see teh console. 
     #That's the end. 
 ###################################################################