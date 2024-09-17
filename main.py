import sys
import os
import json
import shutil

# Insert path for your texture files here.
PATH = r'C:\Users\cyncxd\Desktop\block'
files = os.listdir(PATH)

# Get the directory of the script
main_dir = os.path.dirname(os.path.abspath(__file__))
output_files_dir = os.path.join(main_dir, PATH)

# MER and normal suffixes
MER_SUFFIX = "s"
NORMAL_SUFFIX = "n"
DEPTH_TYPE = "normal"

def to_texture_set(diffuse, mer_suffix, normal_suffix, depth_type):
    texture_set = {
        "format_version": "1.16.100",
        "color": diffuse,
        "metalness_emissive_roughness": diffuse + "_" + mer_suffix,
        depth_type: diffuse + "_" + normal_suffix
    }
    json_file_path = os.path.join(output_files_dir, diffuse + ".texture_set.json")
    with open(json_file_path, "w", encoding="utf-8") as name:
        json.dump(texture_set, name, indent=4)
    print(f"Created JSON file: {json_file_path}")

# Create texture set JSON files
for item in files:
    hasSuffix = "_" + MER_SUFFIX + ".png" in item or "_" + NORMAL_SUFFIX + ".png" in item
    hasExtension = ".png" in item or ".tga" in item
    if not hasSuffix and hasExtension:
        texture_name = item[:-4]
        to_texture_set(texture_name, MER_SUFFIX, NORMAL_SUFFIX, DEPTH_TYPE)

# Move JSON files to the specified path
output_files = os.listdir(output_files_dir)
for texture in output_files:
    if '.json' in texture:
        source_path = os.path.join(output_files_dir, texture)
        destination_path = os.path.join(PATH, texture)
        shutil.move(source_path, destination_path)
        print(f"Moved {texture} to {PATH}")

sys.exit()
