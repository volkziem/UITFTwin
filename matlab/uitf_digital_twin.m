% uitf_digital_twin.m, V. Ziemann, 260901
%
clear all;
pause(0.3);
addpath ./4D
global Racc
global spos names seg2loc
inhibit_update=0;
update_flag=1;
show_screens=1;
imsav=-1;
%model='uitf.lattice';
model='uitf_Bdl.lattice';

[inj,names]=read_lattice_file(model); % load input file
inj=misalign_magnets(inj,0.1);
beamline=inj;  
[bpmpos,corloc,quadloc,solloc,loc2seg,seg2loc]=find_bpm(beamline);
corpos=loc2seg(corloc); % with segments taken into account
nbpm=length(bpmpos); ncor=length(corloc);

ibeamx=ifind('BEAMX',names);   % get initial values from file
%linex=beamline(ibeamx,1:6), emitx=beamline(ibeamx,4)
ibeamy=ifind('BEAMY',names);
%liney=beamline(ibeamy,1:6), emity=beamline(ibeamy,4)

%return

% Measured initial values for beam
state0=[0;0;0;0];  % initial trajectory
if isempty(ibeamx)
  disp('Using hardcoded beam values')
  emitX=0.22e-6; emitY=0.23e-6; 
  betaX=0.124; alphaX=0.85; gammaX=(1+alphaX^2)/betaX;
  betaY=0.184; alphaY=0.85; gammaY=(1+alphaY^2)/betaY;
else
  disp('Using beam values from input file')
  emitX=beamline(ibeamx,4); betaX=beamline(ibeamx,5);
  alphaX=beamline(ibeamx,6); gammaX=(1+alphaX^2)/betaX;
  emitY=beamline(ibeamy,4); betaY=beamline(ibeamy,5);
  alphaY=beamline(ibeamy,6); gammaY=(1+alphaY^2)/betaY;
end
sigmaX=[betaX,-alphaX;-alphaX,gammaX]; 
sigmaY=[betaY,-alphaY;-alphaY,gammaY];
sigma0=[sigmaX, zeros(2);zeros(2),sigmaY];
sigmabeam0=[emitX*sigmaX, zeros(2);zeros(2),emitY*sigmaY];
disp(['Emittances=',num2str(emitX),', ',num2str(emitY)])

s=tcpserver(8000,'TimeOut',1e20);
configureTerminator(s,"CR/LF");

tic
while 1
  if update_flag==1 & inhibit_update==0   % visual output only if requested
    %[Racc,spos,nmat,nlines,state,gammaE]=calcmat(beamline,state0); % update optics
    [Racc,spos,nmat,nlines,state,gammaE]=calcmatBdl(beamline,state0);
    do_all_plots; 
    if show_screens > 0, make_viewer_image; else figure(3); set(gcf,'Visible','off'); end
    drawnow('update'); 
    if s.Connected
      bpmloc=ifind('IPM',names); bpos=loc2seg(bpmloc);
      s.writeline(['ALLBPM ',num2str(state(1,bpos)),' ',num2str(state(3,bpos))])
    end
  end    
  line=char(s.readline);               % read command from socket
  if strcmp(line,'quit'), clear s; break; end   % terminate at request
  token=split(line); 
  switch length(token)  % check how many arguments are provided
    case 1  % request a single value
      update_flag=0;  % no need to update if only requesting values
      if contains(line,'.XPOS?')  % check whether BPMX is requested
        k=strfind(line,'.XPOS?'); nam=line(1:k-1); 
        bpmloc=ifind(nam,names); bpos=loc2seg(bpmloc);
        s.writeline([nam,'.XPOS ',num2str(state(1,bpos))])
      elseif contains(line,'.YPOS?')  % check whether BPMY is requested
        k=strfind(line,'.YPOS?'); nam=line(1:k-1); 
        bpmloc=ifind(nam,names); bpos=loc2seg(bpmloc);
        s.writeline([nam,'.YPOS ',num2str(state(3,bpos))])
      elseif contains(line,'H.BDL?')  % check HCOR
        k=strfind(line,'H.BDL?'); nam=line(1:k-1); magpos=ifind(nam,names);
        s.writeline([nam,'H.BDL ',num2str(beamline(magpos(1),5))]);
      elseif contains(line,'V.BDL?')  % check VCOR
        k=strfind(line,'V.BDL?'); nam=line(1:k-1); magpos=ifind(nam,names);
        s.writeline([nam,'V.BDL ',num2str(beamline(magpos(1),6))]);
      elseif contains(line,'.BDL?')  % check other magnets
        k=strfind(line,'.BDL?'); nam=line(1:k-1); magpos=ifind(nam,names);
        s.writeline([nam,'.BDL ',num2str(beamline(magpos,4)')]);
        disp([num2str(toc,'%6.2f'),' get_val ',line]);
      elseif contains(token(1),[".1?",".2?",".3?",".4?",".5?",".6?"])  %
        k=strfind(line,'.'); nam=line(1:k-1); magpos=ifind(nam,names);
        ik=str2double(line(k+1:k+1));
        s.writeline([nam,'.',line(k+1:k+1),' ',num2str(beamline(magpos,ik)')]);
        %beamline(magpos,ik)=str2double(token(2)); 
      elseif contains(line,'IPM.XPOS?')   % all horizontal bpm
        bpmloc=ifind('IPM',names); bpos=loc2seg(bpmloc);
        s.writeline([nam,'.XPOS ',num2str(state(1,bpos))])
      elseif contains(line,'IPM.YPOS?')   % all horizontal bpm
        bpmloc=ifind('IPM',names); bpos=loc2seg(bpmloc);
        s.writeline([nam,'.YPOS ',num2str(state(3,bpos))]) 
      elseif contains(char(token(1)),'.SIGMAS?') 
         k=strfind(line,'.SIGMAS'); nam=line(1:k-1); 
         magpos=ifind(nam,names); iseg=loc2seg(magpos(1));
         R=Racc(:,:,iseg); beam=1e6*R*sigmabeam0*R';
         s.writeline([strcat(nam,'.SIGMAS'),' ',num2str(sqrt(beam(1,1))),' ',  ...
                      num2str(sqrt(beam(3,3))),' ',num2str(beam(1,3))]);  
      else 
        disp(['***Error1, not found: ',line]);
        s.writeline(['***Error1, not found: ',line]);
      end 
    case 2  % set a value, name+value provided
      update_flag=1;
      if contains(char(token(1)),'H.BDL')  % set HCOR
        k=strfind(line,'H.BDL'); nam=line(1:k-1); magpos=ifind(nam,names);
        beamline(magpos,5)=str2double(token(2));
      elseif contains(char(token(1)),'V.BDL')  % set VCOR
        k=strfind(line,'V.BDL'); nam=line(1:k-1); magpos=ifind(nam,names);
        beamline(magpos,6)=str2double(token(2));
      elseif contains(char(token(1)),'.BDL')  % set other magnet
        k=strfind(line,'.BDL'); nam=line(1:k-1); magpos=ifind(nam,names);
        if length(magpos)>1
          for k=1:length(magpos)
            v=beamline(magpos(k),4);
            beamline(magpos(k),4)=sign(v)*abs(str2double(token(2)));
            %disp([names(magpos(k)),' = ',num2str(beamline(magpos(k),4))])
          end
        else
          beamline(magpos,4)=str2double(token(2));
        end
      elseif contains(token(1),[".1",".2",".3",".4",".5",".6"])  %
        k=strfind(line,'.'); nam=line(1:k(1)-1); magpos=ifind(nam,names);
        ik=str2double(line(k(1)+1:k(1)+1));
        beamline(magpos,ik)=str2double(token(2));
      elseif contains(char(token(1)),'MISALIGN')  % set other magnet
        beamline=misalign_magnets(beamline,str2double(token(2)));
      elseif contains(char(token(1)),'INHIBIT')
        inhibit_update=0;
        if str2double(token(2)) >0.1, inhibit_update=1; end
      elseif contains(char(token(1)),'CORLIST')
        fp=fopen('corlist.txt','w');
        fprintf(fp,'%s\n',names(corloc(1:ncor)));
        fclose(fp); update_flag=0;
      elseif contains(char(token(1)),'BPMLIST')
        fp=fopen('bpmlist.txt','w');
        fprintf(fp,'%s\n',names(seg2loc(bpmpos(1:nbpm))));
        fclose(fp); update_flag=0;
      elseif contains(char(token(1)),'ORM')
        orm=zeros(2*nbpm,2*ncor);
        for ic=1:ncor
          for ib=1:nbpm
            R=TM(corpos(ic),bpmpos(ib));
            orm(ib,ic)=R(1,2);
            orm(ib,ncor+ic)=R(1,4);
            orm(nbpm+ib,ncor+ic)=R(3,4);
            orm(nbpm+ib,ic)=R(3,2);
          end
        end
        dlmwrite('response_matrix.txt',orm); update_flag=0;
      elseif contains(char(token(1)),'SHOW_SCREENS')
        show_screens=0;
        if str2double(token(2)) > 1e-6, show_screens=1; end
      elseif contains(char(token(1)),'RESET')
        [beamline,names]=read_lattice_file(model);
      elseif contains(char(token(1)),'SCREEN')
        imsav=-1;
        name=char(token(2));
        iviewer=ifind(name,names);
        if iviewer>0   % only do if screen is found
          iseg=loc2seg(iviewer(1));
          R=Racc(:,:,iseg);
          beam=1e6*R*sigmabeam0*R';
          s.writeline(['SIGMAS ',num2str(sqrt(beam(1,1))),' ', ...
            num2str(sqrt(beam(3,3))),' ',num2str(beam(1,3))])
          itmp=ifind('ITV',names); imsav=find(itmp(1)==iviewer);
          %imsav=find(ifind('ITV',names)==iviewer);
        else
          disp('**Error: device not found');
        end
      elseif contains(char(token(1)),'TM.FROM')
        update_flag=0;
        iseg1=loc2seg(ifind(char(token(2)),names));
        if isempty(iseg1), disp(['***Error  TM.FROM: ',char(token(2)),' not found']); continue; end
      elseif contains(char(token(1)),'TM.TO') 
        update_flag=0;
        iseg2=loc2seg(ifind(char(token(2)),names));
        if isempty(iseg2), disp('***Error  TM.TO not found'); continue; end
        tm=TM(iseg1,iseg2(1));
        outstr='TM';
        for k1=1:4, for k2=1:4 
          tmpstr=strcat(" ",num2str(tm(k1,k2),'%9.4f'));
          outstr=strcat(outstr,tmpstr); 
        end; end
        s.writeline(outstr)   
      elseif contains(char(token(1)),'SAVE')
        filnam=char(token(2));
        save_lattice_file;
      else
        disp(['***Error2, not found: ',line]);
        s.writeline(['***Error2, not found: ',line]);
      end
      disp([num2str(toc,'%6.2f'),' set_val ',line]);
    case {3,4}            % debug interface
      update_flag=1;
      debug_interface;    % pick or set value in beamline with @? or @ 
    otherwise
      disp(['***Error3, too many arguments: ',line]);
      s.writeline(['***Error3, too many arguments: ',line']);
  end  % of switch nt
end  % of while 1
clear s