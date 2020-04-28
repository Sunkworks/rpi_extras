#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys


# Assumed format of file:
# Gyro \t Accelerometer \t Calculated Angle \n
# TODO: add header row

def parse_file(filename: str):
    gyro_data, acc_data, filter_data = [], [], []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            gyro, acc, complimentary = (float(x) for x in line.split())
            gyro_data.append(gyro)
            acc_data.append(acc)
            filter_data.append(complimentary)

    return np.array(gyro_data), np.array(acc_data), np.array(filter_data)


def main():
    print(f"Reading from: {sys.argv[1]}")
    filename = sys.argv[1]
    #filename = "data.txt"
    gyro_data, acc_data, filter_data = parse_file(filename)
    entry_count = len(gyro_data)
    x = np.linspace(0, 100, entry_count)
    plt.plot(x, gyro_data, label="Gyroscope")
    plt.plot(x, acc_data, label="Accelerometer")
    plt.plot(x, filter_data, label="Complimentary Filter")
    plt.xlabel("time [as percentage]")
    plt.ylabel("angle [°]")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
