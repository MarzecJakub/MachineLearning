from hyperparam import Args     
from tensorflow.keras.preprocessing.image import ImageDataGenerator

args = Args()

train_datagen = ImageDataGenerator(
    rotation_range = 15,
    width_shift_range = 0.2,
    height_shift_range = 0.14,
    horizontal_flip = True
)

def train():
    train_generator = train_datagen.flow_from_directory(
        args.train_dir,
        target_size=(args.im_width, args.im_height),
        batch_size=args.batch_size,
        class_mode='categorical'
    )
    return train_generator


def valid():
    validation_generator = train_datagen.flow_from_directory(
        args.valid_dir,
        target_size=(args.im_width, args.im_height),
        batch_size=args.batch_size,
        class_mode='categorical'
    )
    return validation_generator

