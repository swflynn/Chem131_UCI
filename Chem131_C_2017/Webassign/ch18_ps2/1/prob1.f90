!This is a Fortran 90 program, comments are specified with !

! This problem is similar to Problem 18-9 in McQuarrie. 
! Plot the vibrational contribution to molar ehat capcity of Br2(g) from (250-1000)K
! From P.741 of McQuarrie : C = R(O/T)^2 (e^-o/T / (1-e^-o/T)^2)

! First we name our program
PROGRAM ch18_1  

!Next we define all our variables and the information they store
! Real is anything with a decimal, integer for whole numbers, Dimension is a vector
  IMPLICIT NONE
  REAL, PARAMETER :: vib_temp=463.      ! P. 739
  Real, Parameter :: increment=1
  Integer, Parameter :: n = (1001-250)/increment
  REAL, DIMENSION(1:n) :: T, C_v
  INTEGER :: i

! initialize all variables we are solving for to 0
  T = 0
  C_v = 0

! Set our initial temperature (indepedent variable) and fill a vector with the values. 
  T(1) = 250.
  DO i =2,n
    T(i) = T(i-1) + increment
  END DO

! Now solve for heat capacity  using our function defined below
  DO i = 1, n
    C_v(i) = heat_capacity(T(i))  ! For each T evaluate the function
  END DO

! Write our data to a file called data.dat T, C
  OPEN (UNIT =1, FILE='data.dat')
  DO i=1,n
    WRITE(1,*) T(i), C_v(i)
  END DO
  CLOSE (UNIT=1)

! Here we define a function we want to evaluate C at each T
  CONTAINS 

! our function takes in a value (T) and returns a value C_v(T)
    FUNCTION heat_capacity(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values
      
      values = (vib_temp / x)**2 * ((EXP(-(vib_temp / x))) / ((1. - EXP(-(vib_temp / x)))**2))

    END FUNCTION heat_capacity

! I will plot the data written to data.dat using a python script see plot.py code

END PROGRAM ch18_1
