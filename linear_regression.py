import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

def file_reader(filename_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    _, csv_row = reader.read(filename_queue)
    record_defaults = [[0.0], [0.0]]
    x,y = tf.decode_csv(csv_row, record_defaults=record_defaults)
    return x,y



def append_bias_reshape(x_features,y_vector):
    number_of_training_samples = x_features.shape[0]

    number_of_dim = x_features.shape[1]

    new_x_features = np.reshape(np.c_[np.ones(number_of_training_samples),x_features],[number_of_training_samples,number_of_dim + 1])

    new_y_vector = np.reshape(y_vector,[number_of_training_samples,1])

    return new_x_features,new_y_vector




number_of_instances = file_len("training_set.csv")

filename_queue = tf.train.string_input_producer(["training_set.csv"])

x, y = file_reader(filename_queue)

x_array = []
y_array = []

display_step = 50

with tf.Session() as sess:

    tf.global_variables_initializer().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(number_of_instances):
        try:
            x_coordinates, y_coordinates = sess.run([x,y])
            x_array.insert(i,x_coordinates)
            y_array.insert(i,y_coordinates)
        except tf.errors.OutOfRangeError:
            break
    sess.close()

x_array = np.transpose(np.column_stack(x_array))
y_array = np.transpose(np.column_stack(y_array))

print(x_array)

x_features, y_vector = append_bias_reshape(x_array,y_array)

print(x_features)

learning_rate = 0.5
training_epochs = 10
cost_history = np.empty(shape=[1],dtype=float)


n_dim = x_features.shape[1]

X = tf.placeholder(tf.float32,[None,n_dim])
Y = tf.placeholder(tf.float32,[None,1])

thetas = tf.Variable(tf.ones([n_dim,1]))


init = tf.global_variables_initializer()

predict = tf.matmul(X, thetas)

cost = tf.reduce_mean(tf.square(predict - Y))

training_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        temp = sess.run(training_step,feed_dict={X:x_features,Y:y_vector})

        if (epoch + 1) % display_step == 0:
            cost_history = sess.run(cost,feed_dict={X:x_features,Y:y_vector})
            #print("cost=", cost_history, '\n', "Thetas=", sess.run(thetas), '\n')
            print("[X,Y] = ", sess.run(thetas), '\n')


    print("Optimization done...")
    training_cost = sess.run(cost, feed_dict={X: x_features, Y: y_vector})
    print("Training cost=", training_cost,'\n', "Thetas=", sess.run(thetas), '\n')

    plt.plot(x_array, y_array, 'bo', label='Data Points')
    plt.plot(x_features, sess.run(thetas[1:]) * x_features + sess.run(thetas[0]),label='Fitted line')
    plt.legend()
    plt.show()


    sess.close()