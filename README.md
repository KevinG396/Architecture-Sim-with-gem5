# gem5_basic
Basic simulations of in-order/out-of-order execution CPUs, with/without Branch Prediction, Caches(L1, L2).

# Environment
In Linux System, set GEM5 env_path:
If using tcsh, open .cshrc in your home directory and add:
```
setenv /your_path_to_gem5/gem5/gem5_dev/
```
Then:
```
source ~/.cshrc
```
Else, if using bash, open .bash profile in your home directory and add:
```
export GEM5=/project/linuxlab/gem5/gem5 dev
```
Then:
```
source ~/.bash profile
```

# Test Programs
Before started, you should compile `daxpy.c` to `daxpy_x86` and `daxpy_arm` with gcc tool in `/test_prog/daxpy` folder.

Test programs in `Queens` used existing compiled programs, please let me know if there's any copyright issues.

# Projects Details
Each project has its own README.md in the folder.

### Mark: `OoO_cpu.py` file in Out_of_Order_CPU sub-project used existing python file from gem5 project.
