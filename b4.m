x=xlsread('Mediciones.xlsx',6,'A4:A16');
y=xlsread('Mediciones.xlsx',6,'B4:B16');
z=log10(x);
%plot(z,y)
ap1=-20.676*z-56.045;
hold on
plot(x,y)
plot(x,ap1)
hold off