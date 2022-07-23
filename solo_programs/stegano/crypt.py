# This code is the property pf Ramy Chmak
# ---------------------------------------

import stepic
import Image

imtoopen = raw_input("Tapez le nom de l'image : ")
text = raw_input("Tapez le texte : ")
img = Image.open(imtoopen)
imgg = stepic.encode(img, text)
imgg.save('stegano.bmp', 'BMP')
#end
