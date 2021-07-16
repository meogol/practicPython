import tensorflow as tf

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'data\\train',
    validation_split=0.2,
    subset="training",
    batch_size=10,
    shuffle=True,
    seed=324893,
    image_size=(256, 256),
    color_mode='rgb'
)

validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'data\\validation',
    validation_split=0.2,
    subset="validation",
    batch_size=10,
    shuffle=True,
    seed=324893,
    image_size=(256, 256),
    color_mode='rgb'
)

test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'data\\test',
    batch_size=10,
    image_size=(256, 256),
    color_mode='rgb',

)
