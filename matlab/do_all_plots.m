% do_all_plots.m, V. Ziemann, 260807
fig=figure(1); clf;
subplot(10,1,[1:4])
if 0
  [spos,betax,betay]=plot_betas(beamline,sigma0);
else
  [spos,betax,betay]=plot_sigmas2(Racc,spos,sigmabeam0);
end 
title(model,'Interpreter','none')
set(gca,'FontSize',16)
fig.WindowButtonDownFcn = @myMouseClickCallback;
%fig.WindowButtonMotionFcn = @myUpdateFcn;

subplot(10,1,6)
drawmag(beamline,0,1), legend off
xlim([0, max(spos)]); axis off

subplot(10,1,[7:10])
plot(spos,state(1,:),'k',spos,state(3,:),'r-.',[0,max(spos)],[0,0],'k:','LineWidth',2);
xlim([0, max(spos)]); ylim([-5,5])
xlabel('s [m]'); ylabel('x, y [mm]')
legend('x','y')
set(gca,'FontSize',16)

figure(2); clf  % BPM display
subplot(4,1,1)
drawmag(beamline,0,1), legend off
xlim([0, max(spos)]); axis off
subplot(4,1,2)
bpmloc=find(beamline(:,1)==103); % location of BPM in beamline
bpos=loc2seg(bpmloc);
for k=1:length(bpos)
  text(spos(bpos(k))-0.06,0,names(bpmloc(k)),'Rotation',90,'Color','r'); 
end
for k=1:length(corloc)
  corpos=loc2seg(corloc);
  text(spos(corpos(k))+0.06,0.3,names(corloc(k)),'Rotation',90,'Color','#008800'); 
end
xlim([0,max(spos)]); axis off; ylim([0,2]); 
subplot(4,1,3);
bar(spos(bpmpos),state(1,bpmpos))
xlim([0, max(spos)]); ylim([-5,5])
xlabel('s [m]'); ylabel('x [mm]');
subplot(4,1,4);
bar(spos(bpmpos),state(3,bpmpos))
xlim([0, max(spos)]);  ylim([-5,5])
xlabel('s [m]'); ylabel('y [mm]');

figure(4); clf
plot(spos,0.511*gammaE,'b','LineWidth',2)
xlim([0, max(spos)]);
title(['Energy profile E_{max} = ',num2str(0.511*gammaE(end),4)])
xlabel('s [m]'); ylabel('Energy [MeV]');
set(gca,'FontSize',16)

pause(0.001);  % give time to update plots