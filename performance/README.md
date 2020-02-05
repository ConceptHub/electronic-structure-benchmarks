A collection of performance benchmarks for QE

To submit jobs, use:
```bash
python job_launch.py Si511Ge -i pw.in -p gpu -t 12 -s $SCRATCH -c 'pw.x -sirius' -k 1 --nodes 9 16 25 36 -T '0:20:00' -S '_QE_sirius_elpa' -R
 ```

To collect data, use:
```bash
find $SCRATCH/Si511Ge_QE_native_6T -name slurm-stdout.txt -exec sh -c "echo {}; python get_pwscf_time.py {}" \;
```
