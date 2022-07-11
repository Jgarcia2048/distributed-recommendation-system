import os
from tqdm import tqdm #NEW
import psutil
from time import sleep

def main():

    mxrm = 0
    mxcpu = 0
    with tqdm(total=100, desc='cpu%', position=1) as cpu, tqdm(total=100, desc='ram%', position=0) as ram:
        while True:
            ram.n = psutil.virtual_memory().percent
            cpu.n = psutil.cpu_percent()

            # if psutil.virtual_memory().percent > mxrm:
            #     mxrm = psutil.virtual_memory().percent
            # if psutil.cpu_percent() > mxcpu:
            #     mxcpu = psutil.cpu_percent()

            ram.refresh()
            cpu.refresh()
            sleep(0.25)

if __name__ == "__main__":
    main()