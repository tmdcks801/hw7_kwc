import numpy as np
from numpy import dot
from numpy.linalg import norm

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

if __name__ == '__main__':
  Docs=np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
  docs1=Docs[0]
  docs2=Docs[1]
  docs3=Docs[2]
  
  query=[1,1,0,0,1,0]


  print("doc1:",round(cos_sim(docs1,query),2))
  print("doc2:",round(cos_sim(docs2,query),2))
  print("doc3:",round(cos_sim(docs3,query),2))
