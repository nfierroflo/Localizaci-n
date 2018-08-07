y=xlsread('Mediciones.xlsx',5,'A5:A64');
x=xlsread('Mediciones.xlsx',5,'B5:B64');
d=10.^((-55.097-x)/19.933);
%plot(z,y)
%ap1=-19.933*z-55.097;
hold on
plot(x,y)
plot(x,d)
hold off
