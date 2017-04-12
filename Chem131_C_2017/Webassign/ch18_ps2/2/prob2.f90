PROGRAM ch18_1  

! set all paramaters to 1 for simplicity

  IMPLICIT NONE
  REAL, PARAMETER :: rot_temp=12.02
  REAL, PARAMETER :: T=300
  REAL, PARAMETER :: T2=1000
  Real, Parameter :: increment=1
  Integer, Parameter :: n = (50-0)/increment
  REAL, DIMENSION(1:n) :: j, f, g
  INTEGER :: i

  f = 0
  j = 0
  g = 0

  j(1) = 0
  DO i =2,n
    j(i) = j(i-1) + increment
  END DO

  DO i = 1, n
    f(i) = population(j(i))
  END DO
  
  DO i = 1, n
    g(i) = population2(j(i))
  END DO

  OPEN (UNIT =1, FILE='data.dat')
  DO i=1,n
    WRITE(1,*) j(i), f(i), g(i)
  END DO
  CLOSE (UNIT=1)

  CONTAINS 

! function to calculation x, f(x) values 
    FUNCTION population(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values
      
      values = (2.*x +1.) * (rot_temp / T) * (EXP(-(rot_temp*x*(x+1))/T))

    END FUNCTION population
    
    FUNCTION population2(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values
      
      values = (2.*x +1.) * (rot_temp / T2) * (EXP(-(rot_temp*x*(x+1))/T2))

    END FUNCTION population2

END PROGRAM ch18_1
