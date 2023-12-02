# Structure
This project is about simulation of an out_of_order execution CPU, the logic of the CPU is defined in `OoO_cpu.py` (this file uses an existing file in GEM5 project).

Options are set in `opts.py`.

You can execute the command line instruction, or you can edit auto.sh which is a script allows automatic execution and records the result in `results.txt`

The pdf is a report after analyzing the result of 48 times simulation.

# Usage
1. You can execute in command line tools:
```
$GEM5/build/ARM/gem5.opt OoO_cpu.py -c daxpy_arm_test --cpu-type="DerivO3CPU" --caches --l2cache
--num-phys-int-regs=64 --num-rob-entries=16 --num-iq-entries=64
```

2. Or you can just execute the script:
```
./auto.sh
```
