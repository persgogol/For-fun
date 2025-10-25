import math
import time

def wave_pattern(cycles=5, amplitude=10, width=60, delay=0.05):
    """
    Generate a simple sine wave pattern in the console.

    Args:
    - cycles (int): Number of complete wave cycles to draw.
    - amplitude (int): Vertical amplitude of the wave.
    - width (int): Number of columns for each cycle.
    - delay (float): Delay between frames in seconds.
    """
    for i in range(cycles * width):
        # Calculate horizontal position using a sine function
        phase = 2 * math.pi * (i % width) / width
        offset = int(amplitude * (1 + math.sin(phase)))
        print(' ' * offset + '*')
        time.sleep(delay)

if __name__ == "__main__":
    wave_pattern()
