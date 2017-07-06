#! /usr/bin/env/python
from matplotlib import pyplot

def trajectory(step,atoms):
    if step==0:
        traj=open('traj.pdb','w')
        traj.close()
    traj=open('traj.pdb','a')
    traj.write('MODEL '+str(step)+'\n')
    for atom in atoms:
        cors=''
        for i in range(atom.coords_t.dim):
            cors+=str(round(atom.coords_t[i],3)).rjust(8)
        for j in range(3-atom.coords_t.dim):
            cors+='0'.rjust(8)
        traj.write('HETATM'+str(atom.number).rjust(5)+'  CA  UNK A'+str(atom.number).rjust(4)+'    '+cors+'                       C  \n')
    traj.write('ENDMDL\n')

def stats(step,atoms):
    pass
    if step==0:
        stat=open('stat.txt','w')
        stat.close()
    stat=open('stat.txt','a')
    p_e=0.0
    k_e=0.0
    for atom in atoms:
        p_e+=atom.P_energy()
        k_e+=atom.K_energy()
    stat.write(str(step)+';'+str(p_e)+';'+str(k_e)+';'+str(p_e+k_e)+'\n')
    
def plot_stats():
    file=open('stat.txt')
    steps=[]
    Ps=[]
    Ks=[]
    Alls=[]
    for line in file:
        line=line.split(';')
        steps.append(line[0])
        Ps.append(line[1])
        Ks.append(line[2])
        Alls.append(line[3])
    steps=steps
    pyplot.xlabel('krok')
    pyplot.ylabel('energie')
    pyplot.plot(steps,Ps, color='green',label='energia potencjalna')
    pyplot.plot(steps,Ks,color='red',label='energia kinetyczna')
    pyplot.plot(steps,Alls,color='brown',label='energia calkowita')
    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, mode='expand',ncol=2,borderaxespad=0.)
    pyplot.savefig('energie.png')
    pyplot.clf()
    pyplot.close()