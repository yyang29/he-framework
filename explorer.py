import area_estimator
import design_parameters
import latency_estimator
import platform_constants
import utils

import csv


def generate_range(min_value, max_value):
  current_value = min_value
  while current_value <= max_value:
    yield current_value
    current_value *= 2


class Explorer:

  def __init__(self, he_params, he_op, constraints):
    self.he_params = he_params
    self.he_op = he_op
    self.constraints = constraints
    self.best_design = {
        "design_params": None,
        "latency": None,
        "area": None,
    }

  def explore_design_space(self, output_file):
    file = open(output_file, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(
        ["latency", "dsp", "uram", "bram", "NumAlu", "PermTput", "ScratchSize"])

    alu_range_generator = generate_range(1, 512)
    NUM_ALUS_RANGE = list(alu_range_generator)
    # print(NUM_ALUS_RANGE)

    throughput_permute_range_generator = generate_range(2, 512)
    THROUGHPUT_PERMUTE_RANGE = list(throughput_permute_range_generator)
    # print(THROUGHPUT_PERMUTE_RANGE)

    a_estimator = area_estimator.AreaEstimator(self.he_params, self.constraints)
    l_estimator = latency_estimator.LatencyEstimator(self.he_params, self.he_op,
                                                     self.constraints)

    for num_alus in NUM_ALUS_RANGE:
      for permute_throughput in THROUGHPUT_PERMUTE_RANGE:
        max_coefficients_per_cycle = max(num_alus, permute_throughput)
        scratchpad_bank_width_bytes = (
            max_coefficients_per_cycle //
            utils.get_coefficients_per_uram_row(self.he_params) *
            platform_constants.URAM_WIDTH_BYTES)
        # Does not make sense if less than 128B
        scratchpad_bank_width_bytes = max(scratchpad_bank_width_bytes, 128)
        assert (max_coefficients_per_cycle %
                utils.get_coefficients_per_uram_row(self.he_params) == 0)
        scratchpad_num_banks = self._get_minimal_number_banks()
        scratchpad_start_bytes = (
            scratchpad_bank_width_bytes * scratchpad_num_banks *
            platform_constants.BRAM_DEPTH_WIDE_COEFFICIENT)
        scratchpad_step_bytes = (scratchpad_bank_width_bytes *
                                 scratchpad_num_banks *
                                 platform_constants.BRAM_DEPTH_WIDE_COEFFICIENT)
        scratchpad_step_bytes = max(scratchpad_step_bytes,
                                    utils.get_limb_size_bytes(self.he_params))
        scratchpad_size_range_generator = range(
            scratchpad_start_bytes, platform_constants.MAX_SRAM_SIZE_BYTES,
            scratchpad_step_bytes)

        SCRATCHPAD_SIZE_RANGE = list(scratchpad_size_range_generator)

        for scratchpad_size_bytes in SCRATCHPAD_SIZE_RANGE:
          design_params = design_parameters.DesignParameters(
              num_alus, permute_throughput, scratchpad_size_bytes,
              scratchpad_bank_width_bytes, scratchpad_num_banks)
          print(f"num_alus: {num_alus}, "
                f"permute_throughput: {permute_throughput}, "
                f"scratchpad bank width bytes: {scratchpad_bank_width_bytes}, "
                f"Scratchpad size bytes: {scratchpad_size_bytes}")
          # estimate area
          area = a_estimator.estimate_area(design_params)
          if not self._meet_area_constraints(area):
            continue

          area.display_area()

          # estimate latency
          latency = l_estimator.estimate_latency(design_params)
          if not self._meet_latency_constraints(latency):
            continue

          print(f"latency: {latency}\n")

          writer.writerow([
              latency, area.num_dsps, area.num_urams, area.num_brams,
              design_params.num_modular_alus, design_params.permute_throughput,
              design_params.scratchpad_size_bytes
          ])

          if self.best_design["latency"] is None:
            self.best_design["design_params"] = design_params
            self.best_design["latency"] = latency
            self.best_design["area"] = area
          elif latency < self.best_design["latency"]:
            self.best_design["design_params"] = design_params
            self.best_design["latency"] = latency
            self.best_design["area"] = area

    print(self.best_design["latency"])
    self.best_design["area"].display_area()
    self.best_design["design_params"].display_parameters()

  def _get_minimal_number_banks(self):
    # keep number of banks constant for now
    return 4

  def _meet_area_constraints(self, area):
    if area.num_dsps > self.constraints.dsp:
      return False
    if area.num_brams > self.constraints.bram:
      return False
    if area.num_urams > self.constraints.uram:
      return False

    return True

  def _meet_latency_constraints(self, latency):
    if self.constraints.latency_us is None:
      return True

    if latency > self.constraints.latency_us:
      return False

    return True
