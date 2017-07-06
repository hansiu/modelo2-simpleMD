from integrator import Integrator

class Verlet(Integrator):

    def __init__(self):
        Integrator.__init__(self)
        
    def Move(self,time_step,atom):
        vel=(atom.coords_t - atom.coords_t_1)*(1/time_step)
        atom.velocity=vel
        move=(2*atom.coords_t) - (atom.coords_t_1) + (atom.acceleration*(time_step**2))
        atom.SetNew(move)