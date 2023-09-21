#模块调用
import numpy as np
import math
import pywt


def wavelet_denoising(signal):
    # signal: list
    wavelet_basis = 'db8'  # 此处选择db8小波基
    w = pywt.Wavelet(wavelet_basis)
    maxlevel = pywt.dwt_max_level(len(signal), w.dec_len)  # 根据数据长度计算分解层数

    threshold = 0.7  # threshold for filtering
    coeffs = pywt.wavedec(signal, wavelet_basis, level=maxlevel)  # 将信号进行小波分解
    # 使用阈值滤除噪声
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * max(coeffs[i]))  # 将噪声滤波
        # pywt.threshold 方法有三种阈值模式：硬阈值、软阈值、软硬结合
        # 默认为soft 软阈值模式，其调用格式为
        # pywt.threshold(signal, threshold_value, mode='soft', substitute=0)
        # 处理后值为 signal/np.abs(signal) * np.maximum(np.abs(signal) - threshold_value, 0)
        # 具体可参考pywavelets官方文档的说明
    # 重建信号
    signalrec = pywt.waverec(coeffs, wavelet_basis)
    return signalrec