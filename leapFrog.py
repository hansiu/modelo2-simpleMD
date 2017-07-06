from integrator import Integrator

class LeapFrog(Integrator):

    def __init__(self):
        Integrator.__init__(self)
        
    def Move(self,time_step,atom):
        newvel=atom.velocity + atom.acceleration*time_step
        move=atom.coords_t + newvel*time_step
        atom.velocity_n=newvel
        atom.SetNew(move)