from osgeo import gdal
import numpy as np

# Input slope raster
input_raster = "data_processed/slope.tif"
output_raster = "data_processed/slope_score.tif"

ds = gdal.Open(input_raster)
band = ds.GetRasterBand(1)
arr = band.ReadAsArray()

# Reclassify
reclass = np.zeros_like(arr)

reclass[(arr >= 0) & (arr < 5)] = 1
reclass[(arr >= 5) & (arr < 15)] = 2
reclass[(arr >= 15) & (arr < 25)] = 4
reclass[arr >= 25] = 5

# Create output
driver = gdal.GetDriverByName("GTiff")
out_ds = driver.Create(
    output_raster,
    ds.RasterXSize,
    ds.RasterYSize,
    1,
    gdal.GDT_Float32
)

out_ds.SetGeoTransform(ds.GetGeoTransform())
out_ds.SetProjection(ds.GetProjection())

out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(reclass)
out_band.FlushCache()

out_ds = None
ds = None

print("Slope reclassification complete")
