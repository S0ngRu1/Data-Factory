# -*- coding: utf-8 -*-
# @Time : 2024/10/30 22:44
# @Author : CSR
# @File : test_epstoemf.py

import os
import ghostscript
from PIL import Image

def eps_to_emf(eps_path, emf_path):
    # 使用 Ghostscript 将 EPS 转换为位图（PNG）
    png_path = "temp_image.png"  # 临时 PNG 文件
    args = [
        "eps2png",  # 命令名，可以是任意字符串
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=png16m",  # 输出设备为 PNG
        f"-sOutputFile={png_path}",  # 输出文件路径
        eps_path  # 输入 EPS 文件路径
    ]

    ghostscript.Ghostscript(*args)

    # 使用 Pillow 将 PNG 转换为 EMF
    with Image.open(png_path) as img:
        img.save(emf_path, format='EMF')

    # 删除临时 PNG 文件
    os.remove(png_path)

if __name__ == "__main__":
    eps_file = "../data/论文绘图1.eps"  # 输入的 EPS 文件路径
    emf_file = "output.emf"  # 输出的 EMF 文件路径
    eps_to_emf(eps_file, emf_file)
    print(f"Converted {eps_file} to {emf_file}")

