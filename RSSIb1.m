beacon1=xlsread('Mediciones.xlsx',2);
x=xlsread('Mediciones.xlsx',2,'A4:A10');
y=xlsread('Mediciones.xlsx',2,'B4:B10');
p=polyfit(x,log10(y),1);
fprintf('exponente a= %2.3f\n',p(1));
fprintf('coeficiente c = %3.3f\n',exp(p(2)));
hold on
plot(x,y,'ro','markersize',4,'markerfacecolor','r')
z=@(x) exp(p(2))*exp(x*p(1));
fplot(z,[x(1),x(end)])
xlabel('x')
ylabel('y')
grid on
title('Regresión exponencial')
plot(x,-35*log10(x)-65,'-')
hold off