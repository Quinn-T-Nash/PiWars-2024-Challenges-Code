from __future__ import print_function
import pixy
from ctypes import *
from pixy import *

import redboard

# pixy2 Python SWIG get line features example #
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

class IntersectionLine (Structure):
  _fields_ = [
    ("m_index", c_uint),
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

vectors = VectorArray(100)
intersections = IntersectionArray(100)
barcodes = BarcodeArray(100)
frame = 0


while 1:
  if get_all_features:
    line_get_all_features ()
  else:
    line_get_main_features ()
  
  v_count = line_get_vectors (100, vectors)
 
  if v_count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    #redboard.time.sleep(1)
    for index in range (0, v_count):
      print('[VECTOR: INDEX=%d X0=%d Y0=%d X1=%d Y1=%d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1))
        
    #Means straight line
    if vectors[v_count - 1].m_x0 > 34 and vectors[v_count -1].m_x0 < 44 :
      redboard.M1(25)
      redboard.M2(25)
    #Turn Right
    elif vectors[v_count - 1].m_x0 > 44:
      redboard.M1(70)
      redboard.M2(-70)
    #Turn Left
    elif vectors[v_count -1].m_x0 < 34:
      redboard.M1(-70)
      redboard.M2(70)
  else:
    redboard.M1(0)
    redboard.M2(0)
    
    
    
