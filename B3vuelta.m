x=xlsread('Mediciones.xlsx',5,'A5:A64')
y=xlsread('Mediciones.xlsx',5,'B5:B64');
z=log10(x);
%plot(z,y)
ap1=-19.933*z-55.097;
hold on
plot(x,y)
plot(x,ap1)
hold off
