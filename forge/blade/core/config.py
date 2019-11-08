from pdb import set_trace as T
import numpy as np
import inspect

from collections import defaultdict
from itertools import chain

class Config:
   ROOT = 'resource/maps/procedural/map'
   SUFFIX = '/map.tmx'

   SZ = 128
   BORDER = 8
   R = C = SZ + 2*BORDER

   STIM = 7
   WINDOW = 2*STIM + 1

   NENT = 256
   NPOP = 8
   NTILE = 6 #Add this to tile static

   #V1.2 settings
   #RESTORE flat 5
   #RESOURCE = 32
   #HEALTH = 10
   #IMMUNE = 15

   XPSCALE = 10

   RESOURCE = 10
   HEALTH   = 10

   RESOURCERESTORE = 0.5
   HEALTHRESTORE   = 0.1

   IMMUNE = 10

   #Attack ranges
   MELEERANGE = 1
   RANGERANGE = 2
   MAGERANGE  = 3

   def __init__(self, **kwargs):
      for k, v in kwargs.items():
         setattr(self, k, v)

   def SPAWN(self):
      R, C = int(Config.R/2), int(Config.C/2)
      spawn = [(R-3, C), (R+3, C), (R, C-3), (R, C+3),
         (R+3, C+3), (R-3, C+3), (R+3, C+3), (R+3, C-3)]
      idx = np.random.randint(0, len(spawn))
      return spawn[idx]


