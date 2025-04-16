import matplotlib.pyplot as plt
from typing import List, TypeAlias
Integer : TypeAlias = int
String : TypeAlias = str

class NRZ_I:

    def __init__(self, message : String = '', signal : String = '', time_period : Integer = 1):
        self.message : String = message
        self.signal : List[Integer] = list(int(bit) for bit in signal)   
        self.time_period = time_period


    def setMessage(self, msg: String):
        self.message = msg

    def setSignal(self, signal : String):
        self.signal = list(int(bit) for bit in signal)


    def encode(self) -> List[Integer]:
        encoded_signal : List[String] = []
        signal_level = 1

        for bit in self.message:
            if bit == '1':
                signal_level = 1 - signal_level
            encoded_signal.append(signal_level)

        return encoded_signal 
    
    
    def decode(self) -> String:
        decoded_msg : String = ""
        if self.signal == 0:
           decoded_msg = decoded_msg + "0"
        else:
           decoded_msg = decoded_msg + "1"
           
        for i in range(0, len(self.signal)-1):
            # print(f'iteration no {i} : {self.signal[i]} {self.signal[i+1]}')

            if  self.signal[i] == self.signal[i+1]:
               decoded_msg = decoded_msg + "0"
            else:
               decoded_msg = decoded_msg + "1"
        return decoded_msg
    
    
    def plot(self):
            signal = self.encode()
            time : List[Integer] = [0]
            levels : List[Integer] = [1]
            i = 0 
            plot_signal = [(-1 if i==0 else 1) for i in signal]

            for level in plot_signal:
                time.extend([i for i in range(i,i+self.time_period+1)])
                levels.extend([level]*(self.time_period+1))
                i = i+self.time_period


            plt.figure(figsize=(15,7))
            plt.ylabel("Signal")
            plt.yticks([-1,0,1])
            plt.xlabel("Time")
            plt.xticks([i for i in range(0, len(self.message)*self.time_period+1)])
            plt.plot(time,levels)
            plt.grid(True)
            plt.show()

if __name__ == '__main__':
    input_bits = '10111001'
    nrzi = NRZ_I(message=input_bits,time_period=1)
    nrzi.setSignal(nrzi.encode())
    print(nrzi.encode())
    print(nrzi.decode())
    nrzi.plot()
    





