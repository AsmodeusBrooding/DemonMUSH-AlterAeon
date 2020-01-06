#thin wrapper around eci
from ctypes import *
import sys
eciSpeed=6
eciSynthMode=0
eciInputType=1
eciDictionary=3
eciLanguageDialect=9
eciPitchBaseline=2
eciPitchFluctuation=3
eciSpeed=6
eciVolume=7
if sys.platform == 'linux2':
 lib = cdll['/opt/IBM/ibmtts/lib/libibmeci.so']
else:
 lib = windll.LoadLibrary(r".\eci.dll")
class Synth:
 def __init__(self):
  self.eci = lib.eciNew()
  self.setParam(eciSynthMode, 1)
 def setParam(self, param, value):
  return lib.eciSetParam(self.eci, param, value)
 def addText(self, text):
  lib.eciAddText(self.eci, text)
 def insertIndex(self, num):
  lib.eciInsertIndex(self.eci, num)
 def synthesize(self):
  lib.eciSynthesize(self.eci)
 def synchronize(self):
  lib.eciSynchronize(self.eci)
 def pause(self, flag):
  lib.eciPause(self.eci, flag)
 def stop(self):
  return lib.eciStop(self.eci)
 def registerCallback(self, func, user):
  lib.eciRegisterCallback(self.eci, func, user)
 def setOutputBuffer(self, samples, buf):
  lib.eciSetOutputBuffer(self.eci, samples, pointer(buf))
 def generatePhonemes(self, size, buf):
  return lib.eciGeneratePhonemes(self.eci, size, pointer(buf))
 def setVoiceParam(self, voice, param, val):
  lib.eciSetVoiceParam(self.eci, voice, param, val)
 def speaking(self):
  return lib.eciSpeaking(self.eci) & 0xf #why does this work
