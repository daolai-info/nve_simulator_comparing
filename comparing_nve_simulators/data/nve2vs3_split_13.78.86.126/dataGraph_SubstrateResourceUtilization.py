import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick

subname = '2017-05-1805:05:31_recordsOutput.json'

#dirname = './nve1vs3_split_104.41.184.98/'
dirname = './'


nve_1_file = dirname + 'NVE#2_' + subname

nve_2_file = dirname + 'NVE#3_20_' + subname

nve_3_file = dirname + 'NVE#3_30_' + subname

nve_4_file = dirname + 'NVE#3_40_' + subname

nve_5_file = dirname + 'NVE#3_50_' + subname


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'


#key_1 = 'EmbeddedBandwidth', 
#key_11 = 'SublinkCost'
#Revenue to subcost = Revenue / SubCost
def showResourceUtilizationImage( key_1, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	sum_1 = 0
	index = 0
	for item_1 in record_1[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_2[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_3[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_4[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_5[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(item_1['Total'])
			sum_1 = 0


	print len(timing_1)
	#print timing_1
	print len(values_1)
	#print values_1
	print len(timing_2)
	#print timing_2
	print len(values_2)
	#print values_2
	print len(timing_3)
	#print timing_3
	print len(values_3)
	#print values_3
	print len(timing_4)
	#print timing_4
	print len(values_4)
	#print values_4
	print len(timing_5)
	#print timing_5
	print len(values_5)
	#print values_5


	fig, ax1 = plt.subplots()
 
	n_groups = len(timing_1)
	index = np.arange(n_groups)

	bar_width = 0.13

	opacity = 0.4

	ax1.bar(index, values_1, bar_width,
		color='b', edgecolor='none',
		label='NVE#2-SinglePath')


	ax1.bar(index + bar_width, values_2, bar_width,
                 color='g',edgecolor='none',
                 label='NVE#3-SplitRatio:20%')

	ax1.bar(index + (2 * bar_width), values_3, bar_width,
                 color='r',edgecolor='none',
                 label='NVE#3-SplitRatio:30%')

	ax1.bar(index + (3 * bar_width), values_4, bar_width,
                 color='c',edgecolor='none',
                 label='NVE#3-SplitRatio:40%')

	ax1.bar(index + (4 * bar_width), values_5, bar_width,
                 color='m',edgecolor='none',
                 label='NVE#3-SplitRatio:50%')

	ax1.set_ylabel(ytxt, color='k')
	ax1.set_xlabel(xtxt)

	ax1.set_xticks(index + 3 * bar_width)
	ax1.set_xticklabels(timing_1)
	
	ax1.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	formatter = FuncFormatter(to_percent)
	ax1.yaxis.set_major_formatter(formatter)


	[tl.set_color('k') for tl in ax1.get_yticklabels()]
	
	#ax1.set_ylim(0, 0.7 )
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )
	
	plt.grid(True)
	plt.title(title)
	plt.savefig(dirname + title + '.png')
	plt.close()


	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]


recordJson_1 = json.loads(open(nve_1_file).read())
recordJson_2 = json.loads(open(nve_2_file).read())
recordJson_3 = json.loads(open(nve_3_file).read())
recordJson_4 = json.loads(open(nve_4_file).read())
recordJson_5 = json.loads(open(nve_5_file).read())




limits = 250

#key_1 = 'EmbeddedBandwidth', 
#key_11 = 'SublinkCost'
#Revenue to subcost = Revenue / SubCost
showResourceUtilizationImage('SublinkResourceUtilization', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,  'Utilization','Time Unit(s)','A4 Evaluation of Substrate Link Resource Utilization')


