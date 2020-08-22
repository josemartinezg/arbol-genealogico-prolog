

%-------------------------------------------------------------------
%lo que he hecho:
%Punto 3: Monitoreo

%Lista de lugares *solo el lugar: [habitacion_1,habitacion2]
:- dynamic (lugares/1).

%Lista de puertas *Nombre, Lugar, Tipo: [ (puerta_1,habitacion_1,Inte) ]
:- dynamic (puertas/3).
:- dynamic (puertasAbiertas/3).
:- dynamic (puertasCerradas/3).
%Lista de ventanas *Nombre y lugar: [ (puerta_1,habitacion_1)]
:- dynamic (ventanas/2).
:- dynamic (ventanasAbiertas/2).
:- dynamic (ventanasCerradas/2).
%Lista de luces
:- dynamic (luces/2).
:- dynamic (lucesEncendidas/2).
:- dynamic (lucesApagadas/2).

% DISPOSITIVOS *Nombre, lugar:
%[ (aire_acondicionado, habitacion_1) ]
:- dynamic (dispositivos/3).
:- dynamic (dispositivosEncendidos/2).
:- dynamic (dispositivosApagados/2).
%CONSUMO DIARIO
:- dynamic (consumoDiario/2). %[consumo,dispositivo]

%Lista de sensores



% Protocolos: bloqueo y cierre de entradas principales y ventanas del
% hogar, analizando sus estados y modificándolos de acuerdo a
% evaluaciones de eventos específicos que ocurran y que considere puedan
% representar problemas de seguridad para sus habitantes.

%PUERTAS

agregar_puerta(Nombre,Lugar,Tipo):- assertz(puertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).

remover_puerta(Nombre,Lugar,Tipo):-retract(puertas(Nombre,Lugar,Tipo)).

abrir_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasCerradas(Nombre,Lugar,Tipo)),assertz(puertasAbiertas(Nombre,Lugar,Tipo)).
cerrar_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasAbiertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).


%VENTANAS

agregar_ventana(Nombre,Lugar):- assertz(ventanas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

remover_ventana(Nombre,Lugar):-retract(ventanas(Nombre,Lugar)).

abrir_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),retract(ventanasCerradas(Nombre,Lugar)),assertz(ventanasAbiertas(Nombre,Lugar)).
cerrar_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),retract(ventanasAbiertas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

% LUCES

agregar_luz(Nombre,Lugar):- assertz(luces(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

remover_luz(Nombre,Lugar):-retract(luces(Nombre,Lugar)).

encender_luz(Nombre,Lugar):-luces(Nombre,Lugar),retract(lucesApagadas(Nombre,Lugar)),assertz(lucesEncendidas(Nombre,Lugar)).
apagar_luz(Nombre,Lugar):-luces(Nombre,Lugar),retract(lucesEncendidas(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

% DISPOSITIVOS
agregar_dispositivo(Nombre,Lugar):- assertz(dispositivos(Nombre,Lugar)),assertz(dispositivosApagados(Nombre,Lugar)).

remover_dispositivo(Nombre,Lugar):-retract(dispositivos(Nombre,Lugar)),retract(dispositivosApagados(Nombre,Lugar)).

abrir_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasCerradas(Nombre,Lugar,Tipo)),assertz(puertasAbiertas(Nombre,Lugar,Tipo)).
cerrar_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasAbiertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).

%CONSUMO DIARIO
agregar_consumo(Dispositivo,Consumo):-dispositivos(Dispositivo,_),assertz(consumoDiario(Dispositivo,Consumo)).
remover_consumo(Dispositivo):-dispositivos(Dispositivo,_),retract(consumoDiario(Dispositivo,_)).
mostrar_consumos:-listing(consumoDiario).

%EVENTOS:
% DORMIR

durmiendoVentanas:- ventanasAbiertas(Nombre,Lugar),assertz(ventanasCerradas(Nombre,Lugar)),retract(ventanasAbiertas(Nombre,Lugar)).

durmiendoPuertas:-  puertasAbiertas(Nombre,Lugar,exterior),assertz(puertasCerradas(Nombre,Lugar,exterior)),retract(puertasAbiertas(Nombre,Lugar,exterior)).


% ESTADO:

estado:- write('¿Qué desea ver?:'),nl,
	 write('(puertas, ventanas, luces, dispositivos, consumos diarios, o todo)'),nl,
	 read(Opcion),
	 pseudoIf(Opcion).

pseudoIf(puertas):-write('Puertas Abiertas:'),
	           listing(puertasAbiertas),
	           write('Puertas Cerradas:'),
	           listing(puertasCerradas).
pseudoIf(ventanas):-write('Ventanas Abiertas:'),
	           listing(ventanasAbiertas),
	           write('Ventanas Cerradas:'),
	           listing(ventanasCerradas).
pseudoIf(luces):-  write('Luces encendidas:'),
	           listing(lucesEncendidas),
	           write('Luces apagadas:'),
	           listing(lucesApagadas).
pseudoIf(dispositivos):-write('Dispositivos encendidos:'),
	           listing(dispositivosEncendidos),
	           write('Dispositivos apagados:'),
	           listing(dispositivosApagados).
pseudoIf(consumos):-write('Consumos diarios:'),nl,
	            listing(consumoDiario).
pseudoIf(todo):- write('Puertas Abiertas:'),
	           listing(puertasAbiertas),
	           write('Puertas Cerradas:'),
	           listing(puertasCerradas),
                   write('Ventanas Abiertas:'),
	           listing(ventanasAbiertas),
	           write('Ventanas Cerradas:'),
	           listing(ventanasCerradas),
		   write('Luces encendidas:'),
	           listing(lucesEncendidas),
	           write('Luces apagadas:'),
	           listing(lucesApagadas),
		   write('Dispositivos encendidos:'),
	           listing(dispositivosEncendidos),
	           write('Dispositivos apagados:'),
	           listing(dispositivosApagados).








%			 write("Ventanas Abiertas:"),
%	 listing(ventanasAbiertas),
%	 write("Ventanas Cerradas:"),
%	 listing(ventanasCerradas.
