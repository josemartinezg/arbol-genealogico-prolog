:- dynamic (sensor/2).
:- dynamic (componente/3).
:- dynamic (on/1).
:- dynamic (off/1).

%sensor(Tipo,Ubicacion)
sensor(temperatura,habitacion).
sensor(fotocelda,habitacion).
sensor(movimiento,habitacion).

%componente(Tipo,Ubicacion,Sensor).
componente(climatizador_1,habitacion,temperatura).
componente(ventana_1,habitacion,movimiento).
componente(luz_1,habitacion,fotocelda).

%Registro
agregar_sensor(Sensor,Ubicacion):-
    asserta(sensor(Sensor,Ubicacion)).

agregar_componente(Componente,Ubicacion,Sensor):-
    assertz(componente(Componente,Ubicacion,Sensor)).

eliminar_sensor(Sensor,Ubicacion):-
    retract(sensor(Sensor,Ubicacion)).

eliminar_componente(Componente,Ubicacion,Sensor):-
    retract(componente(Componente,Ubicacion,Sensor)).

eliminar_sensores():-
    retractall(sensor).

eliminar_componentes():-
    retractall(componente).

%Ajuste
ajustar_temperatura(Temp_Actual,Componente,'Calefacci�n'):-
    componente(Componente,_,temperatura),
    Temp_Actual < 14.

ajustar_temperatura(Temp_Actual,Componente,'Aire Acondicionado'):-
    componente(Componente,_,temperatura),
    Temp_Actual > 27.

ajustar_temperatura(_,_,'Ambiente').


%-------------------------------------------------------------------
%lo que he hecho:

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

% Lista de dispositivos *Nombre y lugar:
%[ (aire_acondicionado, habitacion_1) ]
:- dynamic (dispositivos/2).

%Lista de sensores

%Punto 1: Seguridad


% Protocolos: bloqueo y cierre de entradas principales y ventanas del
% hogar, analizando sus estados y modific�ndolos de acuerdo a
% evaluaciones de eventos espec�ficos que ocurran y que considere puedan
% representar problemas de seguridad para sus habitantes.

%funciones puertas

agregar_puerta(Nombre,Lugar,Tipo):- assertz(puertas(Nombre,Lugar,Tipo)),assertz(puertasCerradas(Nombre,Lugar,Tipo)).

remover_puerta(Nombre,Lugar,Tipo):-retract(puertas(Nombre,Lugar,Tipo)).

abrir_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),assertz(puertasAbiertas(Nombre,Lugar,Tipo)),retract(puertasCerradas(Nombre,Lugar,Tipo)).
cerrar_puerta(Nombre,Lugar):-puertas(Nombre,Lugar,Tipo),assertz(puertasCerradas(Nombre,Lugar,Tipo)),retract(puertasAbiertas(Nombre,Lugar,Tipo)).


%funciones ventanas

add_ventana(Nombre,Lugar):- assertz(ventanas(Nombre,Lugar)),assertz(ventanasAbiertas(Nombre,Lugar)).

remove_ventana(Nombre,Lugar):-retract(ventanas(Nombre,Lugar)).

abrir_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),assertz(ventanasAbiertas(Nombre,Lugar)),retract(ventanasCerradas(Nombre,Lugar)).
cerrar_ventana(Nombre,Lugar):-ventanas(Nombre,Lugar),assertz(ventanasCerradas(Nombre,Lugar)),retract(ventanasAbiertas(Nombre,Lugar)).


%eventos:
%Dormir: que cierren todas las ventanas y puertas exteriores
% Salir: que se cierren todas las ventanas y las puertas exteriores
% tambi�n.
durmiendo:- ventanasAbiertas(Nombre,Lugar),assertz(ventanasCerradas(Nombre,Lugar)),retract(ventanasAbiertas(Nombre,Lugar)).

sleeping:- ventanasAbiertas(Nombre,Lugar),assertz(ventanasCerradas(Nombre,Lugar)),retract(ventanasAbiertas(Nombre,Lugar)),puertasAbiertas(PuertaNombre,PuertaLugar,exterior),assertz(puertasCerradas(PuertaNombre,PuertaLugar,exterior)),retract(puertasAbiertas(PuertaNombre,PuertaLugar,exterior)).
goingOut:- ventanasAbiertas(Nombre,Lugar),assertz(ventanasCerradas(Nombre,Lugar)),retract(ventanasAbiertas(Nombre,Lugar)),puertasAbiertas(PuertaNombre,PuertaLugar,exterior),assertz(puertasCerradas(PuertaNombre,PuertaLugar,exterior)),retract(puertasAbiertas(PuertaNombre,PuertaLugar,exterior)).

