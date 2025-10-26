import random
import time

def matrix_rain(iterations=100, width=80, height=20, speed=0.05):
    """
    Simulate a simple matrix rain effect in the console.

    Args:
        iterations (int): Number of frames to display.
        width (int): Width of the output.
        height (int): Height before resetting a column.
        speed (float): Delay between frames in seconds.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789@$#*'
    columns = [0] * width
    for _ in range(iterations):
        line = ''
        for i in range(width):
            if columns[i] <= 0:
                if random.random() > 0.98:
                    columns[i] = random.randint(1, height)
            if columns[i] > 0:
                line += random.choice(chars)
                columns[i] -= 1
            else:
                line += ' '
        print(line)
        time.sleep(speed)

if __name__ == "__main__":
    matrix_rain()
