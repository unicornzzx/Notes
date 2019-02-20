import os
from multiprocessing import Pool

def blur(n)
    time.sleep(0.2)
    print (n*n)

if __name__ == "__main__":

    test_1 = [0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7,4,5,6,7,8]
    for n in test_1:
        blur(n)

        
    for i in range(5):
        test = [i,i+1,i+2,i+3,i+4]
        pool = Pool(10)
        pool.map(blur,test)
        pool.close()
        pool.join()
