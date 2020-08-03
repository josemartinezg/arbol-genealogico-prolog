:- dynamic (sensor/7).
%sensor(Nombre,Estado,Ubicaci�n,Par�metro_Deseado_Min,Par�metro_Deseado_max,ValorActual,Condici�n)
% activo = 1, inactivo = 0

%Sensor de Temperatura
%Par�metros en grados celcius, ValorActual = Temp. exterior
%Condici�n: aire, calefaccion, ambiente.
sensor(temperatura,1,habitacion_1,29,60,25,ambiente).

%Regla para ajustar sensores existentes
ajustar(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion,ValorActual):-
    call(sensor(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion)),
    retract(sensor(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion)),
    write('Estado(1/0): '),
    read(Nuevo_Estado),
    write('Valor M�nimo: '),
    read(Min),
    write('Valor M�ximo: '),
    read(Max),
    write('Condicion: '),
    read(Nueva_Condicion),
    asserta(sensor(Sensor,Nuevo_Estado,Ubicacion,Min,Max,ValorActual,Nueva_Condicion)).

%Regla para registrar nuevos sensores
% agregar_sensor(Nombre,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_max,ValorActual,Condicion).
%

