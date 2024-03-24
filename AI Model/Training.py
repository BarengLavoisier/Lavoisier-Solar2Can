from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

# Define paths and hyperparameters
train_data_dir = "C:/Users/Great/MobileNetV1 AI/Training/Trash_net data"
val_data_dir = "path/to/your/validation/data"
num_classes = 8
img_size = (224, 224)
batch_size = 32
epochs = 10

# Load pre-trained MobileNetV1 (without top layers)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=img_size + (3,))

# Freeze base layers (optional)
for layer in base_model.layers:
    layer.trainable = False

# Add new classification layers
x = base_model.output
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

# Create the final model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Data augmentation (optional)
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
val_datagen = ImageDataGenerator(rescale=1./255)

# Create training and validation generators
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)
val_generator = val_datagen.flow_from_directory(
    val_data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# Train the model
model.fit(
    train_generator,
    epochs=epochs,
    validation_data=val_generator
)

# Save the trained model
model.save("trained_mobilenet_trashnet.h5")