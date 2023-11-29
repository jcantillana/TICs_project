import numpy as np
import sounddevice as sd
import matplotlib
#matplotlib.use("QtAgg")
import matplotlib.pyplot as plt


class Receiver:
    """ Class that represents the receiver of the communication channel"""

    def __init__(self, channel: float):
        self.buffer = None
        self.channel = channel
        self.samplerate = 44100

    def listen(self, duration: float):
        """ Listens to the channel for a message """
        # record audio
        data = sd.rec(frames=int(self.samplerate*duration),
                      samplerate=self.samplerate, channels=2)
        sd.wait()
        self.buffer = data
        return

    def decode(self, msg: np.ndarray, header: int):
        """ Decodes the message from the channel"""
        pass

    def play_recorded(self):
        sd.play(self.buffer, self.samplerate)
        sd.wait()
        return

    def plot_fft(self):
        """Plots the FFT of the recorded data."""
        if self.buffer is None:
            print("No data to plot. Please record data first.")
            return

        # Compute FFT
        fft_result = np.fft.fft(self.buffer[:, 0])  # Use the first channel for FFT
        L = len(fft_result)

        # Compute corresponding frequencies
        freq = np.fft.fftfreq(len(fft_result), 1/self.samplerate)

        max_idx = np.argmax(np.abs(fft_result))
        max_freq = freq[max_idx]

        # Plot FFT
        plt.figure(figsize=(10, 4))
        plt.semilogx(freq[0:L//2], np.abs(fft_result)[0:L//2])
        plt.title("FFT of Recorded Data")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")

        # Add text about the maximum frequency
        plt.text(max_freq, np.abs(fft_result[max_idx]),
                 'Max at {:.2f} Hz'.format(max_freq),
                 ha='center', va='bottom')

        plt.show()
