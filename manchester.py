import matplotlib.pyplot as plt
from typing import List, TypeAlias

Integer: TypeAlias = int
String: TypeAlias = str

class Manchester:
    
    def __init__(self, message: String = '', signal: String = '', time_period: Integer = 1):
        self.message: String = message
        self.signal: List[Integer] = list(int(bit) for bit in signal)   
        self.time_period = time_period
    
    def setMessage(self, msg: String):
        self.message = msg
    
    def setSignal(self, signal: String):
        self.signal = list(int(bit) for bit in signal)
    
    def encode(self) -> List[Integer]:
        encoded_signal: List[Integer] = []
        for bit in self.message:
            if bit == '0':
                encoded_signal.extend([1, 0])  # Representing logical 0 (high to low)
            else:
                encoded_signal.extend([0, 1])  # Representing logical 1 (low to high)
        
        return encoded_signal  # Corrected the indentation
    
    def decode(self) -> String:
        decoded_msg: String = ''
        for i in range(0, len(self.signal)-1, 2):
            if self.signal[i] == 1 and self.signal[i+1] == 0:
                decoded_msg += '0'  # High to low (logical 0)
            elif self.signal[i] == 0 and self.signal[i+1] == 1:
                decoded_msg += '1'  # Low to high (logical 1)
        
        return decoded_msg

    def plot(self):
        signal = self.encode()  # Get the encoded signal
        time: List[Integer] = [0]
        levels: List[Integer] = [1]  # Initial signal level
        i = 0
        
        # Create a list of signal levels based on the encoding
        plot_signal = []
        for bit in signal:
            plot_signal.append(-1 if bit == 1 else 1)

        for level in plot_signal:
            time.extend([i for i in range(i, i + self.time_period + 1)])
            levels.extend([level] * (self.time_period + 1))
            i += self.time_period  # Increment time index

        plt.step(time, levels, where='post')
        plt.title('Manchester Encoding')
        plt.xlabel('Time')
        plt.ylabel('Signal Level')
        plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
        plt.xticks(range(0, len(time),2))
        plt.grid()
        plt.show()


if __name__ == "__main__":
    manchester = Manchester(message='10111001', signal='0101010')
    encoded_signal = manchester.encode()
    print(f'Encoded Signal: {encoded_signal}')
    decoded_signal = manchester.decode()
    print(f'Decoded Signal: {decoded_signal}')
    manchester.plot()
