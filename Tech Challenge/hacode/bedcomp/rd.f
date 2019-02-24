        program readbed
!
!          R. P. Bording - HA Tech Challenge - 2019
!


        integer*8   invec(2,100 000 000)

        character*4  cromo
        character*4  croml

        cromo(1:4) = "    "
        croml(1:4) = "    "

        line = 0
  99    continue

        read(5,*,end=100)  cromo,iv1,iv2
        line =  line + 1

!       write(6,200)  cromo,iv1,iv2

        if( croml .ne. cromo ) then
                  
        write(6,200)  cromo,iv1,iv2

        endif
        croml(1:4)  = cromo(1:4)

 200    format(3x,a4,2i18)

        go to 99
 100    continue

        write(6,201)  line

 201    format(10x," file has ",i15," lines of data ")

        end
