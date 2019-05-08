import tensorflow as tf
import numpy as np
import operator

#tuple(map(operator.add, a, b))

learning_rate = 0.5
training_epochs = 10


with tf.Session() as sess:

    tf.global_variables_initializer().run()
    coordinates = (0.0,0.0)
    coordinates = tuple([learning_rate*x for x in coordinates])

    for i in range(training_epochs):

        function_1_value = ((coordinates[0] - 10)**2) + ( (coordinates[1] + 2)**2)
        print("Function f(x,y) value = " + str(function_1_value) + "\n")
        function_1_X_value = (2 * coordinates[0]) - 20
        function_1_Y_value = (2 * coordinates[1]) + 4
        function_1_X_Y = (function_1_X_value,function_1_Y_value)
        function_1_X_Y = tuple([learning_rate * x for x in function_1_X_Y])
        coordinates = tuple(map(operator.sub, coordinates, function_1_X_Y))
        print("(X coordinate, Y coordinate) = " + str(coordinates) + "\n")

    sess.close()


with tf.Session() as sess:

    tf.global_variables_initializer().run()
    coordinates = (0.0,0.0)
    coordinates = tuple([learning_rate*x for x in coordinates])

    for i in range(training_epochs):

        function_2_value = ((coordinates[0] - 10)**2) + ((coordinates[0] - coordinates[1] + 5)**4)
        print("Function g(x,y) value = " + str(function_2_value) + "\n")
        function_2_X_value = ((2 * coordinates[0]) - 20 ) + (4 * ((coordinates[0] - coordinates[1] + 5) ** 3 ))
        function_2_Y_value = 4 * ((coordinates[1] - coordinates[0] - 5) ** 3 )
        function_2_X_Y = (function_2_X_value,function_2_Y_value)
        function_2_X_Y = tuple([learning_rate * x for x in function_2_X_Y])
        coordinates = tuple(map(operator.sub, coordinates, function_2_X_Y))
        print("(X coordinate, Y coordinate) = " + str(coordinates) + "\n")

    sess.close()