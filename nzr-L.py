import matplotlib.pyplot as plt
from typing import TypeAlias, List

Integer = int
String = str

class NRZ_L:

    def __init__(self, message:String = '', signal:String = ''):
        self.messsage = message
        self.signal = signal

    def encode(self):
        encoded_signal : List[Integer] = []
        for bit in self.messsage:
            encoded_signal.append(int(bit))

        return encoded_signal
    

    def decode(self):
        decoded_msg : String = ''
        for bit in self.signal:
            decoded_msg += str(bit)

        return decoded_msg


    def plot(self):
        signal = self.encode()
        time : List[Integer] = [0]
        levels : List[Integer] = [0]
        i = 0 
        plot_signal = [(-1 if i==0 else 1) for i in signal]

        for level in plot_signal:
            time.extend([i for i in range(i,i+2)])
            levels.extend([level]*(2))
            i = i+1

        plt.step(time, levels, where='post')
        plt.title('NRZ-L Encoding')
        plt.xlabel('Time')
        plt.ylabel('Signal Level')
        plt.grid()
        plt.show()


if __name__ == "__main__":
    message = '11001101'
    signal = '00000000'
    nrz_l = NRZ_L(message, signal)
    encoded_signal = nrz_l.encode()
    print(f'Encoded Signal: {encoded_signal}')
    decoded_signal = nrz_l.decode()
    print(f'Decoded Signal: {decoded_signal}')
    nrz_l.plot()
        