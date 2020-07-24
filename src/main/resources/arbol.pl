hombre(orlando).
hombre(alfonso).
hombre(luis).
hombre(carlos).
hombre(pedro).
mujer(maria).
mujer(karla).
mujer(lola).
mujer(julia).
progenitor(orlando,maria).
progenitor(orlando,pedro).
progenitor(karla,maria).
progenitor(maria,luis).
progenitor(maria,lola).
progenitor(alfonso,lola).
progenitor(pedro,carlos).
progenitor(julia,carlos).

hermanos(X,Y):- progenitor(Z,X),progenitor(Z,Y), X\==Y.
abuelo(Abuelo,Nieto):- progenitor(Padre,Nieto),progenitor(Abuelo,Padre).
tio(X,Y):- progenitor(Z,Y),hermanos(Z,X).
primo(X,Y):- progenitor(Z,Y),progenitor(W,X),hermanos(Z,W).
pareja(X,Y):- progenitor(X,H),progenitor(Y,H),X\==Y,not(hermanos(X,Y)).
suegro(S,Y):- progenitor(S,H),pareja(Y,H),hombre(S).
cunado(X,Y):- (pareja(X,Z),hermanos(Z,Y));(pareja(Y,P),hermanos(P,X)).


