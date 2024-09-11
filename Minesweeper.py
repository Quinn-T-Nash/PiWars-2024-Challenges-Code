from __future__ import print_function
import pixy
from ctypes import *
from pixy import *

import redboard
# Pixy2 Python SWIG get Red/Green/Blue example #

#print("Pixy2 Python SWIG Example -- Get Red/Green/Blue")

#pixy.init ()


#X = 158
#Y = 104
#Frame = 1

pixy
get_all_features = True

print("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")


class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

vectors = VectorArray(100)
frame = 0

i_count = 0
X = 158
Y = 104


while 1:
  if get_all_features:
    line_get_all_features ()
  else:
    line_get_main_features ()
    
  v_count = line_get_vectors (100, vectors)
  

 
  if v_count == 0:
    redboard.M1(0)
    redboard.M2(0)

  elif v_count == 1:
    #print('frame %3d:' % (frame))
    frame = frame + 1
    #redboard.time.sleep(1)
    #for index in range (0, v_count):
      #print('[VECTOR: INDEX=%d X0=%d Y0=%d X1=%d Y1=%d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1))
    #Means straight line
    if vectors[1 - 1].m_x0 > 36 and vectors[1 -1].m_x0 < 42 :
      redboard.M1(15)
      redboard.M2(15)
    #Turn Right
    elif vectors[1- 1].m_x0 > 42:
      redboard.M1(85)
      redboard.M2(-85)
    #Turn Left
    elif vectors[1 -1].m_x0 < 36:
      redboard.M1(-85)
      redboard.M2(85)   
  
    
  elif v_count == 3:
    while v_count != 1:
      redboard.M1(15) 
      redboard.M2(15)
      if get_all_features:
        line_get_all_features ()
      else:
        line_get_main_features ()
      v_count = line_get_vectors (100, vectors)
      print('v3') 
    i_count = i_count + 1
    print(i_count)
    print('intersection')
    if i_count == 2: #turn
      redboard.M1(-90)
      redboard.M2(90) 
      redboard.time.sleep(0.3)
      print(v_count)
      print('vector count after initial turn')
      i_count = 0 	  


while 1:

  redboard.time.sleep(1)
  Frame = Frame + 1
