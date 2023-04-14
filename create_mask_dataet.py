from pathlib import Path
from read_convert_save import save_mask_image

import time


read_at = Path.cwd().parent / "dataset/square"
save_at = Path.cwd().parent / "dataset/masked/mask_square"


for image in read_at.glob("*.jpg"):
    IMAGE = str(image)
    result_file_name = f"{str(save_at)}/mask_{image.name}"
    try:
        print(save_mask_image(IMAGE, result_file_name))
    except Exception as e:
        print("### ERROR : ", IMAGE, " ", str(e))

    time.sleep(2)




