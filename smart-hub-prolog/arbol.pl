persona(francisca).
persona(santiago).
persona(jaquelyn).
persona(ines).
persona(rosa).
persona(julian).
persona(amelia).
persona(ivan).
persona(ivanosevic).
persona(ivania).
persona(isaias).
persona(josemaria).
persona(joseph).

progenitor(francisca, jaquelyn).
progenitor(santiago, jaquelyn).
progenitor(francisca, ines).
progenitor(santiago, ines).
progenitor(francisca, rosa).
progenitor(santiago, rosa).
progenitor(julian, ivan).
progenitor(amelia, ivan).
progenitor(jaquelyn, ivanosevic).
progenitor(ivan, ivanosevic).
progenitor(jaquelyn, ivania).
progenitor(ivan, ivania).
progenitor(rosa, isaias).
progenitor(ines, josemaria).
progenitor(joseph, josemaria).


hermano(X,Y):-progenitor(Pariente,X),progenitor(Pariente,Y), X \= Y.

tio(Tio,Sobrino):-progenitor(Padre,Sobrino),hermano(Padre,Tio).

primo(X,Y):-progenitor(A,Y),tio(A,X),progenitor(B,X),tio(B,Y).

pareja(X,Y):-progenitor(X,Hijo),progenitor(Y,Hijo), X \= Y.

suegro(Suegro,Yerno):-progenitor(Suegro,Hijo),pareja(Hijo,Yerno).

cunado(X,Y):-pareja(X,A),hermano(A,Y).
cunado(X,Y):-pareja(Y,A),hermano(A,X).

