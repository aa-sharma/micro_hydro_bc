# MICRO-HYDROPOWER SITE SUITABILITY MAP

> The purpose of this project is to conduct a feasibility study to identify candidate locations for micro-hydropower development in Southwest BC considering terrain, river proximity, infrastructure access, and environmental constraints.


## OVERVIEW

Deliverables: suitability map, ranked candidate sites layer, short report

Software: QGIS, Python, Git

Study Area Definition:
This feasibility analysis will be focused in the specific region of Southwest British Columbia, Canada (Squamish-Lillooet and Sunshine Coast regions) given the mountainous terrain, many streams, grid access, and manageable data sets.

## DATASET & LAYERS
1. Elevation (DEM) - _Source: https://a100.gov.bc.ca/ext/mtec/public/products/mapsheet_
2. Rivers and Streams - _Source: https://catalogue.data.gov.bc.ca/dataset/freshwater-atlas-stream-network_
3. Protected Areas - _Source: https://catalogue.data.gov.bc.ca/dataset/bc-parks-ecological-reserves-and-protected-areas_
4. Roads - _Source: https://catalogue.data.gov.bc.ca/dataset/digital-road-atlas-dra-demographic-partially-attributed-roads_
5. Transmission Lines - _Source: https://catalogue.data.gov.bc.ca/dataset/bc-transmission-lines_

## SUITABILITY CRITERIA

Each factor (elevation, proximity to river/stream, protected areas, proximity to road, and transmission lines) is converted to a score. A weighted sum is used to  provide final suggestions on ideal micro-hydro power project locations in Southwest BC.

### Criterion 1: Elevation
Rationale: Higher elevation provides higher potential (\(E_p = mgh\)

|    Slope   | Score |
| ---------- | ----- |
| 0-5 deg.   |   1   |
| 5-10 deg.  |   2   |
| 10-15 deg. |   3   |
| 15-25 deg. |   4   |
| >25 deg.   |   5   |

### Criterion 2: Proximity to Streams/Rivers
Rationale: Easier access to flowing water

| Distance  | Score |
| --------- | ----- |
|   <500m   |   5   |
| 500-800m  |   4   |
| 800-1000m |   3   |
|   1-2km   |   2   |
|   >2km    |   1   |

### Criterion 3: Proximity to Roads
Rationale: More efficient with respect to access, cost, and safety

| Distance | Score |
| -------- | ----- |
|   <1km   |   5   |
|   1-3km  |   4   |
|   3-4km  |   3   |
|   4-5km  |   2   |
|   >5km   |   1   |


### Criterion 4: Protected Areas
1. Inside protected area = x0
2. Outside protected area = x1


### Criterion 5: Proximity to Transmission Lines
Rationale: Minimizes energy loss, and reduces construction costs/time

| Distance | Score |
| -------- | ----- |
|   <1km   |   5   |
|   1-3km  |   4   |
|   3-4km  |   3   |
|   4-5km  |   2   |
|   >5km   |   1   |


### Weighted Sum
Suitability_i = (40% Elevation Score) + (30% Stream Score) + (15% Road Score) + (15% Transmission Line Score)

Suitability_f = Suitability_i x (Protected Areas Constraint)


## ASSUMPTIONS
_Note: GIS raw data not included in repo_
