import pickle
import time
tic = time.time()
with open('allSquares.pkl','wb') as file:
    sq = [i**2 for i in range(1,10**8)]
    pickle.dump(sq,file)
toc = time.time()
print('pickled in: ',toc-tic)
