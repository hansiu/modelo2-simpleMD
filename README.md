# modelo2-simpleMD
First program for a class in molecular modelling (done in june 2016). Its an implementation of simple Molecular Dynamics for atoms with a possibility to choose from different algorithms (Verlet, VelocityVerlet, Leepfrog) and potentials (Lenard-Jones, SoftWall, min-barrier-bin).

# How to use:
* Prepare the config.ini file (example in the example folder sym2) either by hand or using the MakeConfig function from configmaker.py
* Go for the main script: python main.py
* When it finishes it prints "END" - then in the folder in which the script was executed the following files should show:
    - traj.pdb is a pdb file with a trajectory that you can view i.e. in Chimera
    - energie.png is a graph of energies
    - stat.txt is a text file with energy statistics for a graph.
    
Note: if you are using Lenard-Jones's potential with some other potential, then please place the Lenard-Jones last on the list in the config.ini file. Otherwise the energies may be wrong - Lenard Jones potential calculates the energies in the other way than all the other potentials.
