import platform_constants
import utils

import logging
import math
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger('latency_estimator')
logger.setLevel("DEBUG")


class LatencyEstimator:
  design_params = None

  def __init__(self, he_params, op, constraints, logger=None):
    self.he_params = he_params
    self.op = op
    self.constraints = constraints
    self.logger = logger
    self.derating_factor = 1.08

    # scratchpad data reuse policy:
    # first, reuse twiddle factors
    # then, reuse 1/2 ciphertext across sub-routines
    # then, reuse KSK plaintext (column by column)
    # then, alpha limbs for basis conversion

  def estimate_latency(self, design_params):
    self.design_params = design_params

    if self.op == "CtCtAdd" or self.op == "CtCtSub":
      latency_us = self._estimate_limb_elementwise(
          platform_constants.POLYNOMIALS_PER_CIPHERTEXT * self.he_params.L)
      logger.info(f"{self.op} takes {latency_us} us.")
      return latency_us

    elif self.op == "CtCtMult":
      pass

    elif self.op == "Rotate":
      pass

    elif self.op == "KeySwitch":
      # Scratchpad (S) strategy
      #  Reuse: base conversion (L limbs)
      #  Reuse: producer - consumer between sub-routines
      #  Reuse: twiddle factors in NTT and INTT respectively
      # Processing flow
      #  Process the 1st polynomial first, then go to the 2nd polynomial
      #  if S < sizeof(2L limbs)
      #    "2L due to the fact that we need to read L limbs and write L limbs per polynomial"
      #    store x limbs (x = S / sizeof(limb) / 2)
      #  elif sizeof(2L limbs) < S < sizeof(2L limbs) + sizeof(tw)
      #    store L limbs + y set of tw
      #  else
      #    store L limbs and twiddle factors
      pass
      # alpha = self.he_params.alpha
      # beta = self.he_params.beta
      # k = self.he_params.k
      # decomp_output_fused = False
      # modup_ntt_output_fused = False
      # inner_prod_output_fused = False
      # moddown_ntt_output_fused = False

      # decomp_output_bytes = utils.get_limb_size_bytes(
      #     self.he_params) * self.he_params.L
      # if self.design_params.scratchpad_size_bytes > decomp_output_bytes * 2:
      #   decomp_output_fused = True

      # latency_decomp = self._estimate_decomp(False, decomp_output_fused)
      # latency_modup_intt = self._estimate_ntt(self.he_params.L, 0.0,
      #                                         decomp_output_fused, False)
      # latency_modup_base_conv = self._estimate_base_conv(
      #     self.he_params.L, beta * (alpha * beta + k - 1),
      #     beta * (alpha * beta + k - 1 - alpha))

      # modup_ntt_output_bytes = (utils.get_limb_size_bytes(self.he_params) *
      #                           beta * (alpha * beta + k - 1))
      # if self.design_params.scratchpad_size_bytes > modup_ntt_output_bytes:
      #   modup_ntt_output_fused = True
      # latency_modup_ntt = self._estimate_ntt(
      #     beta * (alpha * beta + k - 1 - alpha), 0.0, False,
      #     modup_ntt_output_fused)

      # inner_prod_output_bytes = (utils.get_limb_size_bytes(self.he_params) * 2 *
      #                            (alpha * beta + k - 1))
      # if self.design_params.scratchpad_size_bytes > inner_prod_output_bytes:
      #   inner_prod_output_fused = True
      # latency_inner_prod = self._estimate_inner_prod(modup_ntt_output_fused,
      #                                                inner_prod_output_fused)

      # latency_moddown_intt = self._estimate_ntt(2 * (alpha * beta + k - 1), 0.0,
      #                                           inner_prod_output_fused, False)
      # latency_moddown_base_conv = self._estimate_base_conv(
      #     2 * (alpha * beta + k - 1), 2 * self.he_params.L,
      #     2 * self.he_params.L)

      # moddown_ntt_output_bytes = (utils.get_limb_size_bytes(self.he_params) *
      #                             2 * self.he_params.L)
      # if self.design_params.scratchpad_size_bytes > moddown_ntt_output_bytes:
      #   moddown_ntt_output_fused = True
      # latency_moddown_ntt = self._estimate_ntt(2 * self.he_params.L, 0.0, False,
      #                                          moddown_ntt_output_fused)

      # latency_ct_add = self._estimate_limb_elementwise(
      #     2 * self.he_params.L, moddown_ntt_output_fused, False)

      # print(f"decomp_output_fused: {decomp_output_fused}")
      # print(f"modup_ntt_output_fused: {modup_ntt_output_fused}")
      # print(f"inner_prod_output_fused: {inner_prod_output_fused}")
      # print(f"moddown_ntt_output_fused: {moddown_ntt_output_fused}")

      # return (latency_decomp + latency_modup_intt + latency_modup_base_conv +
      #         latency_modup_ntt + latency_inner_prod + latency_moddown_intt +
      #         latency_moddown_base_conv + latency_moddown_ntt + latency_ct_add)

    elif self.op == "Rescale":
      # Scratchpad (S) strategy
      #  Reuse: base conversion (L limbs)
      #  Reuse: producer - consumer between sub-routines
      #  Reuse: twiddle factors in NTT and INTT respectively
      # Processing flow
      #  Process the 1st polynomial first, then go to the 2nd polynomial
      #  if S < sizeof(2L limbs)
      #    "2L due to the fact that we need to read L limbs and write L limbs per polynomial"
      #    store x limbs (x = S / sizeof(limb) / 2)
      #  elif sizeof(2L limbs) < S < sizeof(2L limbs) + sizeof(tw)
      #    store L limbs + y set of tw
      #  else
      #    store L limbs and twiddle factors
      num_limbs = platform_constants.POLYNOMIALS_PER_CIPHERTEXT * self.he_params.L
      tf_reuse_ratio = 0.0
      if (self.design_params.scratchpad_size_bytes
          > utils.get_plaintext_size_bytes(self.he_params)):
        tf_reuse_ratio = 0.5
      latency_intt = self._estimate_ntt(num_limbs, self.he_params.L,
                                        tf_reuse_ratio)
      latency_base_conv = self._estimate_base_conv(num_limbs, num_limbs,
                                                   num_limbs - 1)
      latency_ntt = self._estimate_ntt(num_limbs - 1, self.he_params.L - 1,
                                       tf_reuse_ratio)

      latency_us = latency_intt + latency_base_conv + latency_ntt
      logger.info(f"{self.op} takes {latency_us} us.")

      return latency_us

    else:
      raise ValueError

  def _estimate_limb_elementwise(self,
                                 num_limbs,
                                 input_fused=False,
                                 output_fused=False):
    memory_read_time_us = 0 if input_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs / self.constraints.bandwidth_gbps / 1e3
    memory_write_time_us = 0 if output_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs / self.constraints.bandwidth_gbps / 1e3
    compute_time_us = (
        num_limbs * (self.he_params.N / self.design_params.num_modular_alus) *
        utils.get_cycle_us(self.constraints.frequency_mhz))
    logger.debug(f"_estimate_limb_elementwise: "
                 f"compute_time_us: {compute_time_us}, "
                 f"memory_read_time_us: {memory_read_time_us}, "
                 f"memory_write_time_us: {memory_write_time_us}")

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_ntt(self,
                    num_limbs,
                    tf_reuse_ratio=0.0,
                    input_fused=False,
                    output_fused=False):
    tf_read_bytes = utils.get_twiddle_factor_size_bytes(
        self.he_params, num_limbs) * (1 - tf_reuse_ratio)
    limb_read_bytes = 0 if input_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    total_read_bytes = tf_read_bytes + limb_read_bytes
    memory_read_time_us = total_read_bytes / self.constraints.bandwidth_gbps / 1e3

    total_write_bytes = 0 if output_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    memory_write_time_us = total_write_bytes / self.constraints.bandwidth_gbps / 1e3

    # Factor of "1.5" in the alu_cycles to indicate the mult and add/sub require
    # separate issue slots.
    alu_cycles = (1.5 * num_limbs * math.log2(self.he_params.N) *
                  (self.he_params.N / self.design_params.num_modular_alus))
    permute_cycles = (
        num_limbs * math.log2(self.he_params.N) *
        (self.he_params.N / self.design_params.permute_throughput))
    compute_time_us = (max(alu_cycles, permute_cycles) *
                       utils.get_cycle_us(self.constraints.frequency_mhz))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_base_conv(self, num_input_limbs, num_output_limbs,
                          num_compute_limbs):
    memory_read_time_us = (utils.get_limb_size_bytes(self.he_params) *
                           num_input_limbs / self.constraints.bandwidth_gbps /
                           1e3)
    memory_write_time_us = (utils.get_limb_size_bytes(self.he_params) *
                            num_output_limbs / self.constraints.bandwidth_gbps /
                            1e3)
    compute_time_us = (
        2 * num_compute_limbs *
        (self.he_params.N / self.design_params.num_modular_alus) *
        utils.get_cycle_us(self.constraints.frequency_mhz))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_decomp(self, input_fused=False, output_fused=False):
    # only one polynomial goes through decomp.
    limb_read_bytes = 0 if input_fused else utils.get_limb_size_bytes(
        self.he_params) * self.he_params.L
    memory_read_time_us = limb_read_bytes / self.constraints.bandwidth_gbps / 1e3

    # only one polynomial goes through decomp.
    limb_write_bytes = 0 if output_fused else utils.get_limb_size_bytes(
        self.he_params) * self.he_params.L
    memory_write_time_us = limb_write_bytes / self.constraints.bandwidth_gbps / 1e3

    compute_time_us = (
        2 * self.he_params.L *
        (self.he_params.N / self.design_params.num_modular_alus) *
        utils.get_cycle_us(self.constraints.frequency_mhz))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_inner_prod(self, input_fused=False, output_fused=False):
    ksk_read_bytes = utils.get_key_switch_keys_size_bytes(self.he_params)

    alpha = self.he_params.alpha
    beta = self.he_params.beta
    k = self.he_params.k
    num_limbs = alpha * beta + k - 1

    limb_read_bytes = 0 if input_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    total_read_bytes = ksk_read_bytes + limb_read_bytes
    memory_read_time_us = total_read_bytes / self.constraints.bandwidth_gbps / 1e3

    total_write_bytes = 0 if output_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    memory_write_time_us = total_write_bytes / self.constraints.bandwidth_gbps / 1e3

    compute_time_us = (2 * num_limbs * beta *
                       (self.he_params.N / self.design_params.num_modular_alus))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_automorph(self,
                          num_limbs,
                          input_fused=False,
                          output_fused=False):
    pass

  def _estimate_ntt_new(self, num_limbs, num_limbs_read, num_limbs_write,
                        num_tf_sets_read):
    tf_read_bytes = utils.get_twiddle_factor_size_bytes(
        self.he_params, num_limbs) * (1 - tf_reuse_ratio)
    limb_read_bytes = 0 if input_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    total_read_bytes = tf_read_bytes + limb_read_bytes
    memory_read_time_us = total_read_bytes / self.constraints.bandwidth_gbps / 1e3

    total_write_bytes = 0 if output_fused else utils.get_limb_size_bytes(
        self.he_params) * num_limbs
    memory_write_time_us = total_write_bytes / self.constraints.bandwidth_gbps / 1e3

    # Factor of "1.5" in the alu_cycles to indicate the mult and add/sub require
    # separate issue slots.
    alu_cycles = (1.5 * num_limbs * math.log2(self.he_params.N) *
                  (self.he_params.N / self.design_params.num_modular_alus))
    permute_cycles = (
        num_limbs * math.log2(self.he_params.N) *
        (self.he_params.N / self.design_params.permute_throughput))
    compute_time_us = (max(alu_cycles, permute_cycles) *
                       utils.get_cycle_us(self.constraints.frequency_mhz))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor

  def _estimate_base_conv_new(self, num_input_limbs, num_output_limbs,
                              num_limbs_read, num_limbs_write,
                              num_compute_limbs):
    memory_read_time_us = (utils.get_limb_size_bytes(self.he_params) *
                           num_input_limbs / self.constraints.bandwidth_gbps /
                           1e3)
    memory_write_time_us = (utils.get_limb_size_bytes(self.he_params) *
                            num_output_limbs / self.constraints.bandwidth_gbps /
                            1e3)
    compute_time_us = (
        2 * num_compute_limbs *
        (self.he_params.N / self.design_params.num_modular_alus) *
        utils.get_cycle_us(self.constraints.frequency_mhz))

    latency_us = max(compute_time_us,
                     memory_read_time_us + memory_write_time_us)

    return latency_us * self.derating_factor
