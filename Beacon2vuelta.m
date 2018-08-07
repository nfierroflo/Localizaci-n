x=xlsread('Mediciones.xlsx',3,'A5:A28');
y=xlsread('Mediciones.xlsx',3,'B5:B28');
z=log10(x);
ap1=-15.008*z-58.953;
%plot(z,y)
hold on
plot(x,y)
plot(x,ap1)
hold off