from forceField import ForceField
from vector import *
from copy import copy,deepcopy

class SoftWall:

    def __init__(self,args):
        ForceField.__init__(self)
        self.f=float(args[0])/2
        self.L=float(args[1])
    
    def Accelerate(self,atoms):
        if len(atoms)==2:
            pass
        elif len(atoms)==1:
            atom=atoms[0]
            pot_energy=0
            acc=Vector(atom.acceleration.dim)
            for i in range(atom.coords_t.dim):
                if atom.coords_t[i]>self.L:
                    acc[i]=-2*(self.f)*(atom.coords_t[i]-self.L)
                    pot_energy+=self.f*((self.L-atom.coords_t[i])**2)
                elif atom.coords_t[i]<-self.L:
                    acc[i]=-2*(self.f)*(self.L+ atom.coords_t[i])
                    pot_energy+=self.f*((self.L+atom.coords_t[i])**2)
            atom.acceleration+=acc*(1/atom.mass)
            atom.p_energy+=pot_energy
        else:
            sys.exit('Soft Wall potential gets 1 atom')