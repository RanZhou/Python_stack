# Python_stack
###genetic_drift_sim.py is a script to simulate the "genetic drift" in population genetics(Wright-Fisher model).
###Lib requirements: numpy, matplotlib.
###Run python genetic_drift_sim.py -h to see the usage of available arguments. If you want to have figure plotted, please make sure you have matplotlib module installed.
>usage: genetic_drift_sim.py [-h] [-v] [-plt {f_vs_t,t_dist,np,all}]
>                           [-o OUTPUT] [-p POP] [-s SIZE] [-f FREQ]

>optional arguments:
>  -h, --help            show this help message and exit

>  -v, --verbose         increase output verbosity

>  -plt {f_vs_t,t_dist,np,all}, --plot {f_vs_t,t_dist,np,all}
>                        whether output plot and need to specify plot type

>  -o OUTPUT, --output OUTPUT
>                        OUTPUT FILE

>  -r REP, --rep REP     specify how many replicates you want in the
>                        simulation, must be int

>  -s SIZE, --size SIZE  specify the population size you want in the
>                        simulation, must be int
###Be careful, the larger your population size is, the longer the program will run according to current setup. Maximum generation is set to 20 times population size.
>  -f FREQ, --freq FREQ  specify the initial frequency you want in the
>                        simulation, must be between 0 and 1

 
>Default output files are sim.rst.txt which contains the main result and sim.rst.txt.log that contains the frequency of each generation for each population.You can set up your own output name through -o. -v can give you the generation when either a fix or loss event happens in the result file.

>-plt, --plot accepts four options:

>"f_vs_t" will plot the frequency change over time for the first ten populations.

>"t_dist" will plot the histogram of the generation time when the allele is fixed or lost in the population. Suggest to use when number of population is greater than 30.

>"all" will plot both two plots above. Additionally, you will also have parameters and estimates in left bottom.

>"np" will plot nothing.

>-v to ouput with more details
