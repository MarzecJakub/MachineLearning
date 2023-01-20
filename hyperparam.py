import os
from funkcje import get_nb_files
import glob

class Args():
    def __init__(self):
        
        self.im_width, self.im_height = 150, 150
        self.batch_size = 32
        
        local_folder = 'C:/Users/yamrc/animals'
        self.train_dir = os.path.join(local_folder, 'train/')
        self.valid_dir = os.path.join(local_folder, 'valid/')
        self.test_dir = os.path.join(local_folder, 'test/')   
        
        self.nb_train_samples = get_nb_files(self.train_dir)
        self.classes = glob.glob(self.train_dir + "/*")
        self.classes = [x.split('\\')[-1] for x in self.classes]
        self.classes.sort()
        self.nb_classes = len(self.classes)
        self.nb_valid_samples = get_nb_files(self.valid_dir)            
        self.train_steps = int(self.nb_train_samples / self.batch_size)
        self.valid_steps = int (self.nb_valid_samples / self.batch_size)   
