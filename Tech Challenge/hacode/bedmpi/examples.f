
         call MPI_Init ( ierr )

         call MPI_Comm_rank ( MPI_COMM_WORLD, id, ierr )

         call MPI_Comm_size ( MPI_COMM_WORLD, np, ierr )

         call MPI_Finalize ( ierr )

         integer ( kind = 4 ) status(MPI_STATUS_SIZE)

         call MPI_Send ( h(1), 1, MPI_DOUBLE_PRECISION, id-1, tag, &
           MPI_COMM_WORLD, ierr )

         call MPI_Recv ( h(n+1), 1,  MPI_DOUBLE_PRECISION, id+1, tag, &
           MPI_COMM_WORLD, status, ierr )

         call MPI_Send ( h(n), 1, MPI_DOUBLE_PRECISION, id+1, tag, &
           MPI_COMM_WORLD, ierr )

         call MPI_Recv ( h(0), 1, MPI_DOUBLE_PRECISION, id-1, tag, &
           MPI_COMM_WORLD, status, ierr )







