:- dynamic (sensor/7).
%sensor(Nombre,Estado,Ubicación,Parámetro_Deseado_Min,Parámetro_Deseado_max,ValorActual,Condición)
% activo = 1, inactivo = 0

%Sensor de Temperatura
%Parámetros en grados celcius, ValorActual = Temp. exterior
%Condición: aire, calefaccion, ambiente.
sensor(temperatura,1,habitacion_1,29,60,25,ambiente).

%Regla para ajustar sensores existentes
ajustar(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion,ValorActual):-
    call(sensor(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion)),
    retract(sensor(Sensor,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_Max,ValorAnterior,Condicion)),
    write('Estado(1/0): '),
    read(Nuevo_Estado),
    write('Valor Mínimo: '),
    read(Min),
    write('Valor Máximo: '),
    read(Max),
    write('Condicion: '),
    read(Nueva_Condicion),
    asserta(sensor(Sensor,Nuevo_Estado,Ubicacion,Min,Max,ValorActual,Nueva_Condicion)).

%Regla para registrar nuevos sensores
% agregar_sensor(Nombre,Estado,Ubicacion,Parametro_Deseado_Min,Parametro_Deseado_max,ValorActual,Condicion).
%

