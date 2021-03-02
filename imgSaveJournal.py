# NX 1957
# Journal created by Amalie on Tue Mar  2 14:12:48 2021 Vest-Europa (normaltid)
#
import math
import NXOpen
import NXOpen.Gateway
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
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
    
    imageExportBuilder1.FileName = "C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\theProduct.png"
    
    imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
    
    imageExportBuilder1.EnhanceEdges = False
    
    nXObject1 = imageExportBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId1, "Export Image")
    
    imageExportBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()