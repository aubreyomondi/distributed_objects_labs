from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_processors = comm.Get_size()

if rank != 0:
    message = "Hello from process " + str(rank)
    comm.send(message, dest=0)
else:
	for pid in range(1, n_processors):
		message = comm.recv(source=pid)
		print("Process 0 receives message from process {}: {}".format(pid, message))
