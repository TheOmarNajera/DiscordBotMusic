# DiscordBotMusic
Bot de discord para reproducir musica con youtube.

## Instrucciones de uso
El prefijo para utilizar todos los comandos es: _**!**_

### play
Este comando hace que el bot se una al canal de voz donde se encuentre el autor que invocó el comando, y el  bot reproduce la canción especificada.
>Internamente, el programa descarga el vídeo, lo transforma a un nuevo archivo **song.mp3**, y elimina los archivos originalmente descargados.

Para poder utilizar el comando, el usuario puede escribir la url de la canción a reproducir, o bien, el nombre de la canción, y esta traerá el primer resultado de Youtube.
Ejemplo:

```
!play https://www.youtube.com/watch?v=GP5qFx2yAtU&ab_channel=TheMusicLifeOfMichaelJackson
!play The Jackson Five
```
!Solo se puede reproducir una canción. Para poder reproducir otra canción, el usuario debe esperar a que termine la canción actual, o poner el comando *>stop* para parar y ahora poner el comando *>play [link]* para reproducir la canción deseada.
### pause
Este comando pausa la canción que el bot está actualmente reproduciendo, dejándolo en espera.
```
!pause
```
### resume
Este comando sirve para continuar reproduciendo la canción que fue pausada con anterioridad.
```
!resume
```
### stop
Este comando sirve para parar por completo la canción, haciendo incapaz de continuar reproduciendo, dando opción de reproducir otra canción que el usuario desee.
```
!stop
```
### leave
Este comando sirve para desconectar al bot del canal de voz. Si había una canción reproduciendo, ésta se elimina.
```
!leave
```
### info
Este comando muestra la información del servidor donde se encuentra el bot.
```
!info
```