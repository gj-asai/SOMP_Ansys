import numpy as np
from scipy.sparse import coo_matrix
from scipy.ndimage import gaussian_filter

# https://www.rmit.edu.au/research/centres-collaborations/centre-for-innovative-structures-and-materials/software
"""
Weights: max{0, rmin-distance(i,j)}
"""
class ConvolutionFilter():
    def __init__(self, rmin, num_elem, centers):
        self.H = ConvolutionFilter.preFlt(rmin, num_elem, centers)
        
    def distances(matrixA, matrixB):
        A = np.matrix(matrixA)
        B = np.matrix(matrixB)
        Btrans = B.transpose()
        vecProd = A * Btrans
        SqA =  A.getA()**2
        sumSqA = np.matrix(np.sum(SqA, axis=1))
        sumSqAEx = np.tile(sumSqA.transpose(), (1, vecProd.shape[1]))    
        SqB = B.getA()**2
        sumSqB = np.sum(SqB, axis=1)
        sumSqBEx = np.tile(sumSqB, (vecProd.shape[0], 1))    
        SqED = sumSqBEx + sumSqAEx - 2*vecProd   
        elmDis = (np.maximum(0,SqED).getA())**0.5
        return np.matrix(elmDis)
    
    def preFlt(rmin, num_elem, centers):
        if rmin == 0: return np.identity(num_elem)
        try:
            limitElementNumber = 4000 # should be larger than (2*(rmin/elmsize)) ** 2
            nfilter=int(num_elem*limitElementNumber) 
            iH,jH,sH,cc = np.zeros(nfilter),np.zeros(nfilter),np.zeros(nfilter),0
            for ei in range(num_elem):
                ii = np.where(abs(centers[:,0] - centers[ei][0]) < rmin)[0]
                jj = np.where(abs(centers[ii,1] - centers[ei][1]) < rmin)[0]
                kk = np.where(abs(centers[ii[jj],2] - centers[ei][2]) < rmin)[0]
                neighbors = ii[jj][kk]
                iH[cc:cc+len(neighbors)] = ei
                jH[cc:cc+len(neighbors)] = neighbors
                eiH = np.maximum(0,rmin - ConvolutionFilter.distances(centers[ei],centers[neighbors]))
                sH[cc:cc+len(neighbors)] = eiH / np.sum(eiH)
                cc += len(neighbors)
            H = coo_matrix((sH,(iH,jH)),shape=(num_elem,num_elem))
        except:
            H = np.identity(num_elem)
            print('\n***   Insufficient memory or small limitElementNumber    ***\n')
        return H
    
class MeshIndependenceFilter(ConvolutionFilter):
    def __init__(self, rmin, num_elem, centers):
        super().__init__(rmin,num_elem,centers)
        
    def filter(self, rho, dc):
        return self.H.dot(rho*dc)/rho

class OrientationRegularizationFilter(ConvolutionFilter):
    def __init__(self, rmin, num_elem, centers):
        super().__init__(rmin,num_elem,centers)
        self.H = self.H.tocsr()
        
    def filter(self, theta):
        sign = np.sign(np.outer(theta,theta))
        sign[np.where(sign==0)] = -1
        return self.H.multiply(sign).dot(theta)
    
class GaussianFilter():   
    def __init__(self, num_elem, centers):
        self.num_elem = num_elem
        self.centers = centers
        self.x, self.y = np.meshgrid(np.unique(centers[:,0]),np.unique(centers[:,1]))
        
        # Matrix i,j correspondence for each element
        self.e = range(num_elem)
        self.i = []
        self.j = []
        for e in self.e:
            self.i.append(np.where(self.x[0,:] == self.centers[e,0])[0][0])
            self.j.append(np.where(self.y[:,0] == self.centers[e,1])[0][0])
        
    def filter(self, theta):
        theta_grid = np.zeros_like(self.x)
        theta_grid[self.j,self.i] = theta[self.e]
        
        theta_grid = gaussian_filter(theta_grid, sigma=3)
        
        thetanew = np.zeros_like(theta)
        thetanew[self.e] = theta_grid[self.j,self.i]
            
        return thetanew