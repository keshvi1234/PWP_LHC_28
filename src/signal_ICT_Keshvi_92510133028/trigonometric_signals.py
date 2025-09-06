import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """Generate a sine wave: A*sin(2πft + phi)"""
    signal = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title(f"Sine Wave: A={A}, f={f}Hz, phi={phi}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def cosine_wave(A, f, phi, t):
    """Generate a cosine wave: A*cos(2πft + phi)"""
    signal = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title(f"Cosine Wave: A={A}, f={f}Hz, phi={phi}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def exponential_signal(A, a, t):
    """Generate an exponential signal: A*e^(a*t)"""
    signal = A * np.exp(a * t)
    plt.plot(t, signal)
    plt.title(f"Exponential Signal: A={A}, a={a}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


# Testing section
if __name__ == "__main__":
    # Time vector from 0 to 1 second with 100 samples
    t = np.linspace(0, 1, 100)

    sine_wave(A=2, f=5, phi=0, t=t)      # Sine wave test
    cosine_wave(A=2, f=5, phi=0, t=t)    # Cosine wave test
    exponential_signal(A=1, a=2, t=t)    # Exponential growth
    exponential_signal(A=1, a=-2, t=t)   # Exponential decay
