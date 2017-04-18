rm *.dat *.out *.png
gfortran integrand.f90
./a.out
python plot.py
