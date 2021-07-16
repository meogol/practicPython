import os

from tensorflow import keras
from tensorflow.keras import layers

import ai_manager

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

inputs = keras.Input(shape=(256, 256, 3), name="img")

x = layers.Conv2D(128, 3, activation="relu", padding="same")(inputs)
x = layers.Conv2D(128, 3, activation="relu", padding="same")(x)
block_1_output = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
x = layers.Conv2D(64, 3, activation="relu", padding="same")(x)
x = layers.MaxPooling2D(3)(x)


x = layers.Conv2D(32, 3, activation="relu", padding="same")(x)
x = layers.Conv2D(32, 3, activation="relu", padding="same")(x)
x = layers.MaxPooling2D(3)(x)

x = layers.Conv2D(16, 3, activation="relu")(x)
x = layers.GlobalAveragePooling2D()(x)

x = layers.Dense(16, activation="relu")(x)
x = layers.Dense(16, activation="relu")(x)

outputs = layers.Dense(2, activation='softmax')(x)

model = keras.Model(inputs, outputs, name="toy_resnet")

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(ai_manager.train_ds,
          validation_data=ai_manager.validation_ds,
          epochs=3)

model.save('gosha_model')

model.save_weights('model_weights')

#model.load_weights('model_weights')
print(model.evaluate(ai_manager.test_ds))

# class_names = ai_manager.train_ds.class_names
# plt.figure(figsize=(10, 10))
# for images, labels in ai_manager.test_ds.take(1):
#     for i in range(9):
#         p = model.predict(tf.expand_dims(images[i], axis=0))
#         print(np.argmax(p))
#
#         ax = plt.subplot(3, 3, i + 1)
#         plt.imshow(images[i].numpy().astype("uint8"))
#         plt.title(class_names[labels[i]])
#         plt.axis("off")
#         plt.show()
