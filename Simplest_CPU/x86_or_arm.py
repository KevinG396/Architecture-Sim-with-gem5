import m5
from m5.objects import *
import os
import optparse

gem5_path = os.environ["GEM5"]   # GEM5 env_path

parser = optparse.OptionParser()
parser.add_option("--prog", type="str", default=None)
(options, args) = parser.parse_args()
program = options.prog

# Instantiate system SimObject
system = System()

# Create a clock domain
system.clk_domain = SrcClockDomain()

# Set different clk for ISAs
isa = m5.defines.buildEnv['TARGET_ISA']
if isa=="x86":
    system.clk_domain.clock = '1GHz'
elif isa == "arm":
    system.clk_domain.clock = '1.2GHz'

# Specify a voltage domain for the clock domain
system.clk_domain.voltage_domain = VoltageDomain()

# Use timing mode for memory simulation
# Set up a 512MB Memory
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]


# Create CPU
system.cpu = TimingSimpleCPU()

# Create System-wide MemBus
system.membus = SystemXBar()

# Connect cache ports on CPU to MemBus
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

# Create an I/O controller on CPU
system.cpu.createInterruptController()
if isa == 'x86':
    system.cpu.interrupts[0].pio = system.membus.master
    system.cpu.interrupts[0].int_master = system.membus.slave  # get interrupt signal from membus
    system.cpu.interrupts[0].int_slave = system.membus.master  # send interrupt signal to membus

# Connect a special port in the system to the membus
system.system_port = system.membus.slave

# Create a memcontroller and connect it to membus
# Manage entire mem range
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master


# Create a process (Another SimObject)
process = Process()
apps_path = "/test_progs/"
if program == "daxpy" and isa == "x86":
    process.cmd = [apps_path + '/daxpy/daxpy_x86']
elif program == "daxpy" and isa == "arm":
    process.cmd = [apps_path + '/daxpy/daxpy_arm']
elif program == "queens" and isa == "x86":
    process.cmd = [apps_path + '/queens/queens_x86']
    process.cmd += ["10 -c"]
elif program == "queens" and isa == "arm":
    process.cmd = [apps_path + '/queens/queens_arm']
    process.cmd += ["10 -c"]

system.cpu.workload = process
system.cpu.createThreads()


# Instantiate the system, begin execution
# Create Root object
root = Root(full_system = False, system = system)
m5.instantiate()
print ("Beginning simulation!")
exit_event = m5.simulate()
print ('Exiting @ tick %i because %s' %(m5.curTick(), exit_event.getCause()))
