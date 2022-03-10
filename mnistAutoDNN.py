def main():
    '''Demo of keras_tuner for Neural Architecture Search (NAS).
    Smaller dense layers -> faster training -> more epochs, saves copute resources.
    Better than hand-designed.
    You can optimize the count of dense layers, number of units in dense layers, dropout %, type of activation function.
    Outcomes are saved in files, which enables resuming when once stopped.
    '''
    import tensorflow as tf
    from tensorflow import keras
    import keras_tuner as kt

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train, x_test = x_train / 255.0, x_test / 255.0

    def model_builder(hp):
        model = keras.Sequential()
        model.add(keras.layers.Flatten(input_shape=(28, 28)))
        # define search band for number of neurons/units and plug into dense layer
        hp_units = hp.Int('int', min_value=16, max_value=512, step=16)
        model.add(keras.layers.Dense(units=hp_units, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(10))

        # define search band for learning rate
        hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
                      loss=keras.losses.SparseCategoricalCrossentropy(),
                      metrics=['accuracy']
                      )
        return model

    # the tuner will automatically create files with the results of each trial.
    # Beyond Hyperband, there are also other methods for covering the search space.
    tuner = kt.Hyperband(model_builder,
                         objective='val_accuracy',
                         max_epochs=10,
                         factor=3,
                         directory='keras_tuner_files',
                         project_name='mnist_tune2'
                         )
    # stop early callback if validation loss does not change significantly in 5 epochs
    stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                  patience=5
                                                  )
    # start tuning
    tuner.search(x_train,
                 y_train,
                 epochs=50,
                 validation_split=0.2,
                 callbacks=[stop_early]
                 )

    # from best to worst, 0 = best
    best_hps = tuner.get_best_hyperparameters()[0]

    # print('The best number of neurons/units in the dense hidden layer is: ',best_hps.get('units'))
    # print('The best learning rate is: ',best_hps.get('learning_rate'))

    # # re-train with best value from tuning
    # # hardcode a hidden layer with the best val_accuracy from keras_tuner
    # model2 = keras.Sequential()
    # model2.add(keras.layers.Flatten(input_shape=(28, 28)))
    # model2.add(keras.layers.Dense(units=16, activation='relu'))
    # model2.add(tf.keras.layers.Dropout(0.2))
    # model2.add(tf.keras.layers.Dense(10, activation='softmax'))

    # load the tuner's best model and train fully
    best_model = tuner.hypermodel.build(best_hps)

    best_model.compile(optimizer='adam',
                       loss='sparse_categorical_crossentropy',
                       metrics=['accuracy']
                       )

    history = best_model.fit(x_train,
                             y_train,
                             epochs=5,
                             validation_split=0.2
                             )

    val_acc_per_epoch = history.history['val_accuracy']
    best_epoch = val_acc_per_epoch.index(max(val_acc_per_epoch)) + 1
    print(f'Best epoch: {best_epoch}')

    best_model.evaluate(x_test,
                        y_test
                        )


if __name__ == '__main__':
    main()
