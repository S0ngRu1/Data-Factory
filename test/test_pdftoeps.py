# -*- coding: utf-8 -*-
# @Time : 2024/10/30 22:26
# @Author : CSR
# @File : test_pdftoeps.py

import os
import ghostscript

def pdf_to_eps(pdf_path, eps_path):
    # 定义 Ghostscript 参数
    args = [
        "ps2eps",  # 命令名，可以是任意字符串
        "-dNOPAUSE",  # 不暂停
        "-dBATCH",  # 批处理模式
        "-sDEVICE=eps2write",  # 输出设备为 EPS
        f"-sOutputFile={eps_path}",  # 输出文件路径
        pdf_path  # 输入 PDF 文件路径
    ]

    # 调用 Ghostscript
    ghostscript.Ghostscript(*args)

if __name__ == "__main__":
    pdf_file = "input.pdf"  # 输入的 PDF 文件路径
    eps_file = "output.eps"  # 输出的 EPS 文件路径
    pdf_to_eps(pdf_file, eps_file)
    print(f"Converted {pdf_file} to {eps_file}")
