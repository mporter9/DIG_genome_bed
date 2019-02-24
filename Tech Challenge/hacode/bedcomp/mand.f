        program mand
!
!          R. P. Bording - HA Tech Challenge - 2019
!


        integer*8   intl(100 000 000)
        integer*8   intr(100 000 000)

        character*4  cromo
        character*4  cromn
        character*4  croml

        cromo(1:4) = "    "
        croml(1:4) = "    "
        cromn(1:4) = "    "

        ltotal = 0
        line = 0
        nfile = 0
        ifirst = 0
  99    continue

        read(5,*,end=100)  cromn,iv1,iv2
        if( ifirst .ne. 0 .and. (cromn .ne. cromo )) then
!
!    end of file section -- process data
! 
        nfile =  nfile + 1

        write(6,209) cromn,cromo
 209    format(a4,1x,a4)
        do ip=1,4
          write(6,*)  ip,intl(ip),intr(ip)
        enddo

        write(6,*)  line,nfile


        call dataout(cromo,line,intl,intr,nfile,ltotal)
        write(6,*) "           "


        else
        line =  line + 1
        intl(line) = iv1
        intr(line) = iv2
        endif
        ifirst = 1
 
        cromo = cromn

!       write(6,200)  cromo,iv1,iv2

        if( croml .ne. cromo ) then
                  
        write(6,200)  cromo,iv1,iv2

        endif
        croml(1:4)  = cromo(1:4)

 200    format(3x,a4,2i18)

        go to 99
 100    continue
!
!    end of file -- process data
!
        nfile =  nfile + 1
        call dataout(cromo,nline,intl,intr,nfile,ltotal)

        write(6,201)  line

 201    format(10x," file has ",i15," lines of data ")

        end

        subroutine dataout(cromo,nline,intl,intr,nfile,ltotal)

        integer*8   intl(100 000 000)
        integer*8   intr(100 000 000)
        real*8      sum
 
        character*4 cromo

        open(nfile+10,form="formatted")

        ilsft = intl(1)
        irlft = intr(nline)
        sum = 0.0d00
        ltotal = ltotal + 1
        do jj=1,nline
          write(nfile+10,203) cromo,intl(jj),intr(jj)
          sum = sum + intr(jj)-intl(jj)
          ltotal = ltotal + 1
        enddo
 203    format(a4,1x,i15,1x,i15)
        savg = sum/float(nline)

        write(6,*) " file has first - last entries ",
     x              ilfst,irlft,savg

        close(nfile+10)
        return
        end
