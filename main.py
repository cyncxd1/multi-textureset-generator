import os
import functions as func

PATH: str = input(r"Paste your block folder path here: ")
files: list[str] = os.listdir(PATH)

main_dir: str = os.path.dirname(os.path.abspath(__file__))
output_files_dir: str = os.path.join(main_dir, PATH)

MER_SUFFIX: str = input("What suffix do you use for MER? *Exlude underscores\n")
DEPTH_TYPE: str = input("Do you use [heightmap] or [normal]?\n")
NORMAL_SUFFIX: str = input(f"What suffix do you use for {DEPTH_TYPE}s? *Exlude underscores?\n")

for item in files:
    func.create_json(item, MER_SUFFIX, NORMAL_SUFFIX, DEPTH_TYPE, output_files_dir)

output_files: list[str] = os.listdir(output_files_dir)
for texture in output_files:
    func.move_files(output_files_dir, texture, PATH, texture)

input("Press enter to exit\n")
