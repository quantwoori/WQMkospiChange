import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class BrownianMotion:
    def __init__(self, initial:int=0):
        # CONSTANT
        self.INIT = initial

    def gen_rand_normal(self, mean, std, step) -> np.ndarray:
        """
        :param mean: mean of daily rate of return
        :param std: standard deviation of daily rate of return
        :param step: step size?
        """
        w = np.ones(step) * 0
        for i in range(1, step):
            x = np.random.normal(
                loc=mean,
                scale=std
            )
            w[i] = w[i - 1] + (x / np.sqrt(step))
        return w

    def gen_scaled_brownian(self, mean, std, step):
        return self.gen_rand_normal(mean, std, step) * self.INIT + self.INIT
