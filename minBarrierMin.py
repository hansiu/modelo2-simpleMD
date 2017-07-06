from forceField import ForceField
from math import e
from vector import Vector

class MinBarrierMin:

    def __init__(self,args):
        ForceField.__init__(self)
        self.a=float(args[0])
        self.b=float(args[1])
        self.c=float(args[2])
        self.d=float(args[3])
        
    def Accelerate(self,atoms):
        if len(atoms)==2:
            pass
        elif len(atoms)==1:
            atom=atoms[0]
            acc=Vector(atom.acceleration.dim)
            pot_energy= -self.a * (e ** (-self.b * (atom.coords_t[0] - 1) ** 2)) - self.c * (e ** (-(atom.coords_t[0] + 1) ** 2)) + self.d * (atom.coords_t[0]) ** 4
            for i in range(atom.coords_t.dim):
                acc[i]=-float(4)*self.d*(atom.coords_t[i]**3)
                acc[i]-=float(2)*self.a*self.b*(atom.coords_t[i]-1)*(e**(-self.b*((atom.coords_t[i]-1)**2)))
                acc[i]-=float(2)*self.c*(atom.coords_t[i]+1)*(e**(-(atom.coords_t[i]+1)**2))
            atom.p_energy+=pot_energy
            atom.acceleration+=acc*(1/atom.mass)
        else:
            sys.exit('Minimum-Barrier-Minimum potential gets 1 atom')