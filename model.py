import tensorflow as tf

def utworzModel():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape = (150,150,3)))
    model.add(tf.keras.layers.Conv2D(64, (2, 2), (1,1), activation='relu', padding = 'valid', kernel_regularizer = tf.keras.regularizers.l2(0.01), bias_regularizer = tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.SeparableConv2D(64, (3, 3), activation='relu', padding = 'same', bias_regularizer = tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Dropout(0.20))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.SeparableConv2D(128, (3, 3), activation='relu', bias_regularizer = tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.SeparableConv2D(128, (3, 3), activation='relu', bias_regularizer = tf.keras.regularizers.l2(0.01)))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.AveragePooling2D())
    model.add(tf.keras.layers.Conv2D(96, (3, 3), activation='relu'))
    model.add(tf.keras.layers.SeparableConv2D(128, (3, 3), activation='relu', bias_regularizer = tf.keras.regularizers.l1(0.01)))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.40))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    return model

