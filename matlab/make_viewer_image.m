% make_viewer_images.m, V. Ziemann, 260817
iviewer=ifind('ITV',names);
figure(3); clf
[XX,YY]=meshgrid(-10:0.1:10,-10:0.1:10); 
sigma_viewer=zeros(2,2,4);
for k=1:4
  iseg=loc2seg(iviewer(k));
  x0=state(1,iseg); y0=state(3,iseg);
  %x0=0; y0=0;
  R=Racc(:,:,iseg);
  beam=R*sigmabeam0*R';
  sig=1e6*[beam(1,1),beam(1,3);beam(1,3),beam(3,3)];
  siginv=inv(sig);
  psi=@(x,y)exp(-0.5*(siginv(1,1).*(x-x0).^2+2*siginv(1,2).*(x-x0).*(y-y0) ...
                   +siginv(2,2).*(y-y0).^2))./(2*pi*sqrt(det(sig)));
  ZZ=psi(XX,YY);
  ZZ=flipud(ZZ);  
  subplot(2,2,k); 
  colormap default; c='y';
  %colormap(flipud(gray)); c='b';
  %surfc(XX,YY,ZZ); xlabel('x [mm]'); ylabel('y [mm]'); view(2)
  imagesc(ZZ); axis equal
  if k==imsav 
    if exist('tmp/') ~= 7, mkdir('tmp'); end
    tim=char(datetime('now', 'Format', '_HHmmss'));
    txt=sprintf('tmp/%s%s',names(iviewer(k)),tim);
    exportgraphics(gca, strcat(txt,'.png')); 
  end
  title(names(iviewer(k)))
  text(10,10,['\sigma_x = ',num2str(sqrt(sig(1,1)),'%6.2f'),' mm'],'Color',c)
  text(10,20,['\sigma_y = ',num2str(sqrt(sig(2,2)),'%6.2f'),' mm'],'Color',c)
  text(100,10,['\sigma_{13} = ',num2str(sig(1,2),'%6.2f'),' mm^2'],'Color',c)
  text(10,190,['x_0 = ',num2str(x0,'%6.1f'),' mm        ', ...
               'y_0 = ',num2str(y0,'%6.1f'),' mm'],'Color',c)
  axis equal
  if k==imsav, imsav=-1; exportgraphics(gca, strcat(txt,'a.png')); end 
  %sigma_viewer(:,:,k)=sig;  % remember
  %ff=@(x,y)x.*y.*psi(x,y); s13=integral2(ff,-20,20,-20,20,'AbsTol',1e-8)
end
return

x0=state(1,iseg); y0=state(3,iseg);
R=Racc(:,:,iseg);
beam=R*sigmabeam0*R';
sig=1e6*[beam(1,1),beam(1,3);beam(1,3),beam(3,3)]
siginv=inv(sig);

psi=@(x,y)exp(-0.5*(siginv(1,1).*(x-x0).^2-2*siginv(1,2).*(x-x0).*(y-y0) ...
                   +siginv(2,2).*(y-y0).^2))./(2*pi*sqrt(det(sig)));

[XX,YY]=meshgrid(-5:0.1:5,-5:0.1:5); ZZ=psi(XX,YY);

subplot(2,2,1); contour(XX,YY,ZZ); xlabel('x [mm]'); ylabel('y [mm]')
subplot(2,2,2); surfc(XX,YY,ZZ); xlabel('x [mm]'); ylabel('y [mm]'); view(2)
subplot(2,2,3); plot(-5:0.1:5,sum(ZZ,1),'b'); xlabel('x [mm]')
subplot(2,2,4); plot(-5:0.1:5,sum(ZZ,2),'r'); xlabel('y [mm]')