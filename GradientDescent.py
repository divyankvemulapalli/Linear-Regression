#Bonus HomeWork 1
#Implementation of Gradient Descent of two variables

from ast import literal_eval
import matplotlib.pyplot as plt
from numpy import polyval


def theta_function(theta):

    temp = 0;
    if (theta == 0):
        for i in range(input_number):
            temp = temp + ((temp_theta_0+(temp_theta_1*X_coordinates[i])) - Y_coordinates[i]);
        return temp;
    if(theta == 1) :
        for i in range(input_number):
            temp = temp + ((temp_theta_0 + (temp_theta_1 * X_coordinates[i])) - Y_coordinates[i]) * X_coordinates[i];
        return temp;




#Initializations
theta_0 = 0;
temp_theta_0 = theta_0; # used to store temporary theta 0 value
theta_1 = 0;
temp_theta_1 = theta_1; # used to store temporary theta 1 value
X_coordinates = []; # storing all X coordinates in this array
Y_coordinates = [] # storing all Y coordinates in this array




input_number = input("enter number of input coordinates\n");
input_coordinates = raw_input("enter the coordinates in this format...(0,0) (1,1)\n").split();
input_stepsize = input("enter the step size (if your input points are nearer, step size should be minimal) \n");

if ( len(input_coordinates) == input_number ):
    coordinates = [literal_eval(coordinate) for coordinate in input_coordinates]; #converts strings into array of coordinates

    for i in xrange(input_number):
        X_coordinates.insert(i, coordinates[i][0]); #inserting X coordinates in an array
        Y_coordinates.insert(i, coordinates[i][1]);#inserting Y coordinates in an array
        plt.scatter(X_coordinates[i], Y_coordinates[i]); #plotting every point on to the graph

    plt.show();
else:
    print "Program terminated due to miss match of no.of points entered with no.of points supposed to be entered";
    exit(0);

while 1 : # if stepsize is not set to the best one, it may go into infinite loop because step size plays a mojor role in predicting the best theta 0 and theta 1 value

    theta_0 = theta_0 - ( input_stepsize* (theta_function(0)/input_number)); # I had calculated Theta_0 and Theta_1 seperately for my better understanding
    theta_1 = theta_1 - ( input_stepsize* (theta_function(1)/input_number));

    if (temp_theta_0 != theta_0 and temp_theta_1 != theta_1):  # this statement need not to be true for every data points but it works for some data points ex: Test data points given in class
        temp_theta_0 = theta_0;
        temp_theta_1 = theta_1;
    else:
        break;

computable_funtion_values = polyval([temp_theta_1, temp_theta_0],X_coordinates);  # used to plot the hypothesis function on to the graph
plt.plot(X_coordinates, computable_funtion_values);

for i in xrange(input_number):
    plt.scatter(X_coordinates[i], Y_coordinates[i]);  # plotting every point on to the graph

plt.show();






print "theta_0: " + str(theta_0) + " theta_1: " + str(theta_1);
print "These are the best theta_0 and theta_1 values for which our J(theta_0,theta_1) function is minimized"




