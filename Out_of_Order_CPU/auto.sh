output_file="results.txt"
echo "num_rob_entries num_phys_int_regs num_iq_entries nss NCRB NIRL IIR ICRR ROB CMR" > $output_file

gem5_command="$GEM5/build/ARM/gem5.opt OoO_cpu.py -c daxpy_arm_test --cpu-type=DerivO3CPU --caches --l2cache"

num_rob_entries_values=(4 16 64 256)
num_phys_int_regs_values=(64 256 1024)
num_iq_entries_values=(4 16 64 256)


for num_rob in "${num_rob_entries_values[@]}"; do
  for num_phys_int in "${num_phys_int_regs_values[@]}"; do
    for num_iq in "${num_iq_entries_values[@]}"; do
      timestamp=$(date +%Y%m%d%H%M%S)
      result_folder="m5out"


      $gem5_command --num_phys_int_regs=$num_phys_int --num_rob_entries=$num_rob --num_iq_entries=$num_iq

      NCRB=$(grep "system.cpu.rename.BlockCycles" $result_folder/stats.txt | awk '{print $2}')
      nss=$(grep "sim_seconds" $result_folder/stats.txt | awk '{print $2}')
      NIRL=$(grep "system.cpu.rename.int_rename_lookups" $result_folder/stats.txt | awk '{print $2}')
      IIR=$(grep "system.cpu.iq.rate" $result_folder/stats.txt | awk '{print $2}')
      ICRR=$(grep "system.cpu.rename.IdleCycles" $result_folder/stats.txt | awk '{print $2}')
      ROB=$(grep "system.cpu.rename.ROBFullEvents" $result_folder/stats.txt | awk '{print $2}')
      CMR=$(grep "system.cpu.dcache.overall_miss_rate::total" $result_folder/stats.txt | awk '{print $2}')
      echo "$num_rob $num_phys_int $num_iq $nss $NCRB $NIRL $IIR $ICRR $ROB $CMR" >> $output_file
    done
  done
done

echo "done! all in $results_file"
