import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger('constraints')
logger.setLevel("DEBUG")


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
    logger.info("Exploration constraints are shown below.")
    logger.info(f"\tLatency (us): {self.latency}")
    logger.info(f"\tURAM (instances): {self.uram}")
    logger.info(f"\tBRAM (instances): {self.bram}")
    logger.info(f"\tDSP: {self.dsp}")
    logger.info(f"\tBandwidth (GB/s): {self.bandwidth_gbps}")
    logger.info(f"\tFrequency (MHz): {self.frequency_mhz}")
