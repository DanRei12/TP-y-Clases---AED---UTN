import PySimpleGUI as psg
psg.popup ("Hola nuevo usuario, ¿Cómo estas?")
username = psg.popup_get_text("Ingresa tu nombre de usuario aquí, por favor", "Nombre del loquito")
age = int(psg.popup_get_text("Ingresa tu edad aquí, por favor", "Edad del loquito"))
age = str(age)
country = psg.popup_get_text("Ingresa tu país aquí, por favor", "País del loquito")
team = psg.popup_get_text("Ingresa el equipo del que eres hincha, por favor", "Team del loquito")
insulto = psg.popup_get_text("Ingresa el mejor insulto que te sepas, por favor", "Insulto del loquito")
pelfav = psg.popup_get_text("Ingresa tu pelicula favorita, por favor", "Pelicula del loquito")

psg.popup_scrolled ("Datos del loquito identificados", "...", "Te damos la bienvenida..." + username, \
                    "Edad: " + age, "País: " + country, "Equipo Favorito: " + team, "Pelicula favorita: " + pelfav, "En resumen, " + insulto + ", " + username + ".")
