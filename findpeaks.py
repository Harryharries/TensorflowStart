from scipy import signal
import numpy as np
xs = np.arange(0, np.pi, 0.05)
data = np.sin(xs)
peakind = signal.find_peaks_cwt(data, np.arange(1,10))
print(xs)
print(peakind)
print(xs[peakind])
print(data[peakind])