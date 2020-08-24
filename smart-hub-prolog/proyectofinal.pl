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
:- dynamic (dispositivos/3).
:- dynamic (dispositivosEncendidos/3).
:- dynamic (dispositivosApagados/3).
:- dynamic (posicionPanel/2).
:- dynamic (posiciones/2).
%CONSUMO DIARIO
:- dynamic (consumoDiario/2). %[consumo,dispositivo]
%TEMPERATURAS
:- dynamic (temperatura/2). %[consumo,dispositivo]

ventanas(ventana1, habitacion).
ventanas(ventan2, living).
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

%HECHOS DE PRUEBA
ventanas(ventana1, habitacion).
ventanas(ventan2, living).
ventanas(ventana3, terraza).
ventanas(ventana4, cocina).

dispositivos(ac_hab, habitacion, ac).
dispositivos(panel_techo1, techo, panel_solar).
dispositivos(panel_techo2, techo, panel_solar).
dispositivos(regadera_cocina, cocina, regadera).
%dispositivos(habitacion, sensorMovimiento).
%dispositivos(habitacion, sensorLuz).
%dispositivos(habitacion, sensorTemperatura).
%dispositivos(cocina, sensorHumo).

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

dispositivos(panel1, techo, panel_solar).
dispositivos(panel2, techo, panel_solar).
dispositivos(panel3, techo, panel_solar).
dispositivos(panel4, techo, panel_solar).

posiciones(north, 0).
posiciones(east, 8).
posiciones(west, 15).
posiciones(south, 20).

posicionPanel(panel1, north).
posicionPanel(panel2, north).
posicionPanel(panel3, north).
posicionPanel(panel4, north).

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

%%  si todos salen true se reutilizarían las reglas de durmiendo
%%  porque es un evento parecido.

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

nukeAll:- retractall(puertas(_,_,_)),retractall(puertasAbiertas(_,_,_)),retractall(puertasCerradas(_,_,_)),retractall(ventanas(_,_)),retractall(ventanasAbiertas(_,_)),retractall(ventanasCerradas(_,_)),retractall(dispositivos(_,_,_)),retractall(dispositivosEncendidos(_,_,_)),retractall(dispositivosApagados(_,_,_)),retractall(posicionPanel(_,_)),retractall(posiciones(_,_)),retractall(consumoDiario(_,_)),retractall(temperaturas(_,_)).