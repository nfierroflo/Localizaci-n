x=xlsread('Mediciones.xlsx',2,'A5:A28');
y=xlsread('Mediciones.xlsx',2,'B5:B28');
z=log10(x);
ap1= -16.226*z-58.894;
ap2= 12.19*z.^2-21.881*z-63.705;
%plot(z,y)
hold on
plot(x,y,'+')
plot(x,ap1)
plot(x,ap2)
%hold off

