% drawmag.m, draw magnet lattice
function drawmag(beamline,vpos,height);
legend('AutoUpdate','off');
hold on
nlines=size(beamline,1);
nmat=sum(beamline(:,2))+1;
spos=zeros(nmat,1);
ic=1;
for line=1:nlines 
  for seg=1:beamline(line,2)
    ic=ic+1;    
    switch beamline(line,1)
        case 2  % thin quad
            dv=0.15*height*sign(beamline(line,4));
            rectangle('Position',[spos(ic-1),vpos+dv,0.1,height])
        case {4 44}  % bend
            L=beamline(line,3);
            rectangle('Position', ...
                [spos(ic-1),vpos+0.25*height,L,0.5*height],'FaceColor','k')
        case 5  % quad
            L=beamline(line,3);
            dv=0.15*height*sign(beamline(line,4));
            rectangle('Position',[spos(ic-1),vpos+dv,L,height],  ...
              'FaceColor','b')
        case 7   % corrector
            a=0.05;
            s=spos(ic-1);
            pgon=polyshape(s+a*[-0.5,0,0.5],vpos+height*[1.3,-0.7,1.3]);
            plot(pgon,'FaceColor','green');
        case 19  % solenoid
            L=beamline(line,3);
            dv=0.15*height*sign(beamline(line,4));
            rectangle('Position',[spos(ic-1),vpos+dv,L,2*height], ...
              'FaceColor','r')
        case 30  % V-WIEN
            L=beamline(line,3);
            dv=0.1*height;
            rectangle('Position',[spos(ic-1),vpos-dv,L,8*dv], ...
              'FaceColor','c')
        case 31  % H-WIEN
            L=beamline(line,3);
            dv=0.1*height;
            rectangle('Position',[spos(ic-1),vpos+3*dv,L,8*dv], ...
              'FaceColor','c')
        case 50   % RFCAV
           L=beamline(line,3);
           dv=0.4*height;
           rectangle('Position',[spos(ic-1),vpos-2*dv,L,6*dv], ...
              'FaceColor','c')
        case 52
           L=beamline(line,3);
           dv=0.4*height;
           draw_ellipse(spos(ic-1)+0.5*L,vpos+dv,L,6*dv);
        case 103  % BPM 
           a=0.2;
           s=spos(ic-1);
           plot(s+[-0.04,0.04],vpos+height*[1,1],'r','LineWidth',2)
           plot(s+[0.0,0.0],vpos+height*[1,3],'r','LineWidth',1)
           plot(s+[-0.04,0.04],vpos-height*0.5*[1,1],'r','LineWidth',2) 
           plot(s+[0.0,0.0],vpos-0.5*height*[1,4],'r','LineWidth',1)
        case 110   % SCREEN
           s=spos(ic-1)-0.03;
           plot([s,s],[vpos-1.7*height,vpos+1.7*height],'m','LineWidth',3)
    end
    spos(ic)=spos(ic-1)+beamline(line,3);
  end
end
plot([spos(1),spos(end)],[vpos+0.5*height,vpos+0.5*height],'k:')