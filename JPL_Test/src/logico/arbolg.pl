progenitor(diogenes,juan) .
progenitor(diogenes,bernarda) .
progenitor(juan,luis) .
progenitor(juan,maria) .
progenitor(laura,maria) .
progenitor(luis,carlos) .
progenitor(luis,laura) .
progenitor(maria,jesus) .

abuelo(Abuelo,Nieto):- progenitor(Padre,Nieto), progenitor(Abuelo,Padre).
hermano(X,Y):-progenitor(Z,X),progenitor(Z,Y) .
tio(Tio,Sobrino):-hermano(Padre,Tio),progenitor(Padre,Sobrino) .
primo(X,Y):-tio(Tio,X),tio(Tio,Y) .
pareja(X,Y):-progenitor(X,Hijo),progenitor(Y,Hijo) .
suegro(Suegro,Yerno):-progenitor(Suegro, X),pareja(Yerno, X) .
cunado(X,Y):-pareja(X,Z),hermano(Y,Z) .