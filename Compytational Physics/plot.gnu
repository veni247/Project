set terminal pngcairo
set output 'EulerODE_plot.png'
set title 'Giải phương trình vi phân bằng phương pháp Euler'
set xlabel 'x'
set ylabel 'y'
plot 'EulerODE.txt' using 1:2 with linespoints title 'y = f(x)'