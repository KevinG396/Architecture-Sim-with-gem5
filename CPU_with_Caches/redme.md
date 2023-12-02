# Project Structure
#### Caches.py is used to define L1ICache, L1DCache and L2Cache, other parts of the CPU (In Order Execution) are defined in cpu.py

# Usage
#### Run:
```
$GEM5/build/ARM/gem5.opt  --outdir="daxpy_arm" cpu.py --prog="daxpy" --l1d_size="128kB" --l1d_assoc="8" --clock_freq="0.8GHz" 
```
#### You can change l1d_size, l1d_assoc, clock_freq three parameters and record L1I/L1D/L2 Cache Miss and other metrics. Program can be changed, too.
