import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


class Sender:
    """ Class that represents the sender of the communication channel"""

    def __init__(self):
        self.Data = None

    def send_image(self):
        """ Sends the image data with the header """
        pass

    def send_text(self):
        """ Sends the text data with the header """
        pass

    def load_image(self, path: str):
        """ Loads the image from the path """
        pass

    def load_text(self, path: str):
        """ Loads the text from the path """
        pass
