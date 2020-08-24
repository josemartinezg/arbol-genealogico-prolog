

%-------------------------------------------------------------------
%lo que he hecho:
%Punto 3: Monitoreo

%Lista de lugares *solo el lugar: [habitacion_1,habitacion2]
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
:- dynamic (dispositivos/2).
:- dynamic (dispositivosEncendidos/2).
:- dynamic (dispositivosApagados/2).
%CONSUMO DIARIO
:- dynamic (consumoDiario/2). %[consumo,dispositivo]
%TEMPERATURAS
:- dynamic (temperatura/2). %[consumo,dispositivo]

ventanas(habitacion).
ventanas(living).
ventanas(terraza).
ventanas(cocina).

dispositivos(habitacion, sensorMovimiento).
dispositivos(habitacion, sensorLuz).
dispositivos(habitacion, sensorTemperatura).
dispositivos(cocina, sensorHumo).

habitaciones(cocina).
habitaciones(habitacion).
habitaciones(living).
habitaciones(terraza).

luces(luz_1, cocina).
luces(luz_2, habitacion).
luces(luz_3, living).
luces(luz_4, terraza).

puertas(puerta1, cocina, interior).
puertas(puerta2, habitacion, interior).
puertas(puerta3, terraza, exterior).
puertas(puerta4, living, exterior).
%HECHOS DE PRUEBA
ventanas(ventana1, habitacion).
ventanas(ventana2, living).
ventanas(ventana3, terraza).
ventanas(ventana4, cocina).

dispositivos(habitacion, sensorMovimiento).
dispositivos(habitacion, sensorLuz).
dispositivos(habitacion, sensorTemperatura).
dispositivos(cocina, sensorHumo).

lugares(cocina,5).
lugares(habitacion,2).
lugares(living,8).
lugares(terraza,10).

luces(luz_1, cocina).
luces(luz_2, habitacion).
luces(luz_3, living).
luces(luz_4, terraza).

puertas(puerta1, cocina, interior).
puertas(puerta2, habitacion, interior).
puertas(puerta3, terraza, exterior).
puertas(puerta4, living, exterior).


% Protocolos: bloqueo y cierre de entradas principales y ventanas del
% hogar, analizando sus estados y modificándolos de acuerdo a
% evaluaciones de eventos específicos que ocurran y que considere puedan
% representar problemas de seguridad para sus habitantes.

%LUGARES
agregar_lugar(Nombre):- assertz(habitaciones(Nombre,0)).
remover_lugar(Nombre):- retract(habitaciones(Nombre,_)).

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

encender_dispositivo(Nombre,Lugar):-dispositivos(Nombre,Lugar),retract(dispositivosApagados(Nombre,Lugar)),assertz(dispositivosEncendidos(Nombre,Lugar)).
apagar_dispositivo(Nombre,Lugar):-dispositivos(Nombre,Lugar),retract(dispositivosEncendidos(Nombre,Lugar)),assertz(dispositivosApagados(Nombre,Lugar)).
%CONSUMO DIARIOventana
agregar_consumo(Dispositivo,Consumo):-dispositivos(Dispositivo,_),assertz(consumoDiario(Dispositivo,Consumo)).
remover_consumo(Dispositivo):-dispositivos(Dispositivo,_),retract(consumoDiario(Dispositivo,_)).
mostrar_consumos:-listing(consumoDiario).


% SENSOR MOVIMIENTO

actualizarCantidad(Nombre,Cantidad):-retract(lugares(Nombre,_)),assertz(lugares(Nombre,Cantidad)).

% SENSOR TEMPERATURA

%EN PROGRESO temperatura(Grados,Lugar):-



% EVENTOS:

% DORMIR

durmiendoVentanas:- ventanasAbiertas(Nombre,Lugar),retract(ventanasAbiertas(Nombre,Lugar)),assertz(ventanasCerradas(Nombre,Lugar)).

durmiendoPuertas:-  puertasAbiertas(Nombre,Lugar,exterior),retract(puertasAbiertas(Nombre,Lugar,exterior)),assertz(puertasCerradas(Nombre,Lugar,exterior)).

durmiendoLuces:- lucesEncendidas(Nombre,Lugar),retract(lucesEncendidas(Nombre,Lugar)),assertz(lucesApagadas(Nombre,Lugar)).

% SALIR

%%	si todos salen true se reutilizarían las reglas de durmiendo
%%	porque es un evento parecido.
salir(Lugar):-lugares(Lugar,Cantidad), Cantidad = 0.

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



