 de lugares *solo el lugar: [habitacion_1,habitacion2]
:- dynamic (lugares/2).

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
:- dynamic (dispositivosEncendidos/3).
:- dynamic (dispositivosApagados/3).
:- dynamic (posicionPanel/2).
:- dynamic (posiciones/2).
%CONSUMO DIARIO
:- dynamic (consumoDiario/2). %[consumo,dispositivo]
% TEMPERATURAS
:- dynamic (temperaturas/2).

% Protocolos: bloqueo y cierre de entradas principales y ventanas del
% hogar, analizando sus estados y modificándolos de acuerdo a
% evaluaciones de eventos específicos que ocurran y que considere puedan
% representar problemas de seguridad para sus habitantes.

%LUGARES
agregar_lugar(Nombre):- assertz(lugares(Nombre,0)).
remover_lugar(Nombre):- retract(lugares(Nombre,_)).
mostar_lugares:-listing(lugares).

%PUERTAS

agregar_puerta(Nombre,Lugar,Tipo):- assertz(puertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).

remover_puerta(Nombre,Lugar,Tipo):-retract(puertas(Nombre,Lugar,Tipo)),retract(puertasCerradas(Nombre,Lugar,Tipo));retract(puertas(Nombre,Lugar,Tipo)),retract(puertasAbiertas(Nombre,Lugar,Tipo)).

abrir_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasCerradas(Nombre,Lugar,Tipo)),assertz(puertasAbiertas(Nombre,Lugar,Tipo)).
cerrar_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),retract(puertasAbiertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).


%VENTANAS

agregar_ventana(Nombre,Lugar):- assertz(ventanas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

remover_ventana(Nombre,Lugar):-retractall(ventanas(Nombre,Lugar)),retractall(ventanasCerradas(Nombre,Lugar)),retractall(ventanasAbiertas(Nombre,Lugar)).

abrir_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),retract(ventanasCerradas(Nombre,Lugar)),assertz(ventanasAbiertas(Nombre,Lugar)).
cerrar_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),retract(ventanasAbiertas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

% LUCES

agregar_luz(Nombre,Lugar):- assertz(luces(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

remover_luz(Nombre,Lugar):-retract(luces(Nombre,Lugar)).

encender_luz(Nombre,Lugar):-luces(Nombre,Lugar),retract(lucesApagadas(Nombre,Lugar)),assertz(lucesEncendidas(Nombre,Lugar)).
apagar_luz(Nombre,Lugar):-luces(Nombre,Lugar),retract(lucesEncendidas(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

% DISPOSITIVOS
agregar_dispositivo(Nombre,Lugar,Tipo):- assertz(dispositivos(Nombre,Lugar,Tipo)),assertz(dispositivosApagados(Nombre,Lugar,Tipo)).

remover_dispositivo(Nombre,Lugar):-retract(dispositivos(Nombre,Lugar,Tipo)),retract(dispositivosApagados(Nombre,Lugar,Tipo)).

encender_dispositivo(Nombre,Lugar,Tipo):-dispositivos(Nombre,Lugar,Tipo),retract(dispositivosApagados(Nombre,Lugar,Tipo)),assertz(dispositivosEncendidos(Nombre,Lugar,Tipo)).

apagar_dispositivo(Nombre,Lugar,Tipo):-dispositivos(Nombre,Lugar,Tipo),retract(dispositivosEncendidos(Nombre,Lugar,Tipo)),assertz(dispositivosApagados(Nombre,Lugar,Tipo)).

% PANELES

agregar_panel(Nombre,Lugar):- assertz(dispositivos(Nombre,Lugar,panel_solar)),assertz(dispositivosApagados(Nombre,Lugar,panel_solar)),assertz(posicionPanel(Nombre,0)).

remover_panel(Nombre,Lugar):-retract(dispositivos(Nombre,Lugar,panel_solar)), retract(dispositivosApagados(Nombre,Lugar,panel_solar)),retract(posicionPanel(Nombre,0)).

ver_paneles:-listing(dispositivos(_,_,panel_solar)).

ver_posiciones_paneles:-listing(posicionPanel).

agregar_posicion(Posicion,Hora):-assertz(posiciones(Posicion,Hora)).

remover_posicion(Posicion,Hora):-retract(posiciones(Posicion,Hora)).

ver_posiciones:-listing(posiciones).

cambiar_posicion(PosicionNueva):-posicionPanel(Panel,Posicion),retract(posicionPanel(Panel,Posicion)),assertz(posicionPanel(Panel,PosicionNueva)).

% CONSUMO DIARIO
agregar_consumo(Dispositivo,Consumo):-dispositivos(Dispositivo,_,_),assertz(consumoDiario(Dispositivo,Consumo)).

remover_consumo(Dispositivo):-dispositivos(Dispositivo,_,_),retract(consumoDiario(Dispositivo,_)).

mostrar_consumos:-listing(consumoDiario).

% TEMPERATURAS
agregar_temperatura(Lugar,Grados):-assertz(temperaturas(Lugar,Grados)).

remover_temperatura(Lugar,Grados):-retract(temperaturas(Lugar,Grados)).

mostrar_temperaturas:-listing(temperaturas).


% SENSOR MOVIMIENTO

actualizarCantidad(Nombre,Cantidad):-retract(lugares(Nombre,_)),assertz(lugares(Nombre,Cantidad)).

% SENSOR TEMPERATURA

temperatura(Grados,Lugar):-temperaturas(Lugar,SetGrados), Grados >= SetGrados,encenderRegaderas(Lugar).
temperatura(Grados,Lugar):-temperaturas(Lugar,SetGrados), Grados < SetGrados,apagarRegaderas(Lugar).



% EVENTOS:


% AIRES ACONDICIONADOS CON 0 PERSONAS

apagarAC(Lugar):- lugares(Lugar,Cantidad), Cantidad = 0,!,apagar_dispositivo(_,Lugar,aire_acondicionado).

% MOVER PANELES SOLARES

mover_paneles(Hora):- posiciones(Posicion,Hora),cambiar_posicion(Posicion).

% DORMIR

durmiendoVentanas:- ventanasAbiertas(Nombre,Lugar),retract(ventanasAbiertas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

durmiendoPuertas:-  puertasAbiertas(Nombre,Lugar,exterior),retract(puertasAbiertas(Nombre,Lugar,exterior)),assertz(puertasCerradas(Nombre,Lugar,exterior)).

durmiendoLuces:- lucesEncendidas(Nombre,Lugar),retract(lucesEncendidas(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

% SALIR

%%	si todos salen true se reutilizarían las reglas de durmiendo
%%	porque es un evento parecido.

salir(Lugar):-lugares(Lugar,Cantidad), Cantidad = 0.

% REGADERAS

encenderRegaderas(Lugar):- encender_dispositivo(_,Lugar,regadera).
apagarRegaderas(Lugar):- apagar_dispositivo(_,Lugar,regadera).



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
	           listing(dispositivosApagados),
                   write('Consumos diarios:'),nl,
	            listing(consumoDiario).
