import av
import os
import numpy as np
from PIL import Image

val_path = r"D:\Dataset\5food\val.txt"
img_head = r"D:\Dataset\5food"


def encode_and_write(img_list):
    with av.open('val.mp4', 'w') as container:
        stream = container.add_stream('libx264', '60')
        stream.pix_fmt = 'yuv420p'

        # stream.width = 320
        # stream.height = 240

        stream.options["crf"] = "15"  # for libx264, 0-51, 0 is lossless.

        # encoding
        for img_path in img_list:
            with Image.open(img_path) as image:
                img = np.asarray(image)

            frame = av.VideoFrame.from_ndarray(img)
            for packet in stream.encode(frame):
                container.mux(packet)

        # flush
        for packet in stream.encode():
            container.mux(packet)

if __name__ == '__main__':

    all_files = []
    with open(val_path, 'r') as f:
        for line in f:
            img_path = os.path.join(img_head, line.strip())
            all_files.append(img_path)
            # with Image.open(img_path) as image:
            #     img = np.asarray(image)
            #     print(img.shape)
            # break

    encode_and_write(all_files)