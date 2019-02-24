          program logic

!         Ralph Phillip Bording - Hudson Alpha Tech Challenge - 2019
!
!         ANDy logic two data case version
!
         character*20 head
         character*30 fnames
         character*30 fnamec

         character*4 croms
         character*4 cromo
!
         real*4 plot(3048)

         integer*2  istate(800 000 000)
         integer*8  ils(100000),irs(100000)
         integer*8  ilc(100000),irc(100000)

         nstate = 400 000 000
          
         do ip=1,2048
          plot(ip) = 0.0
         enddo
         do i=1,nstate
          istate(i) = 0
         enddo

         fnames(1:30) ="../bedcomp/case1/fort.11      "
         fnamec(1:30) ="../bedcomp/case2/fort.11      "
!lllllllllllllllllllllll123456789012345678901234567890
         write(6,*) fnames(1:30)
         write(6,*) fnamec(1:30)

         open(10,file=fnames(1:30),form="formatted")


         k = 0
  99     continue
          read(10,*,end=100) croms,ilst,irst
          k = k + 1
          ils(k) = ilst
          irs(k) = irst
         go to 99
 100     continue
         kss = k 

         close(10)
         open(11,file=fnamec(1:30),form="formatted")
         k = 0
  98     continue
          read(11,*,end=101) croms,ilct,irct
          k = k + 1
          ilc(k) = ilct
          irc(k) = irct
         go to 98
 101     continue
         kcc = k 

         close(11)



         ilmin = min(ils(1),ilc(1))
         irmax = max(irs(kss),irc(kcc))
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) " base chromosome     "
         write(6,*) "                     "
         write(6,*)  ils(1),irs(kss)
         write(6,*) "  length in pairs is ",kss        
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) " test chromosome     "
         write(6,*) "                     "
         write(6,*)  ilc(1),irc(kcc)
         write(6,*) "  length in pairs is ",kcc        
         write(6,*) "                     "
         write(6,*) "                     "
         write(6,*) "  search boundaries  "
         write(6,*) "                     "
         write(6,*)  ilmin,irmax
         write(6,*) "                     "

         do k=1,kss
          do j=ils(k),irs(k)
            istate(j) = 1
          enddo
         enddo

         do k=1,kcc
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

         nrecl = 4*2048
         open(20,file="chromo.plot",form="unformatted",
     x          access="direct",recl=nrecl)

         write(6,*) "                     "
         write(6,*) " file open           "
         write(6,*) "                     "

         irec = 0
         ic3 = 0
         ic4 = 0

          do j=ilmin,irmax

               ic4 = ic4 + 1
               plot(ic4) = istate(j)

                 if( ic4 .eq. 2048 ) then
                 ic4 = 0
                 write(6,*) "  plot trace full ",j,ic4
                 k3c = 0
                 do ipc=1,2048
                   if( plot(ipc) .gt. 1.5 ) then
                   k3c = k3c + 1
                   endif
                 enddo
                 write(6,*) "  plot trace counted "

                 if( k3c .gt. 10 ) then
                 irec = irec + 1
                  write(20,rec=irec) (plot(ipc),ipc=1,2048) 
                 if( irec .gt. 512 ) go to 88
                 endif
                 write(6,*) "  plot trace written "

               endif

             if( istate(j) .eq. 3 ) then
              ic3 = ic3 + 1
!              write(6,*) j,istate(j)
             endif

!                write(6,*) "  end of loop  "
          enddo

 88      continue
         close(20)
         write(6,*) "  file close "
         write(6,*) " Overlap Count ",ic3

         write(6,*) "                     "
         write(6,*) " start index   -- end index "
         write(6,*) "                     "
         write(6,*) ilmin,irmax
         write(6,*) "                     "

         
          end
