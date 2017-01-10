#! /usr/bin/python
from __future__ import division
import random
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity",default=False,action="store_true")
parser.add_argument("-plt","--plot", help="whether output plot and need to specify plot type",choices=['f_vs_t','t_dist','np',"all"],default="np",type=str)
parser.add_argument("-o","--output", help="OUTPUT FILE",default="sim.rst.txt",type=argparse.FileType('w', 0))
parser.add_argument("-r","--rep", help="specify how many replicates you want in the simulation, must be int",default=1,type=int)
parser.add_argument("-s","--size", help="specify the population size you want in the simulation, must be int",default=1,type=int)
parser.add_argument("-f","--freq", help="specify the initial frequency you want in the simulation, must be between 0 and 1",default=0.5,type=float)
args=parser.parse_args()
popc=args.pop
popsize=args.size
init_freq=args.freq
logfile=open(args.output.name+".log",'w+')
out=open(args.output.name,'w+')	
#def popInit(pop_size,allele_freq):
#	A_allele_number=2*pop_size*allele_freq
#	return A_allele_number

def mate_event(pop_size,allele_freq):
	allele_A_new=0
	for i in range(0,pop_size*2):
		if np.random.random()<allele_freq :
			allele_A_new += 1
		else:
			continue
	return allele_A_new


class SimGeneticDrift():
	def __init__(self,popsize,init_freq,generationtime):
		 self.popsize=popsize
		 self.init_freq=init_freq
		 self.gt=generationtime
	def run_sim(self):
		alfreq=self.init_freq
		tplot=list()
		for i in range (0,self.gt+1):
			logfile.write(str(i)+' '+str(alfreq)+'\n')
			sys.stdout.write("\rGeneration:%d" % i)
			sys.stdout.flush()
			tplot.append(alfreq)
			new=mate_event(self.popsize,alfreq)
			alfreq=new/(2*self.popsize)
			if alfreq==0 or alfreq==1 :
				i=i+1
				tplot.append(alfreq)
				logfile.write(str(i)+' '+str(alfreq)+'\n')
				break
		return alfreq,i,tplot

			
def mulsim(popc,popsize,init_freq):
	est_run_times=popsize*20
	count_fix=0
	count_loss=0
	count_mid=0
	fix_time=dict()
	loss_time=dict()
	tplotdata=dict()
	for i in range(1,popc+1) :
		a=SimGeneticDrift(popsize,init_freq,est_run_times)
		logfile.write("Popoluation "+str(i)+":"+"\n")
		tk=a.run_sim()
		ost="Fixed!"
		if tk[0] == 1:
			count_fix += 1
			fix_time[i]=tk[1]
			ost="Fixed!"
		elif tk[0] == 0:
			count_loss += 1
			loss_time[i]=tk[1]
			ost="Loss!"
		else:
			count_mid += 1
			ost="Somewhere!"
		print " pop",i,"complete! ",ost,"\n"
		if args.plot == 'f_vs_t' or 'all':
			#print "parameter read"
			tplotdata[i]=tk[2]
		else:
			pass
	out.write(str(args)+"\n")
	out.write("Fixed\tLoss\tMid\n")
	out.write(str(count_fix)+'\t'+str(count_loss)+'\t'+str(count_mid)+"\n")
	if args.verbose is True:
		try:
			for key in fix_time.keys():
				out.write("In pop "+str(key)+' allele was fixed at '+str(fix_time[key])+"!\n")
		except (KeyError):
			pass
		try:
			for key in loss_time.keys():
				out.write("In pop "+str(key)+' allele was lost at '+str(loss_time[key])+"!\n")
		except (KeyError):
			pass
	
	fix_array=list()
	loss_array=list()
	for key in fix_time.keys():
		fix_array.append(fix_time[key])	
	for key in loss_time.keys():
		loss_array.append(loss_time[key])
	meanf=np.mean(np.array(fix_array))
	meanl=np.mean(np.array(loss_array))
	stdf=np.std(np.array(fix_array))
	stdl=np.std(np.array(loss_array))
	out.write("mean(AvgFixTime)"+str(meanf)+" sd:"+str(stdf)+"\n")
	out.write("mean(AvgLossTime)"+str(meanl)+" sd:"+str(stdl)+"\n")
	####PLOT######
	####plot allele freq vs time ####
	#print "PLOTTING .....",args.plot
	if args.plot == 'f_vs_t':
		tplot_x_max = np.arange(0, est_run_times, 1)
		for key in tplotdata.keys(): 
			if key <= 10 :
				plt.plot(tplotdata[key])				
			else:
				pass
		plt.show()
	elif args.plot == 't_dist':
		print "Suggest that doing this when your tested population is over 30 only!"
		new_ar=[fix_array,loss_array]
		plt.subplots_adjust(wspace=0.5)
		plt.subplot(211)
		plt.hist(fix_array, 20, normed=1, facecolor='b')
		plt.hist(loss_array,20, normed=1, facecolor='r')
		plt.subplot(212)
		b=plt.boxplot(new_ar,labels=['fix','loss'],notch =True, vert=False)
		#plt.boxplot(loss_array, notch =True,vert=False)
		plt.show()
	elif args.plot == 'np' :
		pass
	elif args.plot == 'all' :
		plt.subplots_adjust(wspace=0.5,hspace=0.5)
		plt.subplot(221)
		for key in tplotdata.keys():
			if key <= 10 :
				plt.plot(tplotdata[key])				
			else:
				pass
		plt.title('Frequence vs generation time', fontsize=12)
		#plt.show()
		fix_array=list()
		loss_array=list()
		for key in fix_time.keys():
			fix_array.append(fix_time[key])	
		for key in loss_time.keys():
			loss_array.append(loss_time[key])
		new_ar=[fix_array,loss_array]
		plt.subplot(222)
		plt.hist(fix_array, 20, normed=1, facecolor='b')
		plt.hist(loss_array,20, normed=1, facecolor='r')
		plt.title('Time distribution', fontsize=12)
		plt.subplot(223)
		plt.text(.1, .8,"Parameters:",size=15)
		plt.text(.1, .7,"Populations:"+str(popc),size=12)
		plt.text(.1, .6,"Population Size:"+str(popsize),size=12)
		plt.text(.1, .5,"Initial Allele Frequency:"+str(init_freq),size=12)
		plt.text(.1, .4,"Fix Event:"+str(count_fix),size=12)
		plt.text(.1, .3,"Loss Event:"+str(count_loss),size=12)
		#print "##",meanf,meanl
		if np.isnan(meanf) :
			plt.text(.5, .4,"Avg Fix Time: NaN",size=12)
		else:
		    plt.text(.5, .4,"Avg Fix Time:"+str(int(meanf)),size=12)
		if np.isnan(meanl) :
			plt.text(.5, .3,"Avg Loss Time: NaN",size=12)
		else:
			plt.text(.5, .3,"Avg Loss Time:"+str(int(meanl)),size=12)
		plt.draw()
		plt.subplot(224)
		plt.boxplot(new_ar,labels=['fix','loss'],notch =True, vert=False)
		plt.title('Time distribution', fontsize=12)
		plt.show()

mulsim(popc,popsize,init_freq)
