# NX 1957
# Journal created by andreilo on Sun Feb 21 22:08:30 2021 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Gateway
from time import sleep
from threading import Timer
import os

pathToDFA = "C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\DFAs\\My_Chair_order.dfa"
pathToImg = "C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\theProduct.png"
lastTimeFileChange = 0.0

class RepeatedTimer(object):
	def __init__(self, interval, function, *args, **kwargs):
		self._timer	 = None
		self.interval   = interval
		self.function   = function
		self.args	   = args
		self.kwargs	 = kwargs
		self.is_running = False
		self.start()

	def _run(self):
		self.is_running = False
		self.start()
		self.function(*self.args, **self.kwargs)

	def start(self):
		if not self.is_running:
			self._timer = Timer(self.interval, self._run)
			self._timer.start()
			self.is_running = True

	def stop(self):
		self._timer.cancel()
		self.is_running = False
		



def main() : 

	theSession  = NXOpen.Session.GetSession()
	workPart = theSession.Parts.Work
	displayPart = theSession.Parts.Display
	workPart.RuleManager.Reload(True)
	
	"""
	sleep(2)
	# ----------------------------------------------
	#   Menu: File->Export->Image...
	# ----------------------------------------------
	markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
	
	theUI = NXOpen.UI.GetUI()
	
	imageExportBuilder1 = theUI.CreateImageExportBuilder()
	
	imageExportBuilder1.RegionMode = False
	
	regiontopleftpoint1 = [None] * 2 
	regiontopleftpoint1[0] = 0
	regiontopleftpoint1[1] = 0
	imageExportBuilder1.SetRegionTopLeftPoint(regiontopleftpoint1)
	
	imageExportBuilder1.RegionWidth = 1
	
	imageExportBuilder1.RegionHeight = 1
	
	imageExportBuilder1.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png
	
	imageExportBuilder1.FileName = pathToImg
	
	imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
	
	imageExportBuilder1.EnhanceEdges = False
	
	nXObject1 = imageExportBuilder1.Commit()
	
	theSession.DeleteUndoMark(markId1, "Export Image")
	
	imageExportBuilder1.Destroy()
	
	
	# ----------------------------------------------
	#   Menu: Tools->Journal->Stop Recording
	# ----------------------------------------------
	
	"""

"""	
if __name__ == '__main__':
	main()
"""	

def imgSaver(path):
	#Read the change of the DFA file
	global lastTimeFileChange
	fileLastChanged = os.path.getmtime(pathToDFA)
	#Check if it is > lastTimeFileChange
	if (fileLastChanged > lastTimeFileChange):
		lastTimeFileChange = fileLastChanged
		#If yes, generate new image
		main()
		print("Image file has been saved")
	#else, skip.
   

print("starting...")
# First param - is the frequency
# Second param - is the function
# Third param - path of image
rt = RepeatedTimer(5, imgSaver, pathToImg) # it auto-starts, no need of rt.start()
try:
	sleep(25) # your long-running job goes here...
finally:
	rt.stop() # better in a try/finally block to make sure the program ends!
