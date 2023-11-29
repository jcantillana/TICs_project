# This is a sample Python script.
import matplotlib as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Sender import Sender
from Receiver import Receiver

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Receiver = Receiver(100)
    Receiver.listen(5)
    Receiver.play_recorded()
    Receiver.plot_fft()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
