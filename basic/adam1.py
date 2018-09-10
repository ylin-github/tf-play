import tensorflow as tf

x = tf.Variable(10.0, name="x")
y = tf.Variable(50.0, name="y")
cost = tf.add(tf.square(x), tf.square(y), name="cost")

optimizer = tf.train.AdamOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(cost)

with tf.Session() as sess:
  with tf.summary.FileWriter('adam1', sess.graph) as sum:
    sess.run(tf.global_variables_initializer())
    print sess.run(cost)

    for i in range(100):
        sess.run(train_op)
        print sess.run([x, y, cost])

