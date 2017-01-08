function[]=writeABQsolidsection(filepath,composite,elset,material,refnode,orientation,controls,...
                                layup,order,stackdirection,symmetric,data)
%%
%==============================================================================
% Copyright (c) 2016 Universit� de Lorraine & Lule� tekniska universitet
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
% Neither the name of the Universit� de Lorraine or Lule� tekniska universitet
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

line = strcat('*SOLID SECTION');

if ~strcmp(composite,'none') && ~strcmp(composite,'NONE') && ~strcmp(composite,'None')
    line = strcat(line,', ',composite);
end

if ~strcmp(elset,'none') && ~strcmp(elset,'NONE') && ~strcmp(elset,'None')
    line = strcat(line,', ',elset);
end

if ~strcmp(material,'none') && ~strcmp(material,'NONE') && ~strcmp(material,'None')
    line = strcat(line,', ',material);
end

if ~strcmp(refnode,'none') && ~strcmp(refnode,'NONE') && ~strcmp(refnode,'None')
    line = strcat(line,', ',refnode);
end

if ~strcmp(orientation,'none') && ~strcmp(orientation,'NONE') && ~strcmp(orientation,'None')
    line = strcat(line,', ',orientation);
end

if ~strcmp(controls,'none') && ~strcmp(controls,'NONE') && ~strcmp(controls,'None')
    line = strcat(line,', ',controls);
end

if ~strcmp(layup,'none') && ~strcmp(layup,'NONE') && ~strcmp(layup,'None')
    line = strcat(line,', ',layup);
end

if ~strcmp(order,'none') && ~strcmp(order,'NONE') && ~strcmp(order,'None')
    line = strcat(line,', ',order);
end

if ~strcmp(stackdirection,'none') && ~strcmp(stackdirection,'NONE') && ~strcmp(stackdirection,'None')
    line = strcat(line,', ',stackdirection);
end

if ~strcmp(symmetric,'none') && ~strcmp(symmetric,'NONE') && ~strcmp(symmetric,'None')
    line = strcat(line,', ',symmetric);
end

fprintf(fileId,strcat(line,'\n'));

for i=1:length(data)
    fprintf(fileId,strcat(' ',data{i},'\n'));
end

fprintf(fileId,'**\n');

fclose(fileId);

return