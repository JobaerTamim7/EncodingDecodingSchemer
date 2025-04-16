import matplotlib.pyplot as plt
from typing import List, TypeAlias
from numpy import array
Integer : TypeAlias = int
String : TypeAlias = str

class NRZ_I:

    def __init__(self, message : String):
        self.message : String = message

    def encode(self) -> List[Integer]:
        
        encoded_signal : List[String] = []
        signal_level = 1

        for bit in self.message:
            if bit == '1':
                signal_level = 1 - signal_level 
            encoded_signal.append(signal_level)

        return encoded_signal 
    
    def decode(self) -> String:
         pass


    def plot(self):
            signal = self.encode()
            time : List[Integer] = []
            levels : List[Integer] = []
            i = 0 

            for level in signal:
                time.extend([i for i in range(i,i+3)])
                levels.extend([level]*3)

                i = i+2

            print(time)
            print(levels)
            plt.figure(figsize=(15,7))
            plt.ylabel("Signal")
            plt.xlabel("Time")
            plt.plot(time,levels)
            plt.show()

if __name__ == '__main__':
    input_bits = '101101010'
    nrzi = NRZ_I(input_bits)
    print("Encoded Signal:", nrzi.encode())
    nrzi.plot()



