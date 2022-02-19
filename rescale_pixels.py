from PIL import Image
import os
import sys

def rescale(image, scale):

        return image.resize((scale, scale), resample=Image.BOX)
    
def store_pixel(image, path):
    
    image.save(path)

    return    
    
if __name__ == '__main__':
    FilePaths = []
    dirname = os.getcwd()
    dirname = str(dirname) + '\Pixels'
    
    for root, dirs, files in os.walk(dirname):
        for file in files:
            
            if file.endswith('.png'):
                FilePaths.append(str(os.path.join(root, file)))
        
    Resize = False        
    for i in range ( len ( sys.argv)):
        if sys.argv[i].lower() == '--scale':
            Resize = True
            size = int(sys.argv[i+1])
            
    
    if Resize == False:
        print('Setting Standard scale 1px')
        size = 1
        
    for path in FilePaths:
        img = Image.open(path)
        img = rescale(img, size)
        store_pixel(img, path)
        
        
    
    