# COUNTRIES
* **https://restcountries.eu/**
* **https://requests.readthedocs.io/en/master/**

1. Instalar la librería requests
2. Hacer una request a la url que nos traiga todos los países del mundo
3. Crear una pequeña aplicación con las siguientes características:
	
	* Buscar país
	    * Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitirá los siguientes valores:
		name, capital, region, population, area, idioma (el primero), flag
		A su vez estos valores acturán como cabeceros
	
    * Buscar continente
	    * Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico
		EJ. dinámico --> Si se busca "africa", el archivo deberá llamarse --> africa.json
        * Además entregar la población total del continente
    
    * Paises por idioma
        * Devolver una lista con todos los paises que hablan el idioma indicado por el usuario
    
    * Descargar bandera
        * Permita al usuario descargar la bandera del país que quiera.
        * Estas imágenes serán guardadas en una carpeta aparte con el nombre del país
    
    * Historial
        * Devolvera una lista de los paises buscados de la siguiente manera:
        ```
        name: value - population: value
		```
4. Encontrar los 10 paises más grandes
5. Encontrar los 10 paises más densamente poblados
6. ¿Cuál es el idioma oficial más hablado?
