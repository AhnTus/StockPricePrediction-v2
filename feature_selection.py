#! /usr/bin/python
import sys
import os
import csv
import pandas

from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import StratifiedKFold
import numpy as np

def conv(s):
	try:
		s=float(s)
	except ValueError:
		pass    
	return s

def main(dir_path):

	files = os.listdir(dir_path)

	X = []
	y = []

	ranking = []

	for file_name in files:
		with open( os.path.join(dir_path, file_name), 'r') as textfile:
			data = pandas.read_csv(os.path.join(dir_path, file_name), header=0)
			#reader = csv.reader(textfile)
			#next(reader, None)

			start_test = datetime.datetime(2005, 1, 1)

			col = list(data.adj_close)

			X = [ col[:2] ]
			y = [ col[-1], col[-2] ]

			print X
			print y	
			

		X=np.array(X, np.float64)
		y=np.array(y, np.float64)

		estimator = LinearRegression()
		selector = RFECV(estimator, step=1, cv=StratifiedKFold(y, 2))
		
		selector = selector.fit(X, y)
		X = []
		y = []

		if len(ranking)!=0:
			ranking = [sum(x) for x in zip(ranking, selector.ranking_)]
		else:
			ranking = selector.ranking_

		print ranking

	print ranking

if __name__ == '__main__':
	main(sys.argv[1])
