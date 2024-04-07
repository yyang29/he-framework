import constraints
import explorer
import he_parameters

import argparse
import csv
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger('framework_dse')
logger.setLevel("INFO")


def parse_input_csv(input_file):
  with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    headers = reader.fieldnames

    data_dict = {}

    # Read the next row (data row) and populate the dictionary
    for row in reader:
      for header in headers:
        data_dict[header] = int(row[header])
      break  # Stop after the first data row

    return data_dict


def run_design_space_exploration(parsed_input,
                                 he_op,
                                 output_file,
                                 alu_override=512):
  logger.info(f"Running design space exploration for {he_op}.")

  he_params = he_parameters.HeParameters(parsed_input["N"], parsed_input["L"],
                                         parsed_input["log_P"],
                                         parsed_input["dnum"],
                                         parsed_input["log_q_i"],
                                         parsed_input["name"])

  exploration_constraints = constraints.Constraints(
      parsed_input["latency_us"], parsed_input["uram"], parsed_input["bram"],
      parsed_input["dsp"], parsed_input["bandwidth_gbps"],
      parsed_input["frequency_mhz"])

  he_params.display_parameters()
  exploration_constraints.display_constraints()

  dse = explorer.Explorer(he_params, he_op, exploration_constraints)
  dse.explore_design_space(output_file, alu_override)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description="Design space exploration tool of the HE ops framework.")
  parser.add_argument("--input",
                      "-i",
                      required=True,
                      help="Input of the framework.")

  # op is one of (ptctadd, ctctadd, ptctmult, ctctmult, rotate, keyswitch,
  # rescale)
  parser.add_argument("--operation",
                      "-op",
                      required=True,
                      help="HE operation to explore.")

  parser.add_argument("--output",
                      "-o",
                      required=True,
                      help="Path of the output csv file.")

  parser.add_argument("--alu-override", "-a", type=int, default=512)

  parser.add_argument("--bw-override", "-b", type=int)

  parser.add_argument("--name", "-n", type=str, default="NoName")

  args = parser.parse_args()

  parsed_input = parse_input_csv(args.input)
  parsed_input["name"] = args.name

  logger.info(f"Overriding ALU limit to {args.alu_override}.")

  if args.bw_override is not None:
    logger.info(f"Overriding BW limit to {args.bw_override}.")
    parsed_input["bandwidth_gbps"] = args.bw_override

  assert (args.operation
          in ["CtCtAdd", "CtCtMult", "Rotate", "KeySwitch", "Rescale"])
  run_design_space_exploration(parsed_input, args.operation, args.output,
                               args.alu_override)
