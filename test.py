# -*- coding: utf-8 -*-
# @Time : 11/13/24 10:55 PM
# @Author : CSR
# @File : test.py.py
import numpy as np
import rasterio
from scipy.signal import convolve


def gaussian_filter(wavelength, peak_wavelength, amplitude, width):
    """生成高斯滤波器"""
    return amplitude * np.exp(-((wavelength - peak_wavelength) ** 2) / (2 * width ** 2))


def match_filter_convolution(spectrum, filter):
    """执行匹配滤波器卷积"""
    return convolve(spectrum, filter, mode='same')


def read_tiff(file_path):
    """读取TIFF文件"""
    with rasterio.open(file_path) as src:
        data = src.read(1)  # 读取第一个波段
        wavelength = np.linspace(src.bounds.left, src.bounds.right, data.shape[1])
        return wavelength, data


def main():
    # TIFF文件路径
    file_path = 'path_to_your_tiff_file.tif'  # 替换为你的TIFF文件路径

    # 读取TIFF文件
    wavelength, spectrum = read_tiff(file_path)

    # 甲烷的吸收峰波长和高斯滤波器的参数
    peak_wavelength = 1.65  # 甲烷的吸收峰波长
    amplitude = 1.0  # 高斯滤波器的振幅
    width = 0.01  # 高斯滤波器的宽度

    # 生成匹配滤波器
    filter = gaussian_filter(wavelength, peak_wavelength, amplitude, width)

    # 执行匹配滤波器卷积
    convolution_result = match_filter_convolution(spectrum, filter)

    # 找到卷积结果的最大值对应的位置
    max_index = np.argmax(convolution_result)

    # 计算甲烷柱浓度（这里只是一个示例，实际计算需要根据具体情况调整）
    column_concentration = spectrum[max_index] / amplitude

    # 打印结果
    print(f"Estimated Methane Column Concentration: {column_concentration}")
    print(f"Wavelength at Max Concentration: {wavelength[max_index]}")

    # 保存结果到文件
    output_file_path = 'methane_column_concentration.txt'  # 输出文件的路径
    with open(output_file_path, 'w') as file:
        file.write(f"Estimated Methane Column Concentration: {column_concentration}\n")
        file.write(f"Wavelength at Max Concentration: {wavelength[max_index]}\n")

    print(f"Results have been saved to {output_file_path}")


if __name__ == '__main__':
    main()