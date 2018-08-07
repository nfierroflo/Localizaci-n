x=xlsread('Mediciones.xlsx',7,'A3:A17');
y=xlsread('Mediciones.xlsx',7,'B3:B17');
z=log10(x);
plot(z,y)
%ap1=-25.858*z-55.941;
%hold on
%plot(x,y)
%plot(x,ap1)
%hold off