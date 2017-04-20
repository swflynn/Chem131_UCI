PROGRAM LJ

  IMPLICIT NONE     ! user defines variables
  REAL, Parameter :: increment=0.001 ! space between points
  Integer, Parameter :: upper = 2
  Integer, Parameter :: lower = .95
  Integer, Parameter :: n = (upper - lower)/increment ! actual number of points
  REAL, DIMENSION(1:n) :: r, PE
  INTEGER :: i
  REAL, Parameter :: eps=1.0 ! epsilon for argon (KJ) 1.65*10^21 J
  REAL, Parameter :: sig=1.0! space between points 3.4*10^-10 m

!======= Program to calculate L-J-12-6 Potential for Argon=============!
!============Potential energy as a function of r(angstrom) ====================!

r = 0
PE = 0

  r(1) = 0.95
  DO i =2,n
    r(i) = r(i-1) + increment
  END DO

  DO i = 1, n
    PE(i) = LJP(r(i))
  END DO
  
  OPEN (UNIT =1, FILE='data.dat')
  DO i=1,n
    WRITE(1,*) r(i), PE(i)
  END DO
  CLOSE (UNIT=1)

  CONTAINS 

! Lennard Jones 12-6 potential
    FUNCTION LJP(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values

      values =  4.0*eps*((sig**12/x**12) - (sig**6/x**6))

    END FUNCTION LJP
    
END PROGRAM LJ
