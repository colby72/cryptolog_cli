# This code is the property of Ramy Chmak
# ---------------------------------------

import Image
import stepic

imtoopen = raw_input("Tapez l'image a decoder : ")
img = Image.open(imtoopen)
s = stepic.decode(img)
d = s.decode()
print d
#end
