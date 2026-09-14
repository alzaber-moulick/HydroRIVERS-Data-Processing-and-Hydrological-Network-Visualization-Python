# 🌊 HydroRIVERS Spatial Data Pipeline & Hydrological Network Visualization

## 📌 Overview & Technical Architecture
High-resolution hydrological network visualization requires efficient vector processing, spatial topology handling, and dynamic stream classification. Standard GIS applications often struggle to dynamically filter and render multi-scale river reach hierarchies smoothly without pre-configured symbology.

This project features an automated, end-to-end Python spatial data engineering pipeline utilizing global **HydroRIVERS (HydroSHEDS v1.0)** datasets. The programmatically built workflow downloads hydrographic shapefiles, clips hydrographic networks using OpenStreetMap (OSM) administrative boundaries, and renders publication-grade 4K dark-mode maps based on classical drainage order (`ORD_CLAS`).

---

## 📸 High-Resolution Output Showcase

### 1. National Level: Bangladesh Multi-Color River Hierarchy
<p align="center">
  <img src="assets/Bangladesh_MultiColor_River_Basin_Md_Alzaber_4K.png" alt="Bangladesh MultiColor River Basin Map" width="100%">
</p>



## 🛠️ Spatial Processing Pipeline Workflow

1. **Automated Vector Acquisition:** Downloads and extracts global HydroRIVERS Asia dataset (`HydroRIVERS_v10_as.shp`) directly from HydroSHEDS servers upon execution.
2. **Dynamic Administrative Boundary Clipping:** Integrates `OSMnx` to fetch polygon boundaries on-the-fly and clips line vector layers using `GeoPandas`.
3. **Stream Order Classification (`ORD_CLAS`):** Classifies hydrographic networks across 7 distinct stream hierarchies, assigning custom line weights and neon color profiles dynamically:
   - **Order 1 (Neon Red):** Major Rivers (Padma & Jamuna)
   - **Order 2 (Bright Orange):** Secondary Rivers (Ichhamati, Dhaleshwari, etc.)
   - **Order 3 (Electric Yellow):** Tributaries & Regional Streams
   - **Order 4–7 (Green, Cyan, Purple, Hot Pink):** Minor Channels, Inland Streams, and Micro Canals
4. **Publication-Grade Cartography:** Renders aesthetic dark-mode maps with scale indicators, cardinal orientation arrows, custom legends, and watermark overlays.

---

## 📊 Technical Data Schema (HydroRIVERS Data)

The underpinning vector processing pipeline leverages key hydrographic attributes:
- `ORD_CLAS`: Classical river order classification (used for color mapping)
- `ORD_STRA`: Strahler ordering system
- `DIS_AV_CMS`: Long-term average discharge ($m^3/s$)
- `UPLAND_SKM`: Total upstream catchment area ($km^2$)

---

## 🧰 Tech Stack & Python Libraries
- **Geospatial Processing:** `GeoPandas`, `OSMnx`, `Shapely`
- **Visualization & Rendering:** `Matplotlib`, `Matplotlib.lines`
- **Data Transfer & Automation:** `requests`, `zipfile`, `glob`, `os`
- **Data Source:** HydroSHEDS / HydroRIVERS v1.0 (McGill University / WWF)

---

## 🚀 Quick Start & Execution

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/HydroRIVERS-Data-Processing-and-Hydrological-Network-Visualization-Python.git](https://github.com/YOUR_USERNAME/HydroRIVERS-Data-Processing-and-Hydrological-Network-Visualization-Python.git)
cd HydroRIVERS-Data-Processing-and-Hydrological-Network-Visualization-Python
