ST2Plugin
=========

Agregar el Plugin y su configuracion el el teclado es :

{ "keys": ["ctrl+shift+b"], "command": "open_browser","args": {"block":true,"url_basepath":"http://urlbase/"}}

url_basepath : contiene la ruta base de tu web de desarrollo, usualmente seria [http://localhost/]

pronto mejorare el plugin por ahora solo le puse algunas cosas que necesito yo para crear webs en codeigniter.


DETALLES:
=========

Cuando se posiciona sobre el archivo routes.php : 

$route["seleccionaresto"] = 'controllerclass/function';

al precionar comand: ctrl+b se va al navegador con la url basepath+"seleccionaresto"

si te colocas bajo un archivo diferente y seleccionas algo como :

miarchivo.css

te abrira el archivo : CSSPATH + miarchivo.css , en caso de no existir crea una ventana con el archivo en la ruta y basta con darle guardar y se guarda en CSSPATH, igualmente con un JS 

por ultimo si es un texto con formato : miarchivo.php (mayormente vistas), te abre el buscador de archivos con el texto para abrir el archivo especifico.

me gustaria crear un enlace como el buscador de sublime para hacer click y enlazar directamente una funcion a sus llamados pero esto de las api de sublime son algo reciente en mi lista de cosas por aprender. 

