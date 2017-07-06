from integrator import Integrator

class VelocityVerlet(Integrator):

    def __init__(self):
        Integrator.__init__(self)
        
    def Move(self,time_step,atom):
        newvel=atom.velocity + (atom.acceleration_1 + atom.acceleration)*0.5*time_step
        move=atom.coords_t + newvel*time_step + atom.acceleration*0.5*(time_step**2)
        atom.velocity_n=newvel
        atom.SetNew(move)