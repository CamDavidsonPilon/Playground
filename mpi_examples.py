#use with command mpirun -np 10 python mpi_examples.py




from mpi4py import MPI
from time import sleep
import numpy as np

comm = MPI.COMM_WORLD
num_cpus = comm.size
rank = comm.rank

max_elemement_to_sort = 20

#scatter destination
domain = np.array([0.0])

#gather destination
c = np.zeros( num_cpus, dtype="float" )


#create a random array from 1-20
if comm.rank == 0: 
    to_sort = max_elemement_to_sort*np.random.random(comm.size)
    print "Attempting to sort: ", to_sort
else: 
    to_sort = np.empty( comm.size, dtype = np.float64)


comm.Scatter( [to_sort, MPI.DOUBLE], [domain, MPI.DOUBLE] )
sleep( domain[0]/10 )

print "Rank %d from %d running in total. Returning %f"%(comm.rank, comm.size, domain[0])
#send receive command here?

comm.Gather( [domain[0], MPI.DOUBLE ], [c, MPI.DOUBLE] )

if rank == 0:
    print 'Sorted: ',c







