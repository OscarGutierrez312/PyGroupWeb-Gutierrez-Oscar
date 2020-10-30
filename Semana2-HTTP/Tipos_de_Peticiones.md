# Tipos de peticiones HTTP

-----------------------------------------

El protocolo **HTTP** contiene un conjunto de peticiones que permiten especificar la acción que se realizará sobre un elemento determinado, clasificados en 3 Grupos:

- ***Safe***
- ***Idempotent***
- ***Cacheable***

Un método HTTP es considerado ***Safe*** o seguro si no altera el estado del servidor. Es decir, si realiza una operación de sólo lectura. Algunos de los métodos HTTP más comunes son seguros: OPTIONS, GET o HEAD. Todos los métodos seguros son también a su vez idempotent (así como también algunos, pero no todos, los métodos inseguros como DELETE o PUT).

> - **Método GET:**
El método GET significa recuperar cualquier información (en forma de una entidad), en donde se refiere a un proceso de producción de datos, son los datos producidos los que se devolverán como entidad en la respuesta donde todas las peticiones que usan el método GET, deberán recuperar únicamente datos.

> - **Método POST**
El método POST es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para algún recurso determinado. La diferencia entre PUT y POST es que PUT es idempotente, mientras que si realizamos repetidas idénticas peticiones con el método POST, podría haber efectos adicionales como pasar una orden varias ocasiones. Causando a menudo un cambio en el estado o efectos secundarios en el servidor.

> - **Método OPTIONS:**
El método OPTIONS representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de solicitud/respuesta. Éste método es el que utilizamos para describir las opciones de comunicación existentes de un recurso destino.

> - **Método HEAD:**
El método HEAD es muy similar al GET , a excepción de que el servidor responde con líneas y headers, pero no con el body de la respuesta.

> - **Método PUT:**
El método PUT es usado para solicitar que el servidor almacene el cuerpo de la entidad en una ubicación específica dada por el URL.

> - **Método DELETE**
Este método es utilizado para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL. En otras palabras más simples, este método elimina un recurso determinado.

> - **Método CONNECT**
Este método por su parte es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece en forma de un túnel.

> - **Método TRACE**
Éste método se utiliza para realizar pruebas de de retornos de mensajes en el camino que existe hacia un recurso determinado. Es un método muy utilizado para la depuración y también para el desarrollo. Además realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.

> - **Método PATCH**
El método PATCH aplica modificaciones parciales a un recurso. A diferencia de PUT, el método PATCH no es idempotente, esto quiere decir que peticiones identicas sucesivas pueden tener efectos diferentes.
