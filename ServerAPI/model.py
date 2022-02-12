import pickle
import sklearn
import pandas

class Model():

	def __init__(self):

		filename = 'finalized_model.sav'
		self.loaded_model = pickle.load(open(filename, 'rb'))

	def predict(self,data):

		return self.loaded_model.predict(data[0:1])
