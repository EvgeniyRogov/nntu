from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np

window = signal.parzen(5).transpose()
plt.plot(window)
plt.title("Parzen window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

print(window)

# plt.figure()
# A = fft(window, 2048) / (len(window)/2.0)
# freq = np.linspace(-0.5, 0.5, len(A))
# response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
# plt.plot(freq, response)
# plt.axis([-0.5, 0.5, -120, 0])
# plt.title("Frequency response of the Parzen window")
# plt.ylabel("Normalized magnitude [dB]")
# plt.xlabel("Normalized frequency [cycles per sample]")
# plt.show()