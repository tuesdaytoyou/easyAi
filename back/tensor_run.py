import datetime, os
import sys


epochsValue = sys.argv[1]
rateValue = sys.argv[2]
batchValue = sys.argv[3]
optimizerValue = sys.argv[4]

epochsValue = int(epochsValue)
rateValue = float(rateValue)
batchValue = int(batchValue)

# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# plot cat photos from the dogs vs cats dataset
os.system('ls')
base_dir = './data/cats_and_dogs_filtered'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training cat/dog pictures
train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')

# Directory with our validation cat/dog pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

train_cat_fnames = os.listdir( train_cats_dir )
train_dog_fnames = os.listdir( train_dogs_dir )

# %matplotlib inline

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Parameters for our graph; we'll output images in a 4x4 configuration
nrows = 4
ncols = 4

pic_index = 0 # Index for iterating over images
# Set up matplotlib fig, and size it to fit 4x4 pics

fig = plt.gcf()
fig.set_size_inches(ncols*4, nrows*4)

pic_index+=8

next_cat_pix = [os.path.join(train_cats_dir, fname) 
                for fname in train_cat_fnames[ pic_index-8:pic_index] 
               ]

next_dog_pix = [os.path.join(train_dogs_dir, fname) 
                for fname in train_dog_fnames[ pic_index-8:pic_index]
               ]

for i, img_path in enumerate(next_cat_pix+next_dog_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') # Don't show axes (or gridlines)

  img = mpimg.imread(img_path)
  # plt.imshow(img)

# plt.show()

import tensorflow as tf

model = tf.keras.models.Sequential([
	# Note the input shape is the desired size of the image 150x150 with 3 bytes color
	tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
	tf.keras.layers.MaxPooling2D(2,2),
    
	tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2,2), 
    
	tf.keras.layers.Conv2D(64, (3,3), activation='relu'), 
	tf.keras.layers.MaxPooling2D(2,2),
    
	# Flatten the results to feed into a DNN
	tf.keras.layers.Flatten(), 
    
	# 512 neuron hidden layer
	tf.keras.layers.Dense(512, activation='relu'), 
    
	# Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('cats') and 1 for the other ('dogs')
	tf.keras.layers.Dense(1, activation='sigmoid')  
	])

model.summary()

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import Adamax
from tensorflow.keras.optimizers import Adagrad

if optimizerValue == 'Adam':
  model.compile(optimizer=Adam(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
elif optimizerValue == 'RMSprop':
  print('optimizer RMSprop')
  model.compile(optimizer=RMSprop(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
elif optimizerValue == 'SGD':
  model.compile(optimizer=SGD(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
elif optimizerValue == 'Adamax':
  model.compile(optimizer=Adamax(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
elif optimizerValue == 'Adagrad':
  model.compile(optimizer=Adagrad(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])
else: 
  model.compile(optimizer=RMSprop(learning_rate=rateValue),
              loss='binary_crossentropy',
              metrics = ['accuracy'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# All images will be rescaled by 1./255.
train_datagen = ImageDataGenerator( rescale = 1.0/255. )
test_datagen  = ImageDataGenerator( rescale = 1.0/255. )

# --------------------
# Flow training images in batches of 20 using train_datagen generator
# --------------------
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=batchValue,
                                                    class_mode='binary',
                                                    target_size=(150, 150))     
# --------------------
# Flow validation images in batches of 20 using test_datagen generator
# --------------------
validation_generator =  test_datagen.flow_from_directory(validation_dir,
                                                         batch_size=batchValue,
                                                         class_mode  = 'binary',
                                                         target_size = (150, 150))

logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

history = model.fit(train_generator,
					validation_data=validation_generator,
					steps_per_epoch=100,
					epochs=epochsValue,
					validation_steps=50,
					verbose=2,
          callbacks=[tensorboard_callback])
print(history.params)
print(history.history.keys())
print(history.history['accuracy'][-1])
print(history.history['loss'][-1])
# os.system('tensorboard --logdir=./logs --port=6008')
# tensorboard --logdir='logs' --port=6006