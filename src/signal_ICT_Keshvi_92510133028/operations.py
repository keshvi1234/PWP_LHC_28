import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, n, k):
    """
    Shift the signal by k units.
    Also plots original (time-variant reference) and shifted (time-invariant check).
    """
    shifted_n = n + k

    plt.stem(n, signal, linefmt='b-', markerfmt='bo', basefmt=" ", label="Original Signal")
    plt.stem(shifted_n, signal, linefmt='r-', markerfmt='ro', basefmt=" ", label=f"Shifted Signal (k={k})")

    plt.title(f"Time Shift: Original vs Shifted (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

    return shifted_n, signal


def time_scale(signal, n, k):
    """
    Scale the time axis of the signal by factor k.
    Example: k=2 compresses, k=0.5 expands.
    """
    scaled_n = n * k
    plt.stem(scaled_n, signal, basefmt="r-")
    plt.title(f"Time Scaled Signal (k={k})")
    plt.xlabel("n (scaled)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return scaled_n, signal

def signal_addition(signal1, signal2):
    """
    Perform addition of two signals (element-wise).
    """
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length to add.")
    result = signal1 + signal2
    plt.stem(range(len(result)), result, basefmt="r-")
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return result

def signal_multiplication(signal1, signal2):
    """
    Perform element-wise multiplication of two signals and plot the result.
    Uses a line plot so continuous/sinusoidal signals look correct.
    """
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length to multiply.")

    result = signal1 * signal2

    x = np.arange(len(result))  # sample index (since we don't receive a time vector here)
    plt.plot(x, result)
    plt.title("Signal Multiplication (element-wise)")
    plt.xlabel("Sample index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return result

