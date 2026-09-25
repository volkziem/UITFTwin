% myUpdateFcn.m
function txt = myUpdateFcn(~, event_obj)
  global spos names seg2loc
  ax = gca;
  coordinates = ax.CurrentPoint;
  x_coord = coordinates(1,1);
  y_coord = coordinates(1,2);
  [val,idy]=min(abs(x_coord-spos));
  idx=seg2loc(idy);
  if idx>0 && ~ismissing(names(idx))
    txt=sprintf('idx=%d, val=%9.3f, spos=%9.3f: %s\n',idx,val,spos(idx),names(idx)); 
    fprintf(txt)
  end
end