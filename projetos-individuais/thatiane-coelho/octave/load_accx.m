## Copyright (C) 2022 Thatiane
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {} {@var{retval} =} load_accx (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Thatiane <Thatiane@DESKTOP-C903G91>
## Created: 2022-07-20

function importarAceleracao()
  global aceleracao
  ## [file,dir] = uigetfile('.txt','Importar Acc X');
  ## Arquivo = [dir,file];
  Arquivo = 'C:\Users\Thatiane\Desktop\sensorial piloto\dados\Alexandre .txt'
  aceleracao = dlmread(Arquivo, ';');
  aceleracao

