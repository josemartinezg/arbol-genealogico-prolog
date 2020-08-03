progenitor(antonio,carlos).
progenitor(antonio,eva).
progenitor(maria,carlos).
progenitor(maria,eva).

progenitor(elena,fernando).
progenitor(elena,silvia).
progenitor(carlos,fernando).
progenitor(carlos,silvia).

progenitor(eva,emilio).
progenitor(david,emilio).



%reglas--------------------------------------------
abuelo(Abuelo,Nieto):-progenitor(Padre,Nieto),progenitor(Abuelo,Padre).

hermano(Hijo1,Hijo2):- progenitor(Padre,Hijo1), progenitor(Padre,Hijo2),Hijo1 \= Hijo2.
%Ejemplo: carlos y eva

pareja(X,Y):- progenitor(X,Hijo),progenitor(Y,Hijo),X\=Y.

tio(Tio,Sobrino):- progenitor(Padre,Sobrino),hermano(Tio,Padre).

primo(Primo1,Primo2):- progenitor(X,Primo2),tio(X,Primo1),Primo2\=Primo1.

suegro(Suegro,Yerno):- progenitor(Suegro,Pareja),pareja(Yerno,Pareja).
%Ejemplo: elena tiene como suegros a antonio y maria.
cunado(X,Y):- hermano(Z,Y),pareja(X,Z).
%Ejemplo: eva tiene  como cuñada a elena



