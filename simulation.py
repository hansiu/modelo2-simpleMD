#! /usr/bin/env/python
#pomocnicze
import sys
#klasy
from atom import *
from vector import *
#algorytmy
from verlet import Verlet
from velocityVerlet import VelocityVerlet
from leapFrog import LeapFrog
#potencjały
from softWall import SoftWall
from minBarrierMin import MinBarrierMin
from lenardJones import LenardJones
#statystyki
from trajectoryAndStatistics import *

class Simulation:

    def __init__(self, dim=3,n_a=3,st=0.01,sts=100,algorithm='LeapFrog',force_fields=['SoftWall','MinBarrierMin'],parameters=[[1,10],[5,10,3,0.02]]):
        self.n_atoms=int(n_a)
        self.atoms=[Atom(dim,st) for i in range(self.n_atoms)]
        self.time_step=float(st)
        self.steps=int(sts)
        if algorithm=='Verlet':
            self.algorithm=Verlet()
        elif algorithm=='VelocityVerlet':
            self.algorithm=VelocityVerlet()
        elif algorithm=='LeapFrog':
            self.algorithm=LeapFrog()
        else:
            sys.exit('Wrong algorithm name')
        self.force_fields=[]
        for f in range(len(force_fields)):
            if force_fields[f]=='SoftWall':
                self.force_fields.append(SoftWall(parameters[f]))
                for a in self.atoms:
                    a.Recalculate(st,True)
            elif force_fields[f]=='MinBarrierMin':
                self.force_fields.append(MinBarrierMin(parameters[f]))
                for a in self.atoms:
                    a.Recalculate(st,True)
            elif force_fields[f]=='LenardJones':
                self.force_fields.append(LenardJones(parameters[f]))
                for a in self.atoms:
                    for i in range(a.coords_t.dim):
                        if a.coords_t[i]>=0:
                            a.coords_t[i]+=a.number
                        else:
                            a.coords_t[i]-=a.number
            else:
                sys.exit('Wrong potential name')
        
    def Run(self):
        for time_step in range(self.steps):
            if time_step==0:
                atom1=self.atoms[0]
            for atom in self.atoms:
                for ff in self.force_fields:
                    ff.Accelerate([atom])
                for atom2 in self.atoms[self.atoms.index(atom):]:
                    if atom!=atom2:
                        for ff in self.force_fields:
                            ff.Accelerate([atom,atom2])
                self.algorithm.Move(self.time_step,atom)
                for i in range(atom.coords_t.dim):
                    if atom.coords_t[i]>500:
                        sys.exit(str(atom))
            trajectory((time_step),self.atoms)
            stats((time_step),self.atoms)
        plot_stats()
        
    def __str__(self):
        return(str(self.atoms))
        
    def __repr__(self):
        return(str(self.atoms))