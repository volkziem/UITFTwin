function myMouseClickCallback(src, event)
    global spos names seg2loc
    % 1. Get the current axis inside the figure
    ax = gca;
    
    % 2. Extract the data coordinates relative to the plot axes
    coordinates = ax.CurrentPoint;
    x_coord = coordinates(1,1);
    y_coord = coordinates(1,2);
    
    % 3. Check which mouse button was pressed
    % 'normal' = Left click, 'alt' = Right click, 'extend' = Middle click
    clickType = src.SelectionType;
    
    % Display the results in the command window
    
    
    [val,idy]=min(abs(x_coord-spos));
    idx=seg2loc(idy);
    if idx>0 && ~ismissing(names(idx))
      txt=sprintf('idx=%d, val=%9.3f, spos=%9.3f: %s',idx,val,spos(idx),names(idx)); 
   %  msgbox(txt)
      fprintf('X: %.2f, Y: %.2f %s\n', x_coord, y_coord, names(idx));
    end
end
