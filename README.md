2.1 --> Diagrama
Diagrama anexo
Diagrama2 anexo

Agroso Modo incluyo informacion inetresante para entender el diagranma de aplicacion.
Por ejemplo, Acerca del diagrama de componentes de la aplicacion
En la estructura general de la aplicación, esta incluye tanto el frontend como el backend, y cómo se relacionan entre sí. 
Explicación detallada de cada parte:

Frontend:
Cliente Web: Representa la interfaz de usuario con la que interactúan los usuarios finales.
Componentes React: Los diferentes componentes de la interfaz de usuario, como formularios, listas, etc.
Servicios API: Módulos que manejan las llamadas a la API del backend.


Backend:
API FastAPI: El punto de entrada principal para las solicitudes del frontend.
Rutas: Define los endpoints de la API.
Servicios: Contiene la lógica de negocio principal.
Modelos: Define la estructura de los datos y la interacción con la base de datos.
Utilidades: Funciones auxiliares, como validaciones.

Base de Datos:
PostgreSQL: La base de datos relacional utilizada para almacenar los datos de la aplicación.

Contenedores Docker:
Contenedor Frontend: Aloja la aplicación React.
Contenedor Backend: Aloja la API FastAPI.
Contenedor DB: Aloja la base de datos PostgreSQL.


Ahora para>
- Las flechas sólidas representan las interacciones directas entre componentes, 
- Las flechas punteadas muestran las relaciones de despliegue en los contenedores Docker.
Este diagrama proporciona una visión general de cómo los diferentes componentes de la aplicación se relacionan entre sí y cómo están organizados. 
Es útil para entender la arquitectura general del sistema y sieve de punto de referencia para el desarrollo en diferentes partes de la aplicación.


2.2 -->  ¿Qué mecanismos de seguridad incluirías en la aplicación para garantizar la protección del acceso a los datos?
Podemos considerar los siguientes:
- Autenticación y Autorización
Implementar JWT (JSON Web Tokens) para la autenticación de usuarios.
Utilizar OAuth 2.0 para la autorización, especialmente si se integran servicios de terceros.

- Encriptación de Datos
Utilizar HTTPS/TLS para todas las comunicaciones entre el cliente y el servidor.
Encriptar datos sensibles en la base de datos (como contraseñas) utilizando algoritmos fuertes como bcrypt.

 Gestión de Sesiones
Implementar timeouts de sesión para cerrar sesiones inactivas automáticamente y Utilizar tokens de sesión seguros y rotarlos periódicamente.

- Validación y Sanitización de Entradas
Implementar validación de entradas tanto en el frontend como en el backend.

-Control de Acceso
Utilizar listas de control de acceso (ACL) para gestionar permisos granulares.

-Protección contra Ataques Comunes
Implementar rate limiting para prevenir ataques de fuerza bruta.
Configurar encabezados de seguridad HTTP como Content Security Policy (CSP), X-XSS-Protection, etc.


-Logging y Monitoreo
Implementar logging extensivo de todas las actividades de seguridad relevantes y Utilizar herramientas de monitoreo en tiempo real para detectar eventos sospechosos.,
Implementar un sistema de alerta para notificar sobre posibles brechas de seguridad.

- Seguridad en la Infraestructura
Configurar firewalls para restringir el acceso no autorizado.
Implementar una red privada virtual (VPN) para acceso remoto seguro.

-Políticas de Seguridad y Cumplimiento
Implementar políticas de contraseñas fuertes.

- Backup y Recuperación
Implementar un sistema robusto de backup y recuperación de datos y que estos esten encriptados y protegidos.

2.3. ¿Qué estrategia de escalabilidad recomendarías para la aplicación considerando que el crecimiento proyectado será de 1,000,000 de clientes por año?

Despliegue de la aplicación en microservicios:
Separar la lógica de clientes, servicios y facturación en servicios independientes.
Implementar un servicio de autenticación y autorización centralizado.

Actualizar la infraestructura:
Migrar de Docker Compose a Kubernetes para orquestación de contenedores.
Configurar auto-scaling en Kubernetes basado en métricas de uso.

Optimizar la base de datos:
Implementar sharding en PostgreSQL o considerar una base de datos distribuida como CockroachDB.
Agregar una capa de cache con Redis.


Implementar procesamiento asíncrono
Agregar RabbitMQ o Kafka para manejar tareas en segundo plano.

Mejorar el monitoreo:
Implementar Prometheus y Grafana para monitoreo y visualización.


Optimizar el frontend:
Implementar code splitting y lazy loading en React.


Agregar un API Gateway:
Implementar servcios de API Gateway.


3. Redes
3.1. Explica la diferencia entre un router y un switch. ¿Cuándo usarías cada uno?

Router y switch son dispositivos fundamentales en  nuestras redes tegnologicas, pero tener presente que tienen funciones y usos distintos:
Router:
Función: Enrutamiento de paquetes entre redes diferentes. Los routers examinan la dirección IP de destino de cada paquete y lo envían por la ruta más adecuada para llegar a su destino.
Uso delos Routers:
Conexión entre redes: Se utilizan para conectar redes locales (LAN) entre sí o para conectar una LAN a Internet.
Enrutamiento dinámico: Pueden aprender automáticamente las rutas más eficientes para enviar paquetes.
Subnetting: Dividen las redes en subredes más pequeñas para una mejor gestión y control.

Switch:
Función: Conexión de dispositivos dentro de una misma red. Los switches identifican la dirección MAC de cada dispositivo conectado 
y envían los paquetes directamente al dispositivo de destino, sin necesidad de analizar la dirección IP.
En cuanto a su Uso: 
Conexión de dispositivos en una LAN: Se utilizan para conectar computadoras, servidores, impresoras y otros dispositivos dentro de una misma red.
Creación de redes segmentadas: Pueden dividir una red en segmentos más pequeños para mejorar el rendimiento y la seguridad.

En resumen podemos decir que:
Router:
Cuando necesitas conectar diferentes redes (por ejemplo, tu red doméstica con Internet).
Cuando necesitas dividir una red en subredes.
Cuando necesitas enrutamiento dinámico.
Switch:
Cuando necesitas conectar dispositivos dentro de una misma red.
Cuando necesitas crear redes segmentadas.

Importante:
>>Los routers se encargan de dirigir el tráfico entre diferentes redes
>>Mientras que los switches se encargan de conectar dispositivos dentro de una misma red.

3.2. Describe las siete capas del modelo OSI y menciona brevemente la función principal de cada una
El modelo OSI (Open Systems Interconnection) es una referencia estándar para la comunicación de datos en redes. 
Divide la comunicación en siete capas, cada una con una función específica:
Capa Física: Se encarga de la transmisión de bits a través del medio físico (cables, fibra óptica, etc.). Define las características eléctricas y mecánicas de la conexión.
Capa de Enlace de Datos: Se ocupa de la transmisión de datos entre dispositivos en la misma red local. Define protocolos como Ethernet para la detección y corrección de errores.
Capa de Red: Encarga de la dirección y enrutamiento de paquetes entre redes diferentes. Utiliza protocolos como IP para asignar direcciones únicas a cada dispositivo en una red.
Capa de Transporte: Garantiza la entrega fiable de datos entre aplicaciones en hosts diferentes. Define protocolos como TCP y UDP para la conexión y el control de errores.
Capa de Sesión: Establece, mantiene y termina las conexiones entre aplicaciones. Se encarga de la sincronización y el control de flujo de datos.
Capa de Presentación: Se encarga de la sintaxis y semántica de los datos, como la codificación, la compresión y la encriptación.
Capa de Aplicación: Es la capa más cercana al usuario y proporciona servicios de red a las aplicaciones, como HTTP, FTP, SMTP, etc.
En resumen: Cada capa del modelo OSI se encarga de una función específica y trabaja en conjunto con las otras capas para garantizar la comunicación efectiva entre dispositivos en una red.


3.3. Explica las diferencias entre los protocolos TCP y UDP. Dar un ejemplo de cuándo usarías cada uno?
-- TCP (Transmission Control Protocol): Este esta orientado a la conexión: TCP establece una conexión entre el cliente y el servidor antes de que ocurra la transferencia de datos.
Fiabilidad: TCP garantiza que todos los paquetes de datos enviados llegarán al destino en el orden correcto. Utiliza mecanismos como la confirmación de recepción de paquetes (ACK) 
y retransmisiones para asegurarse de que los datos se entregan correctamente.
Control de flujo y congestión: TCP ajusta dinámicamente la velocidad de envío de datos para evitar la congestión en la red.
TCP es ideal para aplicaciones que requieren una entrega de datos fiable y ordenada, como la navegación web (HTTP/HTTPS), la transferencia de archivos (FTP), y el correo electrónico (SMTP).

-- UDP (User Datagram Protocol):
Caracteristicas importantes:
No establece la conexion, osea "Sin conexión": UDP no establece una conexión previa antes de enviar datos. 
Envía paquetes (datagramas) directamente al destino sin asegurar la entrega.
No garantiza fiabilidad ni orden: UDP no proporciona mecanismos para garantizar que los paquetes lleguen a su destino o que lleguen en el orden correcto. 
Esto hace que UDP sea más rápido y con menor sobrecarga.
Sin control de flujo o congestión: UDP no ajusta la velocidad de envío de datos, lo que puede resultar en pérdida de paquetes si la red está congestionada.
Como ejemplos:
UDP es ideal para aplicaciones que requieren velocidad y pueden tolerar alguna pérdida de datos, como el streaming de video en tiempo real (YouTube, Netflix), juegos en línea, y transmisión de voz (VoIP).

3.4. ¿Qué es una máscara de subred y cómo se utiliza para dividir una red en subredes más pequeñas?

Una máscara de subred es un número binario que se utiliza para dividir una red IP en subredes más pequeñas.
Esta máscara define qué parte de una dirección IP corresponde a la dirección de red y qué parte corresponde a la dirección del host.

Para emplearla para dividir una red. La máscara de subred se representa como una secuencia de unos y ceros, o en notación decimal con puntos. Por ejemplo, 255.255.255.0.
División de bits: Los unos en la máscara indican la parte de la dirección IP que pertenece a la red, mientras que los ceros indican la parte que pertenece al host.
Número de subredes y hosts: El número de unos y ceros en la máscara determina el número de subredes y el número de hosts posibles en cada subred.
Clase de red: La clase de red (A, B o C) influye en la máscara de subred predeterminada.
Por Ejemplo: Si tenemos la dirección IP 192.168.1.100 y la máscara de subred 255.255.255.0, la red a la que pertenece es 192.168.1.0 y la parte de host es 100.

Por qué dividir una red en subredes?
Mejor organización: Facilita la administración de una red grande.
Seguridad: Permite aislar diferentes segmentos de la red.
Eficiencia: Reduce el tráfico de broadcast y mejora el rendimiento.


3.5. ¿Puedes mencionar algunos protocolos de enrutamiento dinámico y explicar brevemente cómo funcionan?

Los protocolos de enrutamiento dinámico permiten que los routers intercambien información de forma automática y calculen las mejores rutas para enviar paquetes. 
Algunos de los más comunes son:

RIP (Routing Information Protocol):Uno de los protocolos más antiguos y sencillos. Utiliza un algoritmo de vector distancia para calcular las rutas.
Tiene una complejidad limitada y una métrica basada en el número de saltos.

OSPF (Open Shortest Path First): Protocolo de estado de enlace que calcula las rutas más cortas basadas en un costo.
Utiliza un algoritmo de Dijkstra para calcular las rutas. Ofrece mayor escalabilidad y estabilidad que RIP.

EIGRP (Enhanced Interior Gateway Routing Protocol): Desarrollado por Cisco, combina características de RIP y OSPF. Utiliza un algoritmo híbrido para calcular las rutas.
Ofrece un equilibrio entre rendimiento y complejidad.

BGP (Border Gateway Protocol): Protocolo de enrutamiento exterior utilizado para conectar diferentes sistemas autónomos (AS). Se basa en el concepto de política y permite un control más granular sobre el enrutamiento.
Personalmente es uno de los que mas he trabajado y me gustan mas.

Cómo funcionan estos protocolos?
Estos protocolos utilizan diferentes algoritmos para calcular las mejores rutas, pero en general siguen estos pasos:
Intercambio de información por ejemplo los routers intercambian información sobre sus redes conectadas y las rutas hacia otros destinos.
Cálculo de rutas: Cada router utiliza un algoritmo para calcular la ruta más corta o de menor costo hacia cada destino.
Actualización de tablas de enrutamiento: Las tablas de enrutamiento de cada router se actualizan con las nuevas rutas calculadas.
Convergencia: El proceso de actualización de las tablas de enrutamiento continúa hasta que todos los routers tienen una vista consistente de la topología de la red.
En resumen: Los protocolos de enrutamiento dinámico permiten que las redes se adapten a los cambios de forma automática, lo que mejora la fiabilidad y la eficiencia.

4. Gestion de Proyectos

4.1. ¿En qué grupos de procesos de dirección de proyectos es creado un presupuesto detallado del proyecto?
El presupuesto detallado del proyecto es creado en el grupo de procesos de Planificación.
Se desarrolla durante el proceso de "Determinar el presupuesto", que forma parte de la planificación de la gestión de los costos.


4.2. ¿En qué grupo de procesos de la dirección de proyectos es creada el acta de constitución del proyecto?
El acta de constitución del proyecto es creada en el grupo de procesos de Inicio. 
Este documento autoriza formalmente el proyecto y proporciona al gerente del proyecto la autoridad para utilizar los recursos de la organización para las actividades que se definan del proyecto.

4.3. El equipo de proyecto acaba de completar el primer cronograma y presupuesto del proyecto. La próxima cosa a hacer es:
Después de completar el primer cronograma y presupuesto del proyecto, la próxima cosa a hacer es obtener la aprobación del cronograma y presupuesto por parte de los interesados clave y el patrocinador del proyecto. 
Tener presente que es muy importante y Esto es crucial para asegurar que todos los stakeholders estén alineados con los objetivos del proyecto y los recursos asignados.

4.4. Un primer cronograma del proyecto puede ser creado solamente después de crear:
Un primer cronograma del proyecto puede ser creado solamente después de crear el WBS (Work Breakdown Structure) o EDT (Estructura de Desglose del Trabajo). 
El WBS es esencial para identificar y definir todos los entregables y actividades del proyecto, que luego se organizan en un cronograma.

4.5. Una persona que debe estar al mando durante la planificación de la gestión del proyecto es:
La persona que debe estar al mando durante la planificación de la gestión del proyecto es el gerente de proyecto.
El gerente de proyecto es responsable de la planificación, ejecución y cierre del proyecto, así como de la coordinación y comunicación con el equipo del proyecto y los stakeholders.

4.6. ¿Cuál son las entradas del grupo de procesos de inicio de un proyecto?
Las entradas del grupo de procesos de inicio de un proyecto incluyen:

Acta de constitución del proyecto.
Documentos de negocio, como el caso de negocio (business case) y el plan de gestión de beneficios.
Factores ambientales de la empresa.
Activos de los procesos de la organización.

4.7. El patrocinador del proyecto acaba de aprobar el acta de constitución del proyecto, ¿cuál es la próxima cosa a hacer?
Después de que el patrocinador del proyecto apruebe el acta de constitución del proyecto, la próxima cosa a hacer es identificar a los stakeholders del proyecto y comenzar a desarrollar el plan de gestión del proyecto. 
Esto incluye la identificación de los interesados clave y la creación de un plan de comunicación para mantenerlos informados.

4.8. Acaban de ser establecidas las restricciones de alto nivel del cronograma del proyecto. ¿En qué grupo de procesos de dirección de proyectos se encuentra?
Las restricciones de alto nivel del cronograma del proyecto generalmente se establecen durante el grupo de procesos de Inicio. 
Estas restricciones proporcionan límites iniciales y criterios que guiarán la planificación detallada del proyecto.

4.9. ¿Qué grupos de procesos deben ser incluidos en cada proyecto?
Cada proyecto debe incluir los siguientes cinco grupos de procesos:

Inicio.
Planificación.
Ejecución.
Monitoreo y control.
Cierre.
Estos grupos de procesos cubren todas las fases de un proyecto desde su inicio hasta su cierre.

4.10. ¿Qué grupo de procesos de la dirección de proyecto necesita normalmente el mayor tiempo y número de recursos?
El grupo de procesos de la dirección de proyecto que normalmente necesita el mayor tiempo y número de recursos es el grupo de Ejecución. 
Durante la ejecución, se realizan las tareas planificadas y se utilizan recursos significativos para completar el trabajo del proyecto.



5. Caso práctico
Celsia internet en su proceso de expansión, se ha fijado como meta un crecimiento para los proximos 5 años donde se espera tener un millon de clientes. Para el que el proceso de facturación y recaudo sea efectivo,
 se requiere que el sistema de liquidación mensual de procese en los tiempos de corte establecidos de acuerdo con los ciclos de facturación definidos, 
 los servicios que han sido prestados a sus clientes y las novedades reportadas en cada periodo. Que estrategias implementaría en el desarrollo de los componentes de liquidación y facturación masiva de servicios por ciclo 
 y el recaudo de los pagos de las factura, buscando que el sistema sea robusto, escalable, resiliente, confiable y mantenible en el tiempo, ademas de la seguridad de la infomración y el tratamiento de los datos personales de los clientes.

Describa o diseñe las estrategias que incluiría para dar solución a los requerimientos solicitados en la implementación de los componentes descritos 
(Justifique la priorización de ciertos atributos sobre otros atributos de calidad en la propuesta de solución).


Para abordar el desafío de expansión de Celsia Internet y alcanzar un millón de clientes en los próximos cinco años, 
es fundamental diseñar un sistema de facturación y recaudo que sea robusto, escalable, resiliente, confiable, mantenible y seguro. Existen soluciones robustas BSS/OSS/CRM/ pero hay que saber evaluarlas de acuerdo a las necesidades y alcances


1. Arquitectura del Sistema
Estrategia: Arquitectura Basada en Microservicios

Una arquitectura de microservicios permite desarrollar, desplegar y escalar componentes individuales del sistema de manera independiente. 
Esto es crucial para manejar un crecimiento significativo en el número de clientes y asegurarse de que el sistema pueda escalar según la demanda.

Dividir el sistema en microservicios dedicados a funciones específicas, como gestión de clientes, facturación, liquidación, gestión de pagos, y notificaciones.
Utilizar contenedores (Docker) y un orquestador de contenedores (Kubernetes) para gestionar el despliegue y escalabilidad de estos microservicios.
Prioridad: Escalabilidad y Mantenibilidad. La escalabilidad permite soportar el crecimiento a un millón de clientes, mientras que la mantenibilidad facilita la actualización y mejora continua del sistema sin afectar al resto de los servicios.

2. Base de Datos Escalable y Distribuida
Estrategia: Uso de Bases de Datos Distribuidas y Multimodelo
Una base de datos distribuida y escalable es esencial para manejar grandes volúmenes de transacciones y datos en tiempo real, sin comprometer el rendimiento ni la disponibilidad.

Implementar bases de datos NoSQL (como Apache Cassandra o Amazon DynamoDB) para la gestión de grandes volúmenes de datos y bases de datos SQL para la consistencia de transacciones.
Utilizar particionamiento y replicación para distribuir los datos de manera eficiente y asegurar alta disponibilidad.
Prioridad: Escalabilidad y Confiabilidad. La base de datos debe soportar la carga creciente y ser capaz de recuperar datos de manera eficiente en caso de fallos.

3. Procesamiento Asíncrono y Colas de Mensajes
Implementación de Procesamiento Asíncrono y Colas de Mensajes
El procesamiento asíncrono y las colas de mensajes permiten que el sistema procese tareas de forma independiente y gestione mejor la carga de trabajo, reduciendo los tiempos de espera y mejorando la eficiencia.

Utilizar colas de mensajes (como RabbitMQ o Apache Kafka) para gestionar las tareas de liquidación y facturación de forma asíncrona.
Implementar procesamiento de las colas y manejen la lógica de facturación y liquidación.
Importante la Prioridad: Resiliencia y Confiabilidad. El uso de colas y procesamiento asíncrono mejora la capacidad del sistema para manejar picos de demanda y recuperarse rápidamente de fallos.

4. Seguridad de la Información y Protección de Datos Personales
Aplicación de Prácticas de Seguridad y Cumplimiento de Normativas
Proteger la información personal de los clientes es fundamental para cumplir con las normativas y mantener la confianza del cliente.
Encriptar los datos sensibles tanto en tránsito (usando TLS) como en reposo (utilizando estándares de cifrado avanzados como AES-256).
Implementar políticas estrictas de control de acceso y autenticación multifactor (MFA) para proteger el acceso a los datos y sistemas críticos.
Asegurar el cumplimiento de normativas o las leyes/Políticas aplicables sobre protección de datos.
la Prioridad: Seguridad. La protección de los datos personales es esencial para evitar brechas de seguridad y mantener la confianza del cliente.

5. Optimización del Procesamiento de Liquidación y Facturación
Estrategia: Algoritmos Eficientes y Planificación de Cargas de Trabajo
Para que el proceso de liquidación y facturación sea eficiente y cumpla con los tiempos de corte establecidos, es necesario optimizar los algoritmos de procesamiento y gestionar las cargas de trabajo.
Utilizar algoritmos de cálculo optimizados y paralelización de procesos para reducir el tiempo de procesamiento.
Implementar planificadores de tareas que ajusten dinámicamente los recursos según la carga de trabajo prevista para los ciclos de facturación.
la Prioridad: Eficiencia y Confiabilidad. Garantizar que los procesos se completen a tiempo sin errores es fundamental para la satisfacción del cliente y el cumplimiento de los requisitos del negocio.

6. Integración de Sistemas de Pago y Recaudo
Estrategia: Integración con Múltiples Proveedores de Pago y Gestión de Pagos Automatizada
Una integración flexible con múltiples proveedores de pago permite ofrecer más opciones a los clientes y mejorar la tasa de éxito de pagos.
Integrar con API de varios proveedores de pago (PayPal, Forte de CSG -la empresa donde yo trabajaba, bancos locales) para permitir múltiples métodos de pago.
Automatizar el seguimiento y la reconciliación de pagos utilizando software de gestión financiera.
la Prioridad: Flexibilidad y Automatización. Mejorar la experiencia del cliente al ofrecer múltiples opciones de pago y reducir la intervención manual en la gestión de pagos.

7. Monitoreo y Gestión de Incidencias
Estrategia: Implementación de Herramientas de Monitoreo y Alertas Proactivas
Un monitoreo constante y un sistema de alertas proactivas permiten identificar y solucionar problemas antes de que afecten a los clientes.
Implementación:
Utilizar herramientas de monitoreo (como Prometheus, Grafana, Kibana, ELK Stack) para observar métricas clave del sistema (rendimiento, errores, tiempo de respuesta).
Configurar alertas automáticas para notificar al equipo de operaciones sobre incidentes críticos.
la Prioridad: Resiliencia y Confiabilidad. Un sistema bien monitoreado puede responder rápidamente a problemas, minimizando el tiempo de inactividad y el impacto en los clientes.

8. Estrategias de Backup y Recuperación ante Desastres
Planes de Recuperación ante Desastres y Copias de Seguridad Redundantes
Se deben Tener planes de recuperación y copias de seguridad sólidas garantiza la continuidad del negocio en caso de fallos críticos o desastres naturales.
Implementar copias de seguridad automáticas y replicación de datos en diferentes zonas geográficas.
Desarrollar y probar regularmente un plan de recuperación ante desastres para asegurar la restauración rápida del sistema.
La Prioridad: Confiabilidad y Resiliencia. Mantener la disponibilidad del sistema y la integridad de los datos ante eventos inesperados es crucial para el negocio.


Conclusión
Para alcanzar un millón de clientes y mantener un sistema de facturación y recaudo eficaz, Celsia Internet debe priorizar escalabilidad, confiabilidad y seguridad al diseñar su infraestructura. 

La escalabilidad es fundamental para soportar el crecimiento, la confiabilidad asegura que los procesos críticos se completen sin errores, y la seguridad protege la información sensible de los clientes. 
Al adoptar una arquitectura moderna y utilizar tecnologías adecuadas, 
Celsia puede construir un sistema que no solo satisfaga las necesidades actuales, sino que también esté preparado para futuros desafíos. El futuro apremia y nuevos elemestos y aplicaciones saltan cada dia.
El desarrollo de la tecnologías NUNCA duerme y trayendo consigo muevos desaafios y riesgos.
