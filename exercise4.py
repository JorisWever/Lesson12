## Geo-Scripting WUR
## Joris Wever, Erwin van den Berg
## 19-Jan-2016
## Lesson 12
## Game Of Life

# ! run this script in the ArcGIS python console

# Import modules
import arcpy
from arcpy.sa import *

# set working directory
arcpy.env.workspace = "E:\Part4"
arcpy.env.overwriteOutput = True

# Construct local variables:
startraster = "E:\\Part4\\startraster"
kernel = "Irregular E:\\Part4\\kernel.txt"
focal = "E:\\Part4\\focal"

for i in range(1, 21):
    OutStage = "E:\\Part4\\GameOfLife\\GameOfLife.gdb\\stage" + str(i)

    # All stages except Stage 1
    if(i != 1):
        LastStage = "E:\\Part4\\GameOfLife\\GameOfLife.gdb\\stage" + str(i-1)
        # Process: Focal Statistics
        arcpy.gp.FocalStatistics_sa(LastStage, focal, kernel, "SUM", "DATA")

        # Process: Raster Calculator
        outRaster = Con(Raster(LastStage) == 1,Con(Raster(focal) < 2, 0,Con((Raster(focal) == 2)|(Raster(focal) == 3), 1,Con(Raster(focal) > 3, 0))),Con(Raster(focal) == 3, 1, 0))
        outRaster.save(OutStage)

    # (Only) Stage 1       
    else:
        # Process: Focal Statistics
        arcpy.gp.FocalStatistics_sa(startraster, focal, kernel, "SUM", "DATA")

        # Process: Raster Calculator
        outRaster = Con(Raster(startraster) == 1,Con(Raster(focal) < 2, 0,Con((Raster(focal) == 2)|(Raster(focal) == 3), 1,Con(Raster(focal) > 3, 0))),Con(Raster(focal) == 3, 1, 0))
        outRaster.save(OutStage)
