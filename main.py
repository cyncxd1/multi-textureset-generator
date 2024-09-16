import sys
import os
import json
import shutil

# Insert path for your texture files here.
path = r'C:\Users\cyncxd\Desktop\block'
files = os.listdir(path)

# Get the directory of the script
main_dir = os.path.dirname(os.path.abspath(__file__))
output_files_dir = os.path.join(main_dir, path)  # Adjust as necessary

# MER and normal suffixes
merSuffix = "mer"
normalSuffix = "normal"
depthType = "normal"

def textureSet(texture, mer_suffix, normal_suffix, depth_type):
    texture_set = {
        "format_version": "1.16.100",
        "color": texture,
        "metalness_emissive_roughness": texture + "_" + mer_suffix,
        depth_type: texture + "_" + normal_suffix
    }
    json_file_path = os.path.join(output_files_dir, texture + ".texture_set.json")
    with open(json_file_path, "w", encoding="utf-8") as name:
        json.dump(texture_set, name, indent=4)
    print(f"Created JSON file: {json_file_path}")

# Create texture set JSON files
for item in files:
    hasSuffix = "_" + merSuffix + ".png" in item or "_" + normalSuffix + ".png" in item
    if (not (hasSuffix) and ".png" in item):
        texture_name = item[:-4]
        textureSet(texture_name, merSuffix, normalSuffix, depthType)

# Move JSON files to the specified path
output_files = os.listdir(output_files_dir)
for texture in output_files:
    if '.json' in texture:
        source_path = os.path.join(output_files_dir, texture)
        destination_path = os.path.join(path, texture)
        shutil.move(source_path, destination_path)
        print(f"Moved {texture} to {path}")

sys.exit()
