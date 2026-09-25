% plot_betas2.m, display the beam sizes, V. Ziemann, 240828
function [spos,betax,betay]=plot_sigmas2(Racc,spos,sigma0)
%[Racc,spos,nmat]=calcmat(beamline);
nmat=size(Racc,3);
betax=zeros(1,nmat); betay=betax;
for k=1:length(spos)
   sigma=Racc(:,:,k)*sigma0*Racc(:,:,k)';
   betax(k)=sqrt(sigma(1,1)); 
   betay(k)=sqrt(sigma(3,3));
end
betax=1e3*betax; betay=1e3*betay;
plot(spos,betax,'k',spos,betay,'r-.','LineWidth',2); 
xlabel(' s[m]'); ylabel('\sigma_x,\sigma_y [mm]')
legend('\sigma_x','\sigma_y')
axis([0, max(spos), 0, 1.05*max([betax,betay])])
set(gca,'FontSize',14)

