from m5 import fatal
import m5.objects
from textwrap import TextWrapper

#add options for number of ROB entries, IQ entries, and number of physical
#integer registers
def addOpts(parser):
    parser.add_option("--num_rob_entries", type="int", default="192")
    parser.add_option("--num_iq_entries", type="int", default="64")
    parser.add_option("--num_phys_int_regs", type="int", default="256")

#set parameters taken in from options on command line
def set_config(cpu_list, options):
    for cpu in cpu_list:
        # set parameters for each thing
        cpu.numROBEntries = options.num_rob_entries
        cpu.numIQEntries = options.num_iq_entries
        cpu.numPhysIntRegs = options.num_phys_int_regs

