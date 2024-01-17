import platform_constants

import math


class Area:

  def __init__(self, num_urams, num_brams, num_dsps):
    self.num_urams = num_urams
    self.num_brams = num_brams
    self.num_dsps = num_dsps

  def display_area(self):
    print(f"DSP (instances): {self.num_dsps}")
    print(f"URAM (instances): {self.num_urams}")
    print(f"BRAM (instances): {self.num_brams}")


class AreaEstimator:

  design_params = None

  def __init__(self, he_params, constraints):
    self.he_params = he_params
    self.constraints = constraints
    if self.he_params.log_q_i == 62:
      self.dsp_per_alu = platform_constants.NUM_DSPS_WIDE_COEFFICIENT
    elif self.he_params.log_q_i == 32:
      self.dsp_per_alu = platform_constants.NUM_DSPS_NARROW_COEFFICIENT
    else:
      raise ValueError

  def estimate_area(self, design_params):
    self.design_params = design_params
    self.scratch_depth_needed = design_params.scratchpad_depth

    num_dsps = self._estimate_dsp()
    num_urams = self._estimate_uram_for_scratch()
    num_brams = self._estimate_bram_for_spn()

    print(f"URAM for scratch: {num_urams}")
    print(f"BRAM for spn: {num_brams}")

    if self.scratch_depth_needed != 0:
      num_brams += self._estimate_bram_for_scratch()

    print(f"BRAM for spn + scratch: {num_brams}")

    return Area(num_urams, num_brams, num_dsps)

  def _estimate_dsp(self):
    return self.design_params.num_modular_alus * self.dsp_per_alu

  def _estimate_bram_for_spn(self):

    # always store one coefficient per entry.
    if self.he_params.log_q_i == 62:
      bram_depth = platform_constants.BRAM_DEPTH_WIDE_COEFFICIENT
    elif self.he_params.log_q_i == 32:
      bram_depth = platform_constants.BRAM_DEPTH_NARROW_COEFFICIENT
    else:
      raise ValueError

    total_depth = self.he_params.N // self.design_params.permute_throughput
    brams_per_temporal_buffer = int(math.ceil(total_depth / bram_depth))

    return brams_per_temporal_buffer * self.design_params.permute_throughput

  def _estimate_uram_for_scratch(self):

    urams_horizontal = math.ceil(
        self.design_params.scratchpad_bank_width_bytes /
        platform_constants.URAM_WIDTH_BYTES)

    urams_vertical = math.ceil(self.design_params.scratchpad_depth /
                               platform_constants.URAM_DEPTH)

    total_urams = urams_horizontal * urams_vertical * self.design_params.scratchpad_banks

    if total_urams > self.constraints.uram:
      allocated_depth = (self.constraints.uram // urams_horizontal //
                         self.design_params.scratchpad_banks *
                         platform_constants.URAM_DEPTH)
      self.scratch_depth_needed = self.scratch_depth_needed - allocated_depth
      return self.constraints.uram
    else:
      self.scratch_depth_needed = 0
      return total_urams

  def _estimate_bram_for_scratch(self):

    brams_horizontal = math.ceil(
        self.design_params.scratchpad_bank_width_bytes /
        platform_constants.BRAM_WIDTH_BYTES)

    brams_vertical = math.ceil(self.scratch_depth_needed /
                               platform_constants.BRAM_DEPTH_WIDE_COEFFICIENT)

    total_brams = brams_horizontal * brams_vertical * self.design_params.scratchpad_banks

    return total_brams
