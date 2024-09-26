import shutil
import json
import os

def to_texture_set(diffuse: str, mer_suffix: str, normal_suffix: str, depth_type: str, output_files_dir: str):
    texture_set: dict = {
        "format_version": "1.16.100",
        "color": diffuse,
        # "metalness_emissive_roughness_subsurface"
        "metalness_emissive_roughness": f"{diffuse}_{mer_suffix}",
        depth_type: f"{diffuse}_{normal_suffix}",
    }

    json_file_path: str = os.path.join(output_files_dir, f"{diffuse}.texture_set.json")
    with open(json_file_path, "w", encoding="utf-8") as name:
        json.dump(texture_set, name, indent=4)
    print(f"Created JSON file: {json_file_path}")


def move_files(output: str, itm: str, PATH: str, texture: str):
    if ".json" in itm:
        source_path: str = os.path.join(output, itm)
        destination_path: str = os.path.join(PATH, texture)
        shutil.move(source_path, destination_path)
        print(f"Moved {itm} to {PATH}")


def create_json(itm: str, MER_SUFFIX: str, NORMAL_SUFFIX: str, DEPTH_TYPE: str, output_files_dir: str):
    hasSuffix: bool = f"_{MER_SUFFIX}.png" in itm or f"_{NORMAL_SUFFIX}.png" in itm
    hasExtension: bool = ".png" in itm or ".tga" in itm
    if not hasSuffix and hasExtension:
        texture_name: str = itm[:-4]
        to_texture_set(texture_name, MER_SUFFIX, NORMAL_SUFFIX, DEPTH_TYPE, output_files_dir)
