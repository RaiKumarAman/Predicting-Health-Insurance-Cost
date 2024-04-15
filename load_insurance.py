import numpy as np
import pickle 

load_model= pickle.load(open(r"C:\Users\Aman\OneDrive\Documents\Python\Medical Insurance Cost Predicition\insurance.sav", 'rb'))

input_data=(31,1,25,74,0,1)

data1=np.asarray(input_data)

data=data1.reshape(1,-1)

prediction=load_model.predict(data)

print("charges are:", prediction[0])

