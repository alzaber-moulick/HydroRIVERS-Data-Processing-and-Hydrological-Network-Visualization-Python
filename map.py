import os
import glob
import zipfile
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import osmnx as ox

zip_path = "HydroRIVERS_v10_as_shp.zip"
url = "https://data.hydrosheds.org/file/hydrorivers/HydroRIVERS_v10_as_shp.zip"

shp_files = glob.glob("**/HydroRIVERS_v10_as.shp", recursive=True)

if not shp_files:
    if not os.path.exists(zip_path):
        print("Downloading HydroRIVERS Asia dataset (~125 MB)... Please wait.")
        response = requests.get(url, stream=True)
        with open(zip_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
    
    print("Extracting ZIP file...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(".")
    
    shp_files = glob.glob("**/HydroRIVERS_v10_as.shp", recursive=True)

shp_path = shp_files[0]

print("Fetching National Boundary of Bangladesh...")
bd_boundary = ox.geocode_to_gdf("Bangladesh")

print("Loading Shapefile and Clipping for Bangladesh...")
rivers = gpd.read_file(shp_path)
bd_rivers = gpd.clip(rivers, bd_boundary)

print("Rendering multi-color vibrant map with centered title...")
fig, ax = plt.subplots(figsize=(14, 16), facecolor='black')
ax.set_facecolor('black')

bd_boundary.plot(
    ax=ax, 
    facecolor='none', 
    edgecolor='#444444', 
    linewidth=1.2, 
    linestyle='--', 
    alpha=0.7
)

color_palette = {
    1: {'color': '#FF0055', 'label': 'Major Rivers (Padma & Jamuna) - Neon Red', 'width': 3.5},
    2: {'color': '#FF9900', 'label': 'Secondary Rivers - Bright Orange', 'width': 2.3},
    3: {'color': '#FFEE00', 'label': 'Tributaries - Electric Yellow', 'width': 1.6},
    4: {'color': '#00FF66', 'label': 'Regional Streams - Neon Green', 'width': 1.1},
    5: {'color': '#00FFFF', 'label': 'Minor Channels - Bright Cyan', 'width': 0.8},
    6: {'color': '#B000FF', 'label': 'Inland Streams - Vibrant Purple', 'width': 0.6},
    7: {'color': '#FF00CC', 'label': 'Micro Streams - Hot Pink', 'width': 0.4}
}

legend_elements = [
    Line2D([0], [0], color='#444444', lw=1.2, linestyle='--', label='National Boundary')
]

for ord_val, config in color_palette.items():
    sub_rivers = bd_rivers[bd_rivers['ORD_CLAS'] == ord_val]
    if not sub_rivers.empty:
        sub_rivers.plot(ax=ax, color=config['color'], linewidth=config['width'], alpha=0.95)
        
        legend_elements.append(
            Line2D([0], [0], color=config['color'], lw=config['width'], label=config['label'])
        )

plt.suptitle(
    "BANGLADESH RIVER NETWORK", 
    color='white', 
    fontsize=22, 
    fontweight='bold', 
    x=0.5, 
    y=0.95, 
    ha='center'
)
plt.title(
    "Multi-Color Drainage Classification | HydroSHEDS Data", 
    color='#B0BEC5', 
    fontsize=11, 
    pad=15, 
    loc='center'
)

legend = ax.legend(
    handles=legend_elements,
    loc='lower left',
    frameon=True,
    facecolor='#111111',
    edgecolor='#333333',
    fontsize=9.5,
    labelcolor='white',
    title="River Hierarchies (Multi-Color)",
    title_fontsize=11
)
legend.get_title().set_color('white')
legend.get_title().set_weight('bold')

ax.annotate('N', xy=(0.93, 0.93), xytext=(0.93, 0.88),
            ha='center', va='center', fontsize=14, fontweight='bold', color='white',
            xycoords='axes fraction', textcoords='axes fraction',
            arrowprops=dict(facecolor='white', edgecolor='white', width=2, headwidth=8))

ax.text(
    0.5, 0.5, 
    "Md. Alzaber", 
    transform=ax.transAxes, 
    color='white', 
    fontsize=60, 
    fontweight='bold', 
    alpha=0.10, 
    rotation=35, 
    ha='center', 
    va='center'
)

ax.text(
    0.98, 0.02, 
    "Cartography by: Md. Alzaber", 
    transform=ax.transAxes, 
    color='#888888', 
    fontsize=10, 
    fontweight='bold', 
    ha='right', 
    va='bottom'
)

ax.set_axis_off()
plt.tight_layout()

output_file = "Bangladesh_MultiColor_River_Basin_Md_Alzaber_4K.png"
plt.savefig(
    output_file, 
    dpi=600, 
    facecolor='black', 
    edgecolor='none', 
    bbox_inches='tight', 
    transparent=False
)
print(f"Done! Multi-color national map saved as '{output_file}'.")
