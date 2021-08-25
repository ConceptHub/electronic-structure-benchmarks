A collection of performance benchmarks for QE

1. To submit jobs, run:
```bash
python job_launch.py Au-surf -i pw.in -p mc -t 3 -c 'pw.x' -k 2 -n 12 24 36 48 -T '0:20:00' -l 'qe_cscs_67' -R
python job_launch.py Au-surf -i pw.in -p gpu -t 12 -c 'pw.x -sirius_scf' -k 2 -n 1 2 3 4 -T '0:20:00' -l 'qe_sirius' -R
 ```

2. To collect data, run:
```bash
python collect.py $SCRATCH/Au-surf
```

3. To produce a plot, run:
```bash
python plot.py -x nodes:Nodes -y scf_time:SCF Au-surf.json "qe_cscs_67:QE-6.7 CPU" "qe_sirius:QE+SIRIUS GPU"
```

# Individual benchmarks

## Si511Ge
```bash
python job_launch.py Si511Ge -i pw.in -p mc -t 9 -c 'pw.x' -k 1 -n 16 36 64 100 -T '0:30:00' -l 'qe_cscs_67' -R
```

## Au-surf
```bash
python job_launch.py Au-surf -i pw.in -p gpu -t 12 -c 'pw.x -sirius_scf' -k 2 -n 1 2 3 4 -T '0:20:00' -l 'qe_sirius' -R
```
