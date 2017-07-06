# -*- coding: utf-8 -*-
from vector import *

class Atom:
    number=0
    mass=1
    
    def __init__(self,dim,scale):
        self.number=Atom.number
        Atom.number+=1
        self.mass=float(Atom.mass)
        self.coords_t=Vector().Random(dim,scale)
        self.coords_t_1=Vector(dim)
        self.velocity=Vector(dim)
        self.velocity_n=Vector(dim)
        self.acceleration=Vector(dim)
        self.acceleration_1=Vector(dim)
        self.k_energy=0
        self.p_energy=0

    def Recalculate(self,scale,acc):
        self.velocity=(self.coords_t-self.coords_t_1)*(1/scale)
        if acc:
            self.acceleration=(self.velocity)*(1/(scale))
        else:
            self.acceleration_1=(self.velocity)*(1/(scale))
        
    def SetNew(self,c):
        self.coords_t_1.NewCoords(self.coords_t.coords)
        self.coords_t.NewCoords(c.coords)
        self.acceleration_1.NewCoords(self.acceleration.coords)
        self.acceleration=Vector(self.acceleration.dim)

#    def __iter__(self):
#	return iter(self.coords)

    def __str__(self):
        return(str(self.number)+':'+str(self.coords_t))

    def __repr__(self):
        return('Atom: '+str(self.number)+' on position '+str(self.coords_t))
        
    def K_energy(self):
        self.k_energy=0.5*(self.mass * (self.velocity.length()**2))
        if self.velocity_n:
            self.velocity=self.velocity_n
            self.velocity_n=Vector(self.velocity_n.dim)
        return(self.k_energy)
        
    def P_energy(self):
        p=self.p_energy
        self.p_energy=0
        return(p)
