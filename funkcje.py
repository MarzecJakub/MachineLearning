import tensorflow as tf
import os
import glob
import matplotlib.pyplot as plt 
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def gpu():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
  
    
def get_nb_files(directory):
    if not os.path.exists(directory):
        print ('No directory')
        return 0
    cnt = 0
    for r, dirs, files in os.walk(directory):
        for dr in dirs:
              cnt += len(glob.glob(os.path.join(r, dr + "/*")))
    return cnt


def wyswPrzyklad(train_generator, classes):
    x, y= train_generator.next()
    fig = plt.figure(figsize=(10, 11))
    rows = 3
    cols = 3
    for i in range(0,9):
        image = x[i]
        fig.add_subplot(rows, cols, i+1)
        plt.imshow(image/255)
        plt.title(classes[np.argmax(y[i],axis=-1)])
    plt.show()
    
    
def wyswWykres(history, option):
    if option == 'acc':
        plt.figure(figsize=(6,4))
        plt.plot(history.history["accuracy"])
        plt.plot(history.history["val_accuracy"])
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")
        plt.title("ACCURACY")
        plt.legend(['training_accuracy', 'validation_accuracy'])
        plt.show()
    elif option == 'loss':
        plt.figure(figsize=(6,4))
        plt.plot(history.history["loss"])
        plt.plot(history.history["val_loss"])
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.title("LOSS")
        plt.legend(['training_loss', 'validation_loss'])
        plt.show()
    
    
def sprawdzKlase(IMAGE_PATH, model, classes):
    img=load_img(IMAGE_PATH,target_size=(150,150))

    img=img_to_array(img)
    predictions=model.predict(np.array([img]))

    dane = []
    for el in predictions:
        for el1 in el:
            dane.append(round(el1*100,2))

    im = plt.imread(IMAGE_PATH)
    fig, ax = plt.subplots()
    im = ax.imshow(im)
    
    plt.title("Klasa właściwa: "+IMAGE_PATH.split("/")[-2]+"\n Klasa estymowana:"+classes[dane.index(max(dane))])
    plt.show()

    plt.barh(classes,dane)
    ax = plt.gca()
    ax.axes.xaxis.set_ticks([]) 
    ax.spines['top'].set_visible(False) 
    ax.spines['right'].set_visible(False) 
    ax.spines['bottom'].set_visible(False) 
    ax.spines['left'].set_visible(False) 
    for index, value in enumerate(dane): 
            plt.text(value, index,
                     str(value)+"%")       
    plt.title('Prawdopodobieństwo poszczególnych klas') 
    plt.ylabel('') 
    plt.xlabel('') 
    plt.show()   
    