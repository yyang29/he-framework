class Constraints:
  # Class members
  latency_us = None
  uram = None
  bram = None
  dsp = None
  bandwidth_gbps = None
  frequency_mhz = None

  def __init__(self, latency_us, uram, bram, dsp, bandwidth_gbps,
               frequency_mhz):
    self.latency = latency_us
    self.uram = uram
    self.bram = bram
    self.dsp = dsp
    self.bandwidth_gbps = bandwidth_gbps
    self.frequency_mhz = frequency_mhz

  def display_constraints(self):
    print("Exploration constraints are shown below.")
    print(f"\tLatency (us): {self.latency}")
    print(f"\tURAM (instances): {self.uram}")
    print(f"\tBRAM (instances): {self.bram}")
    print(f"\tDSP: {self.dsp}")
    print(f"\tBandwidth (GB/s): {self.bandwidth_gbps}")
    print(f"\tFrequency (MHz): {self.frequency_mhz}")
