function[]=writeABQconnectordamping(filepath,component,type,dependencies,extrapolation,frequencydependence,independentcomponents,nonlinear,regularize,rtol,unsymm,data,comment)
%%
%==============================================================================
% Copyright (c) 2017 Universite de Lorraine & Lulea tekniska universitet
% Author: Luca Di Stasio <luca.distasio@gmail.com>
%                        <luca.distasio@ingpec.eu>
%
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are met:
% 
% 
% Redistributions of source code must retain the above copyright
% notice, this list of conditions and the following disclaimer.
% Redistributions in binary form must reproduce the above copyright
% notice, this list of conditions and the following disclaimer in
% the documentation and/or other materials provided with the distribution
% Neither the name of the Universite de Lorraine or Lulea tekniska universitet
% nor the names of its contributors may be used to endorse or promote products
% derived from this software without specific prior written permission.
% 
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
% ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
% LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
% CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
% SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
% INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
% CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
% ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
% POSSIBILITY OF SUCH DAMAGE.
%==============================================================================
%
%  DESCRIPTION
%  
%  A function to write  to Abaqus .inp file format.
%
%%

fileId = fopen(filepath, 'a');

fprintf(fileId,'**\n');

line = '*CONNECTOR DAMPING';

if ~strcmp(component,'none') && ~strcmp(component,'NONE') && ~strcmp(component,'None')
    line = strcat(line,', COMPONENT=',component);
end

if ~strcmp(type,'none') && ~strcmp(type,'NONE') && ~strcmp(type,'None')
    line = strcat(line,', TYPE=',type);
end

if ~strcmp(dependencies,'none') && ~strcmp(dependencies,'NONE') && ~strcmp(dependencies,'None')
    line = strcat(line,', DEPENDENCIES=',dependencies);
end

if ~strcmp(extrapolation,'none') && ~strcmp(extrapolation,'NONE') && ~strcmp(extrapolation,'None')
    line = strcat(line,', EXTRAPOLATION=',extrapolation);
end

if ~strcmp(frequencydependence,'none') && ~strcmp(frequencydependence,'NONE') && ~strcmp(frequencydependence,'None')
    line = strcat(line,', FREQUENCY DEPENDENCE=',frequencydependence);
end

if ~strcmp(independentcomponents,'none') && ~strcmp(independentcomponents,'NONE') && ~strcmp(independentcomponents,'None')
    line = strcat(line,', INDEPENDENT COMPONENTS=',independentcomponents);
end

if ~strcmp(nonlinear,'none') && ~strcmp(nonlinear,'NONE') && ~strcmp(nonlinear,'None')
    line = strcat(line,', NONLINEAR=',nonlinear);
end

if ~strcmp(regularize,'none') && ~strcmp(regularize,'NONE') && ~strcmp(regularize,'None')
    line = strcat(line,', REGULARIZE=',regularize);
end

if ~strcmp(rtol,'none') && ~strcmp(rtol,'NONE') && ~strcmp(rtol,'None')
    line = strcat(line,', RTOL=',rtol);
end

if ~strcmp(unsymm,'none') && ~strcmp(unsymm,'NONE') && ~strcmp(unsymm,'None')
    line = strcat(line,', UNSYMM=',unsymm);
end

fprintf(fileId,strcat(line,'\n'));

if ~strcmp(comment,'none') && ~strcmp(comment,'NONE') && ~strcmp(comment,'None')
    fprintf(fileId,strcat('**',comment,'\n'));
end

for i=1:length(data)
    fprintf(fileId,strcat(' ',data{i},'\n'));
end

fprintf(fileId,'**\n');

fclose(fileId);

return