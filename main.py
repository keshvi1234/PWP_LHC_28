import numpy as np
from src.signal_ICT_Keshvi_92510133028 import unit_step, unit_impulse, ramp_signal
from src.signal_ICT_Keshvi_92510133028 import sine_wave, cosine_wave
from src.signal_ICT_Keshvi_92510133028 import time_shift, signal_addition, signal_multiplication

# --------------------------
# Main Script Demonstration
# --------------------------
if __name__ == "__main__":
    # Task 1: Generate and plot a unit step signal and a unit impulse signal of length 20
    n = np.arange(0, 20, 1)
    step = unit_step(n)
    impulse = unit_impulse(n)

    # Task 2: Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec
    t = np.linspace(0, 1, 100)
    sine = sine_wave(A=2, f=5, phi=0, t=t)

    # Task 3: Perform time shifting on the sine wave by +5 units and plot both original and shifted signals
    print("Performing Time Shift...")
    time_shift(sine, np.arange(len(sine)), k=5)

    # Task 4: Perform addition of the unit step and ramp signal and plot the result
    ramp = ramp_signal(n)
    print("step and ramp signal ")
    signal_addition(step, ramp)

    # Task 5: Multiply a sine and cosine wave of same frequency and plot the result
    cosine = cosine_wave(A=2, f=5, phi=0, t=t)
    print("Performing Signal Multiplication...")
    signal_multiplication(sine, cosine)
