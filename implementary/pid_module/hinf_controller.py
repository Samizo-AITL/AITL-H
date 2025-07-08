# hinf_controller.py

import numpy as np
from scipy import signal

class HinfController:
    """
    H∞制御器の簡易実装クラス。
    LTIモデルに基づいた周波数応答設計に対応。
    """

    def __init__(self, A, B, C, D):
        """
        状態空間モデル (A, B, C, D) をもとに制御器を初期化。
        """
        self.sys = signal.StateSpace(A, B, C, D)

    def simulate_response(self, u, t):
        """
        入力 u（時間軸に沿ったベクトル）に対する出力応答を計算。
        """
        t_out, y_out, x_out = signal.lsim(self.sys, U=u, T=t)
        return t_out, y_out

    def frequency_response(self):
        """
        Bodeプロットなどに使用できる周波数応答を返す。
        """
        w, mag, phase = signal.bode(self.sys)
        return w, mag, phase
