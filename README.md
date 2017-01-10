# Python_stack
genetic_drift_sim.py is a script to simulate the "genetic drift" in population genetics.
Lib requirements: numpy, matplotlib.
Run python genetic_drift_sim.py -h to see the usage of available arguments. If you want to have figure plotted, please make sure you have matplotlib module installed.
usage: genetic_drift_sim.py [-h] [-v] [-plt {f_vs_t,t_dist,np,all}]
                            [-o OUTPUT] [-p POP] [-s SIZE] [-f FREQ]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -plt {f_vs_t,t_dist,np,all}, --plot {f_vs_t,t_dist,np,all}
                        whether output plot and need to specify plot type
  -o OUTPUT, --output OUTPUT
                        OUTPUT FILE
  -p POP, --pop POP     specify how many populations you want in the
                        simulation, must be int
  -s SIZE, --size SIZE  specify the population size you want in the
                        simulation, must be int
  -f FREQ, --freq FREQ  specify the initial frequency you want in the
                        simulation, must be between 0 and 1
 
