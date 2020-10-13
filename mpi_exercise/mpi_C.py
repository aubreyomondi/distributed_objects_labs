from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_processors = comm.Get_size()

total = 0

if rank == 1:
    message = (4 + 2 * 6)
    comm.send(message, dest=0)
elif rank == 2:
    message = (2 * 6 + 2 * 4)
    comm.send(message, dest=0)
elif rank == 3:
    message = (2 * 4 + 5)
    comm.send(message, dest=0)
else:
    for pid in range(1, n_processors):
        message = comm.recv(source=pid)
        print("Process 0 receives message from process {}: {}".format(pid, message))
        total += int(message)
    print("The area under the curve is {}".format(total))