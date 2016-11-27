# -*- coding: utf-8 -*-

import tushare as ts
import pandas  as pd
import numpy   as np
import random



## --------------------------------------------------------------- ##
## TODO: how to append the trading date we need?

def initial_trading_date():
	'''
	return a list containing traiding date
	'''
	list = []

	list.append( '2011-01-04' )
	list.append( '2012-01-04' )
	list.append( '2013-01-04' )
	list.append( '2014-01-04' )

	return list
## --------------------------------------------------------------- ##

def initial_index():
	'''
	download the stock code
	return a list containing stock code
	'''

	## return ts.get_stock_basics().index
	return ts.get_sz50s().code ## which doesn't work
	## return ts.get_hs300s().code
	## return ts.get_sz50s().code
	## return ts.get_zz500s().code

## --------------------------------------------------------------- ##
## TODO: delete all the stocks with label "st"

def random_draw( df, n ):
	'''
	return a list which chooses n random objects from df
	'''

	## TODO: this is NOT a real random!!
	return df.take( np.random.permutation( len( df ) )[:n] ).values
	## if in the function initial_index(),
	## return ts.get_stock_basics().index
	## then we return df.take( np.random.permutation( len( df ) )[:n] )


## --------------------------------------------------------------- ##

def asset_date_return( list_asset_all, num_select_stock, list_date ):
	list = []

	'''
	Remark:
	the look is from 0 to n-2, where is the size of 'list_date'
	'''
	for i in xrange( len( list_date ) - 1 ):
		print '\t The date is %r ' %list_date[i]
		list_asset = random_draw( list_asset_all, num_select_stock )

		print '\t\t the asset set is %r' %list_asset

		tmp_average = 0.0

		for j in xrange( len( list_asset ) ):
			print '----------\n the asset is %r' %list_asset[j]
			df = ts.get_k_data( code = list_asset[j],
			 	   			   start = list_date[i] ,
								 end = list_date[i+1] )

			x1 = 0
			x2 = 0
			x1 = df[ df.date == list_date[i]   ].close.values
			x2 = df[ df.date == list_date[i+1] ].close.values
			print "the current price of the asset is %r, and the next year is%r"\
			 %(x1,x2 )

			tmp = x2[0] / x1[0] * 1.0 - 1.0
			print 'the percentage of price change is %r' %tmp

			tmp_average += tmp
		print '\n the tmp_average is %r\n\n' %tmp_average

		list.append( tmp_average / len( list_asset ) )

	print '\n the list is %r' %list
	return list

## --------------------------------------------------------------- ##

##TODO: compute the return during each period  for at least 10 years

def main( num_iteration = 5, num_select_stock = 2 ):
	## get the trading date
	list_date  = initial_trading_date()

	## choose n indexes from the full index set
	list_index = initial_index()

	## the list which is exactly what we need to record the final return
	list_final_rtn = []

	for i in xrange( num_iteration ):
		print '\n\n=====================\n Round %r' %i

		## test for the code
		## list_index_random = ['601668', '000002', '600000', '600007']
		## list_index_random = random_draw( list_index, num_select_stock )
		list_final_rtn.append( asset_date_return( list_index,
													num_select_stock,
													list_date ) )
		print '\n list_final_rtn is %r' %list_final_rtn

	return list_final_rtn


list_my_rtn = main(5,2)
print '\n\n\n'
print list_my_rtn


## --------------------------------------------------------------- ##
##TODO: record the total return for the iteration



## --------------------------------------------------------------- ##
## TODO: analyze the performance of the algorithm
