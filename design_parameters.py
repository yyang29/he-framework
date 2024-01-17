import math


class DesignParameters:

  def __init__(self, num_modular_alus, permute_throughput,
               scratchpad_size_bytes, scratchpad_bank_width_bytes,
               scratchpad_banks):
    self.num_modular_alus = num_modular_alus
    self.permute_throughput = permute_throughput
    self.scratchpad_size_bytes = scratchpad_size_bytes
    self.scratchpad_bank_width_bytes = scratchpad_bank_width_bytes
    self.scratchpad_banks = scratchpad_banks
    self.scratchpad_depth = int(
        math.ceil(self.scratchpad_size_bytes / self.scratchpad_banks /
                  self.scratchpad_bank_width_bytes))
    self.scratchpad_bank_size_bytes = (self.scratchpad_size_bytes //
                                       self.scratchpad_banks)

  def display_parameters(self):
    print(f"NumAlu: {self.num_modular_alus}")
    print(f"PermTput: {self.permute_throughput}")
    print(f"ScratchSize: {self.scratchpad_size_bytes}")
