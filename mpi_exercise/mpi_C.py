from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_processors = comm.Get_size()

# y_values = [4, 6, 6, 4, 4, 5] 
# x_values = [0, 2 ,4 , 6, 8, 10]

# subintervals = 5

# width = (max(x_values) - min(x_values)) / subintervals
total = 0

# for i, y in enumerate(y_values):
#         if (i == 0) or (i == len(y_values)-1):
#             total += y
#         else:
#             total += (2 * y)

if rank != 0:
    message = 1
    comm.send(message, dest=0)
else:
    for pid in range(1, n_processors):
        message = comm.recv(source=pid)
        print("Process 0 receives message from process {}: {}".format(pid, message))
        total += int(message)
    print("The area under the curve is {}".format(total))

# message = comm.recv(source=pid)
# print("Process 0 receives message from process {}: {}".format(pid, message))
# total += int(message)
# print("The area under the curve is {}".format(total))
# print("The area under the curve is {}".format((width / 2) * total))