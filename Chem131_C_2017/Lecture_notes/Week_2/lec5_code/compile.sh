rm *.dat *.out
rm *.png
gfortran integrand.f90
./a.out
python plot.py
