import sys
import os
import json
import shutil

# insert path for your texture files here.
# *make sure to use a valid folder path
path = r'Your path here.'
files = os.listdir(path)

main_dir = os.path.realpath(__file__)
output_files = os.listdir(main_dir[:-7])

# MER and normal suffixes
# *do not include anything besides the suffix
merSuffix = "mer"
normalSuffix = "normal"
# choose type of depth map(heightmap or normal)
depthType = "normal"

#* DO NOT CHANGE ANYTHING HERE
def textureSet(texture_name, mer_suffix, normal_suffix, depth_type):
    texture_set = {
        "format_version": "1.16.100",
        "color": texture_name,
        "metalness_emissive_roughness": texture_name + "_" + mer_suffix,
        depth_type: texture_name + "_" + normal_suffix
    }
    with open(texture_name + ".texture_set.json", "w") as name:
        json.dump(texture_set, name, indent=4)

for item in files:
    if (not ("_" + merSuffix + ".png" in item or "_" + normalSuffix + ".png" in item) and ".png" in item):
        print(item[:-4])
        textureSet(item[:-4], merSuffix, normalSuffix, depthType)
        

for item in output_files:
    if (".json" in item):
        shutil.move(os.path.join(main_dir[:-7], item), path)
        
print(output_files)
sys.exit()
