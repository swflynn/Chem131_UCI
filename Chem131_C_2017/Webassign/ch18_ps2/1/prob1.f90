!This is a Fortran 90 program (.f90), comments are specified with !

! This problem is similar to Problem 18-9 in McQuarrie. 

!====================================Question=======================================!
! Plot the vibrational contribution to molar ehat capcity of Br2(g) from (250-1000)K
!====================================Question=======================================!

!====================================Solution=======================================!
! From P.741 of McQuarrie : C = R(O/T)^2 (e^-o/T / (1-e^-o/T)^2)
!====================================Solution=======================================!

!====================================Program=======================================!
! Simple program to calculate C/R as a function of T from 250-1000 K
!====================================Program=======================================!

! First we name our program
PROGRAM ch18_1  

!Next we define all our variables 
  IMPLICIT NONE
  REAL, PARAMETER :: vib_temp = 463.      ! McQuarrie P. 739
  Real, Parameter :: increment = 1        ! Calculate for each whole number
  Integer, Parameter :: n = (1001-250)/increment ! Number of Evaluations
  REAL, DIMENSION(1:n) :: T, C_v          ! Our Data!!!!
  INTEGER :: i                            !Looping Variable

!================================Data Types=======================================!
! Real = anything with a decimal
! integer = whole numbers
! Dimension = vector or matrix (a list of numbers is a vector)  
!================================Data Types=======================================!

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
    C_v(i) = heat_capacity(T(i))  ! For each T(i) evaluate C(T)
  END DO

! Write our data to a file called data.dat:  T, C
  OPEN (UNIT =1, FILE='data.dat')
  DO i=1,n
    WRITE(1,*) T(i), C_v(i)
  END DO
  CLOSE (UNIT=1)

! Here we define our function; we want to take a value of T and calculate C_v
  CONTAINS 

! our function takes in any value (x) and returns a number (values)
    FUNCTION heat_capacity(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values
      
      values = (vib_temp / x)**2 * ((EXP(-(vib_temp / x))) / ((1. - EXP(-(vib_temp / x)))**2))

    END FUNCTION heat_capacity

! I will plot the data written to data.dat using a python script see plot.py code

END PROGRAM ch18_1
