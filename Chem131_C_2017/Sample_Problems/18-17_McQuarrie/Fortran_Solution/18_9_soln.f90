!This is a Fortran 90 program (.f90), comments are specified with ! and are not part of the code 

!====================================Question=======================================!
! Plot the vibrational contribution to molar heat capcity of Br2(g) from (250-1000)K
!====================================Question=======================================!

!====================================Solution=======================================!
! From P.741 of McQuarrie : C = R(O/T)^2 (e^-o/T / (1-e^-o/T)^2)
!====================================Solution=======================================!

!====================================Program=======================================!
! Simple program to calculate C/R as a function of T from 250-1000 K
! The data is written to a file data.dat
! See plot.py Python code for plotting this data file
!====================================Program=======================================!

PROGRAM ch18_9                            ! Name your program

!Next we define all our variables 

IMPLICIT NONE                           ! Statement Saying I will define the variables myself
REAL, PARAMETER :: vib_temp = 463.      ! McQuarrie P. 739
REAL, PARAMETER :: increment = 1        ! Calculate for each whole number
INTEGER, PARAMETER:: n = (1001-250)/increment ! Number of Evaluations we make
INTEGER :: i                            !Looping Variable
REAL, DIMENSION(1:n) :: T, C_v          ! Our Data: Temperature and Heat Capacity

!================================Data Types=======================================!
! Real = anything with a decimal
! integer = whole numbers
! Dimension = vector or matrix (a list of numbers is a vector) so a column of data  
! Parameter = value that cannot be changed during the code
!================================Data Types=======================================!
  
! initialize all variables we are solving for (make sure they start as 0)
  T = 0
  C_v = 0

! Set our initial temperature (indepedent variable) and fill a vector with the values. 
  T(1) = 250.                 ! T is a vector (a column of data), the first value is 250
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
! Our function takes in any value (x) and returns a number (values)
! Take in a temperature and use the equation to calculate heat capacity at that temperature

  CONTAINS                ! statement for adding a function of subroutine
    
    FUNCTION heat_capacity(x) RESULT (values)
      IMPLICIT NONE
      REAL :: x, values
      
      values = (vib_temp / x)**2 * ((EXP(-(vib_temp / x))) / ((1. - EXP(-(vib_temp / x)))**2))

    END FUNCTION heat_capacity

! I will plot the data written to data.dat using a python script see plot.py code

END PROGRAM ch18_9
