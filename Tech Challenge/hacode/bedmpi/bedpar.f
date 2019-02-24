          program bedpar
!
!       Chomosone ANDy program
!
!       Ralph Phillip Bording - Hudson Alpha Challenge - 2019
!
!
!**********************************************************************
!
         include "mpif.h" 


         integer  ierror
         integer  id
         integer  np
         real*4   wtime
!
!  Initialize MPI.
!
         call MPI_Init (ierror)


!
!  Get the number of processes.
!
         call MPI_Comm_size ( MPI_COMM_WORLD, np, ierror )


!
!  Get the individual process ID.
!
         call MPI_Comm_rank ( MPI_COMM_WORLD, id, ierror )
!
!  Print a message.
!
         if ( id == 0 ) then
           wtime = MPI_Wtime ( )
         endif

         if ( id == 0 ) then

           write (*,"(a)" ) ""
           write (*,"(a,i5,2x,a)") 
     x      "Proc", id, "HELLO_MPI - Master process:"
           write (*,"(a,i5,2x,a)") 
     x      "Proc", id, "FORTRAN/MPI version"
           write (*,"(a,i5,2x,a)") 
     x      "Proc", id, "An MPI test program."
           write (*,"(a,i5,2x,a,i8)") 
     x      "Proc", id, "The number of MPI processes is ", np

         end if
!
!  Every MPI process will print this message.
!
         write ( *, "(a,i5,2x,a)" ) 
     x           "Proc", id, """Hello, world!"""

         if ( id == 0 ) then

           write ( *, "(a)" ) ""
           write ( *, "(a,i5,2x,a)" ) "Proc", id,
     x       "HELLO_MPI - Master process:"
           write ( *, "(a,i5,2x,a)" ) "Proc", id,
     x       "  Normal end of execution: ""Goodbye, world!""."

         end if
!
!
!        do work here
!
         call ANDy(nsamp,idlr,idrf,nstream)
!
!
!
         if ( id == 0 ) then
           wtime = MPI_Wtime ( ) - wtime
           write ( *, '(a)' ) ''
           write ( *, '(a,i5,2x,a,g14.6,a)' )  
     x "Proc", id, "  Elapsed wall clock time = ", wtime, " seconds."
         end if
!
!  Shut down MPI.
!
         call MPI_Finalize ( ierror )
!
!  Terminate.
!
        if ( id == 0 ) then

        write ( *, "(a)" ) "          "
        write ( *, '(a,i5,2x,a)' ) 
     x       "Proc", id, "HELLO_MPI - Master process:"
        write ( *, '(a,i5,2x,a)' ) 
     x       "Proc", id, "  Normal end of execution."
        write ( *, "(a)" ) "          "
         end if

         stop
       end

       subroutine ANDy(nsamp,idlr,idrf,nstream)

       return
       end
