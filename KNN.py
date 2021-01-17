import pickle
class KNN_regression:
	def __init__(self):
	    
	    self.knn=pickle.load(open('model/knn.pickle','rb'))
	    self.scale=pickle.load(open('model/scaler.pickle','rb'))
	    
	def predict(self,x):
		t2=self.scale.transform(x.reshape((1,-1)))
		prediction=self.knn.predict(t2)[0]
		return prediction
        