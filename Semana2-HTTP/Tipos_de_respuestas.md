# Tipos de Respuestas en HTTP

--------------------------------------------------

En **HTTP** se definen distintos códigos numericos desde el **100** hasta el **600**, los cuales indican si una solicitud realizada se completó exitosamente. Por ello se distribuyeron estos códigos en 5 categorias:

- Respuestas Informativas
- Respuestas Exitosas
- Redirecciones
- Errores del Cliente
- Errores del Servidor

Los códigos de respuesta de estas categorias ayudan entre otras cosas a diagnosticar errores de configuración de un sitio web, por medio de un mensaje en el navegador que estemos utilizando, a continuación los códigos de respuesta mas comunes en cada una de las categorias:

## Respuestas Informativas

- **Código "100": Continue**
Este código indica que la solicitud hasta ahora realizada fue exitosa y que el servidor está listo para recibir el cuerpo de la solicitud. Esto hace que el proceso de solicitud sea más eficiente ya que evita que el navegador envíe una solicitud de cuerpo aunque los encabezados hayan sido rechazados.

- **Código "101": Switching Protocol**
Indica que se ha realizado la solicitud de cambiar de protocolo por medio de la cabecera ***upgrade*** y esta se ha realizado exitosamente por parte del servidor

## Respuestas Satisfactorias

- **Código "200": Ok**
Este código se entrega cuando una página web o recurso actúa exactamente como se espera. El significado de un éxito varía dependiendo del método HTTP.

- **Código "201": Created**
Notifica que el servidor ha cumplido con la petición de crear un nuevo recurso. Éste código es típicamente la respuesta enviada después de una petición PUT.

- **Código "202": Accepted**
Informa que el servidor ha aceptado la solicitud pero aún la está procesando. La solicitud puede, en última instancia, dar lugar o no a una respuesta completa. Está pensado para los casos en que otro proceso o servidor maneja la solicitud, o para el procesamiento por lotes.

- **Código "203": Non-Authoritative Information**
Este código significa que el servidor proxy recibió un código de estado de 200 "Ok" del servidor de origen, pero su contenido no se ha obtenido de la fuente originalmente solicitada, sino que se recoge de una copia local o de un tercero.

## Redirecciones

- **Código "302": Found**
Este código se utiliza para indicar que el recurso solicitado se encontró, pero no en el lugar donde se esperaba. Se utiliza para la redirección temporal de la URL.

- **Código "303": See Other**
El servidor envía esta respuesta para dirigir al cliente a un nuevo recurso solicitado a otra dirección usando una petición GET.

## Errores del cliente

- **Código "400": Bad Request**
Indica que el servidor el servidor no pudo interpretar la solicitud dada una sintaxis inválida.

- **Código "401": Unauthorized**
Esto es devuelto por el servidor cuando el recurso de destino carece de credenciales de autenticación válidas.

- **Código "403":Forbidden**
Este código se devuelve cuando un usuario intenta acceder a algo a que no tiene permiso para ver, por lo que el servidor está rechazando otorgar una respuesta apropiada.

- **Código "404": Not Found**
Este es uno de los códigos que con mas frecuencia aparece en los navegadores, el cual indica que el servidor no puede encontrar el recurso solicitado o que el recurso solicitado no existe, y el servidor no sabe si alguna vez existió.

- **Código "408": Request Timeout**
Esta respuesta es enviada en una conexión inactiva en algunos servidores, incluso sin alguna petición previa por el cliente. Significa que el servidor quiere desconectar esta conexión sin usar. En otras palabras, el servidor no recibió la solicitud completa que fue enviada por el navegador. Una posible causa podría ser la saturación de la red, lo que provoca la pérdida de paquetes de datos entre el navegador y el servidor.

## Errores del Servidor

- **Código "500": Internal Server Error**
Este código significa «error interno del servidor». Algo salió mal en el servidor y el recurso solicitado no fue entregado, o también que el servidor ha encontrado una situación que no sabe cómo manejarla.

- **Código "502":Bad Gateway**
Este código de error significa típicamente que un servidor ha recibido una respuesta inválida de otro, como cuando se utiliza un servidor proxy. Otras veces una consulta o petición tardará demasiado, y así es cancelada por el servidor.

- **Código "503":Service Unavailable**
Este código puede ser devuelto por un servidor sobrecargado que no puede manejar solicitudes adicionales.

- **Código "504":Gateway Timeout**
Este es el código devuelto cuando hay dos servidores involucrados en el procesamiento de una solicitud, y el primer servidor se apaga esperando que el segundo servidor responda.
