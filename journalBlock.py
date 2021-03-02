# NX 1957
# Journal created by Amalie on Tue Mar  2 13:51:22 2021 Vest-Europa (normaltid)
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Insert->Sketch
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Update Model from Sketch")
    
    theSession.BeginTaskEnvironment()
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    simpleSketchInPlaceBuilder1 = workPart.Sketches.CreateSimpleSketchInPlaceBuilder()
    
    theSession.SetUndoMarkName(markId3, "Create Sketch Dialog")
    
    simpleSketchInPlaceBuilder1.UseWorkPartOrigin = False
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction1 = workPart.Directions.CreateDirection(origin2, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 1.0, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    simpleSketchInPlaceBuilder1.CoordinateSystem = cartesianCoordinateSystem1
    
    theSession.Preferences.Sketch.CreateInferredConstraints = False
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = False
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = False
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.DisplayShadedRegions = True
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    theSession.Preferences.Sketch.EditDimensionOnCreation = True
    
    nXObject1 = simpleSketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId6)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    sketchFindMovableObjectsBuilder1 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject2 = sketchFindMovableObjectsBuilder1.Commit()
    
    sketchFindMovableObjectsBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId3, "Create Sketch")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    simpleSketchInPlaceBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    theSession.DeleteUndoMarksUpToMark(markId2, None, True)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Rectangle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId9, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using From Center method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(471.83709421692839, 0.90294687136781704, 0.0)
    endPoint1 = NXOpen.Point3d(-276.60838610129946, 382.25496665258953, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(-276.60838610129946, 382.25496665258953, 0.0)
    endPoint2 = NXOpen.Point3d(-471.83709421693965, -0.90294687136281482, 0.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(-471.83709421693965, -0.90294687136281482, 0.0)
    endPoint3 = NXOpen.Point3d(276.6083861012882, -382.25496665258453, 0.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(276.6083861012882, -382.25496665258453, 0.0)
    endPoint4 = NXOpen.Point3d(471.83709421692839, 0.90294687136781704, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    objects1 = [NXOpen.NXObject.Null] * 4 
    objects1[0] = sketchGeometricConstraint1
    objects1[1] = sketchGeometricConstraint2
    objects1[2] = sketchGeometricConstraint3
    objects1[3] = sketchGeometricConstraint4
    errorList1 = theSession.ActiveSketch.DeleteObjects(objects1)
    
    errorList1.Dispose()
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchFindMovableObjectsBuilder2 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject3 = sketchFindMovableObjectsBuilder2.Commit()
    
    sketchFindMovableObjectsBuilder2.Destroy()
    
    sketchFindMovableObjectsBuilder3 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject4 = sketchFindMovableObjectsBuilder3.Commit()
    
    sketchFindMovableObjectsBuilder3.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId11, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    
    curves1 = [NXOpen.ICurve.Null] * 4 
    curves1[0] = line1
    curves1[1] = line2
    curves1[2] = line3
    curves1[3] = line4
    seedPoint1 = NXOpen.Point3d(159.16637978250662, -128.94734208413684, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch1, curves1, seedPoint1, 0.01, selectionIntentRuleOptions1)
    
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(True)
    
    section1.AllowDegenerateCurves(False)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId14, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId13, None)
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)
    
    targetBodies5 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies5)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies6)
    
    targetBodies7 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies7)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId11, "Extrude")
    
    expression5 = extrudeBuilder1.Limits.StartExtend.Value
    expression6 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression3)
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression4)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId16, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies10)
    
    targetBodies11 = []
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies11)
    
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 140 {(-276.6083861012995,382.2549666525895,50)(-374.2227401591196,190.6760098906133,50)(-471.8370942169397,-0.9029468713629,50) EXTRUDE(2)}")
    point2 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction3 = workPart.Directions.CreateDirection(edge1, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 130 {(-0.0000000000056,0.0000000000025,50) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem2
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature3 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    simpleSketchInPlaceBuilder2 = workPart.Sketches.CreateSimpleSketchInPlaceBuilder()
    
    simpleSketchInPlaceBuilder2.CoordinateSystem = cartesianCoordinateSystem2
    
    simpleSketchInPlaceBuilder2.UseWorkPartOrigin = False
    
    theSession.Preferences.Sketch.CreateInferredConstraints = False
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = False
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = False
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.DisplayShadedRegions = True
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    theSession.Preferences.Sketch.EditDimensionOnCreation = True
    
    nXObject5 = simpleSketchInPlaceBuilder2.Commit()
    
    simpleSketchInPlaceBuilder2.Destroy()
    
    sketch2 = nXObject5
    sketch2.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    sketchFindMovableObjectsBuilder4 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject6 = sketchFindMovableObjectsBuilder4.Commit()
    
    sketchFindMovableObjectsBuilder4.Destroy()
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId18, None, True)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    objects2 = [NXOpen.NXObject.Null] * 1 
    objects2[0] = extrude1
    attributePropertiesBuilder1 = theSession.AttributeManager.CreateAttributePropertiesBuilder(workPart, objects2, NXOpen.AttributePropertiesBuilder.OperationType.NotSet)
    
    attributePropertiesBuilder1.IsArray = False
    
    attributePropertiesBuilder1.IsArray = False
    
    attributePropertiesBuilder1.IsArray = False
    
    attributePropertiesBuilder1.DataType = NXOpen.AttributePropertiesBaseBuilder.DataTypeOptions.String
    
    attributePropertiesBuilder1.Units = "MilliMeter"
    
    objects3 = [NXOpen.NXObject.Null] * 1 
    objects3[0] = extrude1
    featureGeneralPropertiesBuilder1 = workPart.PropertiesManager.CreateFeatureGeneralPropertiesBuilder(objects3)
    
    objects4 = [NXOpen.NXObject.Null] * 1 
    objects4[0] = extrude1
    attributePropertiesBuilder1.SetAttributeObjects(objects4)
    
    attributePropertiesBuilder1.Units = "MilliMeter"
    
    theSession.SetUndoMarkName(markId20, "Extrude Properties Dialog")
    
    attributePropertiesBuilder1.DateValue.DateItem.Day = NXOpen.DateItemBuilder.DayOfMonth.Day02
    
    attributePropertiesBuilder1.DateValue.DateItem.Month = NXOpen.DateItemBuilder.MonthOfYear.Mar
    
    attributePropertiesBuilder1.DateValue.DateItem.Year = "2021"
    
    attributePropertiesBuilder1.DateValue.DateItem.Time = "00:00:00"
    
    attributePropertiesBuilder1.Destroy()
    
    featureGeneralPropertiesBuilder1.Destroy()
    
    theSession.UndoToMark(markId20, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    scaleAboutPoint1 = NXOpen.Point3d(260.46675604687977, -71.971077328743178, 0.0)
    viewCenter1 = NXOpen.Point3d(-260.46675604687977, 71.971077328743178, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(208.3734048375037, -57.576861862994612, 0.0)
    viewCenter2 = NXOpen.Point3d(-208.37340483750395, 57.576861862994541, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(166.69872387000294, -46.06148949039563, 0.0)
    viewCenter3 = NXOpen.Point3d(-166.69872387000314, 46.06148949039563, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(133.35897909600226, -36.849191592316544, 0.0)
    viewCenter4 = NXOpen.Point3d(-133.3589790960026, 36.849191592316501, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(106.68718327680175, -29.479353273853235, 0.0)
    viewCenter5 = NXOpen.Point3d(-106.68718327680214, 29.479353273853203, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(85.349746621441369, -23.583482619082531, 0.0)
    viewCenter6 = NXOpen.Point3d(-85.349746621441724, 23.583482619082556, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(68.279797297153053, -18.866786095265983, 0.0)
    viewCenter7 = NXOpen.Point3d(-68.279797297153408, 18.866786095266111, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(54.623837837722412, -15.093428876212785, 0.0)
    viewCenter8 = NXOpen.Point3d(-54.623837837722753, 15.093428876212906, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(43.699070270177899, -12.074743100970201, 0.0)
    viewCenter9 = NXOpen.Point3d(-43.699070270178225, 12.074743100970323, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(34.9592562161423, -9.6597944807761618, 0.0)
    viewCenter10 = NXOpen.Point3d(-34.95925621614262, 9.6597944807762701, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(27.967404972913783, -7.7278355846209106, 0.0)
    viewCenter11 = NXOpen.Point3d(-27.9674049729141, 7.7278355846210243, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(22.373923978330996, -6.182268467696721, 0.0)
    viewCenter12 = NXOpen.Point3d(-22.373923978331305, 6.1822684676968329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(17.899139182664779, -4.9458147741573661, 0.0)
    viewCenter13 = NXOpen.Point3d(-17.899139182665092, 4.9458147741574781, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(14.319311346131776, -3.9566518193258791, 0.0)
    viewCenter14 = NXOpen.Point3d(-14.319311346132109, 3.9566518193259954, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(11.455449076905413, -3.1653214554606941, 0.0)
    viewCenter15 = NXOpen.Point3d(-11.455449076905721, 3.1653214554608087, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(9.1643592615242859, -2.5322571643685428, 0.0)
    viewCenter16 = NXOpen.Point3d(-9.1643592615246074, 2.5322571643686573, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(11.455449076905401, -3.1653214554606928, 0.0)
    viewCenter17 = NXOpen.Point3d(-11.455449076905708, 3.1653214554608073, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(14.319311346131807, -3.9566518193258799, 0.0)
    viewCenter18 = NXOpen.Point3d(-14.319311346132102, 3.9566518193259919, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(17.89913918266479, -4.9458147741573661, 0.0)
    viewCenter19 = NXOpen.Point3d(-17.899139182665088, 4.9458147741574781, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(22.373923978331035, -6.1822684676967237, 0.0)
    viewCenter20 = NXOpen.Point3d(-22.373923978331323, 6.1822684676968356, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(27.967404972913826, -7.7278355846209204, 0.0)
    viewCenter21 = NXOpen.Point3d(-27.967404972914114, 7.727835584621034, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(34.959256216142329, -9.6597944807761635, 0.0)
    viewCenter22 = NXOpen.Point3d(-34.959256216142613, 9.6597944807762719, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(43.699070270177941, -12.074743100970219, 0.0)
    viewCenter23 = NXOpen.Point3d(-43.699070270178233, 12.074743100970341, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(54.623837837722455, -15.093428876212771, 0.0)
    viewCenter24 = NXOpen.Point3d(-54.623837837722732, 15.093428876212908, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(68.27979729715311, -18.866786095265965, 0.0)
    viewCenter25 = NXOpen.Point3d(-68.279797297153394, 18.866786095266114, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(85.349746621441369, -23.583482619082531, 0.0)
    viewCenter26 = NXOpen.Point3d(-85.349746621441696, 23.583482619082609, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(106.6871832768017, -29.47935327385316, 0.0)
    viewCenter27 = NXOpen.Point3d(-106.6871832768021, 29.47935327385326, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(133.3589790960022, -36.849191592316444, 0.0)
    viewCenter28 = NXOpen.Point3d(-133.35897909600251, 36.849191592316529, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(166.69872387000274, -46.061489490395559, 0.0)
    viewCenter29 = NXOpen.Point3d(-166.69872387000322, 46.061489490395658, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(208.37340483750339, -57.576861862994434, 0.0)
    viewCenter30 = NXOpen.Point3d(-208.37340483750393, 57.576861862994562, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(260.46675604687937, -71.971077328742965, 0.0)
    viewCenter31 = NXOpen.Point3d(-260.46675604687982, 71.971077328743206, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(325.58344505859924, -89.963846660928695, 0.0)
    viewCenter32 = NXOpen.Point3d(-325.58344505859964, 89.963846660929107, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(406.97930632324903, -112.454808326161, 0.0)
    viewCenter33 = NXOpen.Point3d(-406.97930632324955, 112.45480832616126, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(508.72413290406161, -140.56851040770124, 0.0)
    viewCenter34 = NXOpen.Point3d(-508.72413290406161, 140.56851040770155, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(406.97930632324955, -112.454808326161, 0.0)
    viewCenter35 = NXOpen.Point3d(-406.97930632324903, 112.45480832616138, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    matrix2 = NXOpen.Matrix3x3()
    
    matrix2.Xx = 0.0
    matrix2.Xy = 1.0
    matrix2.Xz = 0.0
    matrix2.Yx = -1.0
    matrix2.Yy = 0.0
    matrix2.Yz = 0.0
    matrix2.Zx = 0.0
    matrix2.Zy = -0.0
    matrix2.Zz = 1.0
    workPart.ModelingViews.WorkView.Orient(matrix2)
    
    matrix3 = NXOpen.Matrix3x3()
    
    matrix3.Xx = 0.0
    matrix3.Xy = 1.0
    matrix3.Xz = 0.0
    matrix3.Yx = 0.0
    matrix3.Yy = 0.0
    matrix3.Yz = -1.0
    matrix3.Zx = -1.0
    matrix3.Zy = 0.0
    matrix3.Zz = 0.0
    workPart.ModelingViews.WorkView.Orient(matrix3)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.UndoToMark(markId17, None)
    
    theSession.DeleteUndoMark(markId17, None)
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    datumCsys1 = feature3
    nErrs2 = theSession.UpdateManager.AddToDeleteList(datumCsys1)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    extrudeBuilder2.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression7)
    
    theSession.UndoToMark(markId16, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()