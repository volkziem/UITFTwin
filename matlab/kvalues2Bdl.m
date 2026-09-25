% kvalues2Brho.m, V. Ziemann, 260914
clear all
mc2=0.511;  % electron restmass in MeV
model='uitf.lattice';
k=strfind(model,'.');
filnam=strcat(model(1:k-1),'_Bdl.lattice');
[beamline,names]=read_lattice_file(model);
[bpmpos,corloc,quadloc,solloc,loc2seg,seg2loc]=find_bpm(beamline);
state0=[0;0;0;0];
[Racc,spos,nmat,nlines,state,gammaE]=calcmat(beamline,state0);


for line=1:nlines
  gamma0=gammaE(loc2seg(line));
  Brho=1e6*sqrt(gamma0^2-1)*mc2/300; % microTesla-meter
  switch beamline(line,1)
    case {5, 19}    % quadrupole
      beamline(line,4)=beamline(line,4)*beamline(line,3)*Brho;
    case 7    % corrector
      %disp([line,gamma0,Brho])
      beamline(line,5:6)=Brho*beamline(line,5:6)*1e-3;
  end
end

save_lattice_file

