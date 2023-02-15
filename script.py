# CONFIGURAR GIT CON GITHUB POR PRIMERA VEZ
# En la terminal: git config --global user.name "Hugo Avsquez" / git config --global user.email "hugoabrahamv19@gamil.com"

# Cuando doy git init script.py cambia a color verde y aparece un U (untracked file, archivo NO versionado) al frente del archivo
# (ls -la) = a usar (ll),  me sirve pra ver los archivos ocultos de git, los accesos o permisos que tiene la carpeta donde escribi git init
# Cuando el archivo pasa de verde U a amarillo M significa que aunque ya hice el primer commit, algo he modificado y no lo he agragado aun, el ultimo paso seria que el archivo pase a A en color blanco, significa que todo ha sido agregado
# pwd ,En la terminal me muestra donde estoy parado
# git branch -m main ,Para cambiar el nombre de master a main
# git add script.py ,Agrega el el codigo al estado staging (recuerda que hay 3 estados = working directory, ejecuto git add y paso as segundo estado, staging area, ejecuto git commit y paso a tercer estado, repository)
# git status ,Muestra que he agragado a la version que espero guardar
# git log ,Para saber si he hecho commit
# git commit -m 'titulo de commit' ,Para nombrar mis commits, puntos de recuperacion (entre 1 y 4 lineas para resumir lo que hicimos)
# git log ,Muestra como esta configurada mi maquina, Author y Date y los commit que hayan
# Puedo ver un archivo en U verde y otro en M amarillo, en ese instante puedo decidir si hago commits de ambos o solo de uno / git add archivo.py le dice al sistema que ese archivo que esta en working directory(estado 1) lo quiero mover a stagin area (estado 2)


print('Hola mundo')




