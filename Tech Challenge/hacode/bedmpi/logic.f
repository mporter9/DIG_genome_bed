          program logic

!
!
!         ANDy logic test
!
         character*20 head
!

         integer*2  istate(400 000 000)
         integer*8  ils(100),irs(100)
         integer*8  ilc(100),irc(100)

         nstate = 400 000 000
          
         do i=1,nstate
          istate(i) = 0
         enddo

         nk = 2

         read(5,'(a20)') head
         write(6,'(a20)') head
         do k=1,nk
          read(5,*)  ils(k),irs(k)
         enddo
         ils = ils + 1

         read(5,'(a20)') head
         write(6,'(a20)') head
         do k=1,nk
          read(5,*)  ilc(k),irc(k)
         enddo
         ilc = ilc + 1

         ilmin = min(ils(1),ilc(1))
         irmax = max(irs(nk),irc(nk))
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) " base chromosome     "
         write(6,*) "                     "
!        write(6,*)  ils,irs
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) " test chromosome     "
         write(6,*) "                     "
!        write(6,*)  ilc,irc
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) "  search boundaries  "
         write(6,*) "                     "
         write(6,*)  ilmin,irmax
         write(6,*) "                     "

         do k=1,nk
          do j=ils(k),irs(k)
            istate(j) = 1
          enddo

          do j=ilc(k),irc(k)
            if( istate(j) .eq. 1 ) then
              istate(j) =  3
            else
              istate(j) =  2
            endif
          enddo
         enddo

         write(6,*) "                     "
         write(6,*) "  solution space     "
         write(6,*) "                     "
          do j=ilmin,irmax
             if( istate(j) .ne. 0 ) then
               write(6,*) j,istate(j)
             endif
          enddo

         write(6,*) "                     "
         write(6,*) "                     "
          end
