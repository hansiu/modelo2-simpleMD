from forceField import ForceField
from vector import Vector
from math import sqrt

class LenardJones:

    def __init__(self,args):
        ForceField.__init__(self)
        self.R=float(args[0])
        self.eps=float(args[1])
        
    def Accelerate(self,atoms):
        if len(atoms)==1:
            return(0)
        elif len(atoms)==2:
            acc1=Vector(atoms[0].acceleration.dim)
            acc2=Vector(atoms[1].acceleration.dim)
            dist=0.0
            pot_energy=0
            for i in range(atoms[0].coords_t.dim):
                dist+=(atoms[1].coords_t[i]-atoms[0].coords_t[i])**2
            if dist:
                dist=sqrt(dist)
                acc=-12*self.eps*(self.R**6)*(self.R**6 - dist**6)/(dist**13)
                acc1=(atoms[1].coords_t-atoms[0].coords_t).UnitVector()*acc
                acc2=(atoms[0].coords_t-atoms[1].coords_t).UnitVector()*acc
                pot_energy=self.eps*((self.R *(1/dist))**12 - 2*((self.R*(1/dist))**6))
            atoms[0].p_energy+=pot_energy/2
            atoms[1].p_energy+=pot_energy/2
            atoms[0].acceleration+=acc1*(1/atoms[0].mass)
            atoms[1].acceleration+=acc2*(1/atoms[1].mass)
        else:
            sys.exit('LenardJones potential gets 2 atoms')

