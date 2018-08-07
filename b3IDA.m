x=xlsread('Mediciones.xlsx',4,'A5:A44');
y=xlsread('Mediciones.xlsx',4,'B5:B44');
z=log10(x);
%plot(z,y)
ap1=-25.858*z-55.941;
hold on
plot(x,y)
plot(x,ap1)
hold off