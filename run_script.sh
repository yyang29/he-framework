echo "Name,Op,Latency,DSPs,URAMs,BRAMs,NumAlu,PermTput,ScratchSize,BW" > results.csv

for set in "Set-1" "Set-2" "Set-3"; do
  for op in "CtCtAdd" "CtCtMult" "Rescale" "Rotate"; do
    for alu in 64 128 256 512; do
      for bw in 128 256 460; do
        echo "python design_space_exploration.py --input ${set}.csv --operation ${op} --output ./${set}_output.csv -a $alu -b $bw -n Set-1 2>&1 | tee /tmp/log.log"
        python design_space_exploration.py --input ${set}.csv --operation ${op} --output ./${set}_output.csv -a $alu -b $bw -n ${set} > /tmp/log.log
      done
    done
  done
done

# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 16 -b 460 -n Set-1 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 32 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 64 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 128 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 256 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 512 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 16 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 32 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 64 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 128 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 256 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 512 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 16 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 32 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 64 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 128 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 256 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 512 -b 460  -n Set-1 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 16 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 32 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 64 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 128 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 256 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 512 -b 460 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 256 -b 256 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtMult --output ./exp_1_output.csv -a 256 -b 128 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 256 -b 256 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rotate --output ./exp_1_output.csv -a 256 -b 128 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 256 -b 256 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation Rescale --output ./exp_1_output.csv -a 256 -b 128 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 256 -b 256 -n Set-1  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_1.csv --operation CtCtAdd --output ./exp_1_output.csv -a 256 -b 128 -n Set-1  2>&1 | tee /tmp/log.log

# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 16 -b 460 -n Set-2 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 32 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 64 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 128 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 256 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 512 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 16 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 32 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 64 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 128 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 256 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 512 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 16 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 32 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 64 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 128 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 256 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 512 -b 460  -n Set-2 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 16 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 32 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 64 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 128 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 256 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 512 -b 460 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 256 -b 256 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtMult --output ./exp_2_output.csv -a 256 -b 128 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 256 -b 256 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rotate --output ./exp_2_output.csv -a 256 -b 128 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 256 -b 256 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation Rescale --output ./exp_2_output.csv -a 256 -b 128 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 256 -b 256 -n Set-2  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_2.csv --operation CtCtAdd --output ./exp_2_output.csv -a 256 -b 128 -n Set-2  2>&1 | tee /tmp/log.log

# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 16 -b 460 -n Set-3 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 32 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 64 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 128 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 256 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 512 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 16 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 32 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 64 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 128 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 256 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 512 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 16 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 32 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 64 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 128 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 256 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 512 -b 460  -n Set-3 2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 16 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 32 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 64 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 128 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 256 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 512 -b 460 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 256 -b 256 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtMult --output ./exp_3_output.csv -a 256 -b 128 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 256 -b 256 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rotate --output ./exp_3_output.csv -a 256 -b 128 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 256 -b 256 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation Rescale --output ./exp_3_output.csv -a 256 -b 128 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 256 -b 256 -n Set-3  2>&1 | tee /tmp/log.log
# python design_space_exploration.py --input exp_3.csv --operation CtCtAdd --output ./exp_3_output.csv -a 256 -b 128 -n Set-3  2>&1 | tee /tmp/log.log