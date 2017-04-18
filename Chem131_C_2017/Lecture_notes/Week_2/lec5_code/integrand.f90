PROGRAM integrand

  IMPLICIT NONE
  REAL, Parameter :: increment=0.001
  Integer, Parameter :: n = (1.3- 0)/increment
  REAL, DIMENSION(1:n) :: x, f, g, h
  INTEGER :: i

!======= Program to demonstrate stirling's approximation=============!
!============integrand of gamma function scaling====================!
!============ e^-x * x^n for large n ===============================!

! let's calculate values for the 2 functions between 0<x<2
! n is just some large number in these calculations, lets take it to be 100
x = 0
f = 0
g = 0
h = 0

  x(1) = 0.
  DO i =2,n
    x(i) = x(i-1) + increment
  END DO

  DO i = 1, n
    f(i) = expon(x(i))
  END DO
  
  DO i = 1, n
    g(i) = poly(x(i))
  END DO

  h = f*g

  OPEN (UNIT =1, FILE='data.dat')
  DO i=1,n
    WRITE(1,*) x(i), f(i), g(i), h(i)
  END DO
  CLOSE (UNIT=1)

  CONTAINS 

! function to calculation  f(x) = e^-x and g(x)=x^n values 
    FUNCTION expon(y) RESULT (values)
      IMPLICIT NONE
      REAL :: y, values

      values =  EXP(-y)

    END FUNCTION expon
    
    FUNCTION poly(y) RESULT (values)
      IMPLICIT NONE
      REAL :: y, values
      Integer, PARAMETER :: a=10

      values =  y**a

    END FUNCTION poly

END PROGRAM integrand
