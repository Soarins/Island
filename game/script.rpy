init:
    image logo = "image_install/logo.png"
    image openning = "image/openning.jpeg"
    
init python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

init python:
    import datetime
    def gett():
        h = int(datetime.datetime.now().strftime("%H"))
        res = "night" # по умолчанию ночь
        # границы любого времени суток можно поменять
        if (h > 6) and (h < 11):
            res = "morning"
        if (h >= 11) and (h <= 18):
            res = "day"
        if (h > 18) and (h < 23):
            res = "evening"
        return res

label splashscreen:
    scene black
    $ renpy.pause (2, hard=True)
    
    play sound "sound/logo.wav"fadein(2)
    
    $ renpy.pause (3, hard=True)
     
    show logo with dissolve:
        yalign .5 subpixel True 
        xalign .5 subpixel True
    $ renpy.pause (3, hard=True)
    
    scene black with dissolve
    $ renpy.pause (1, hard=True)
    
    show text "Me&You studio presents..." with dissolve
    $ renpy.pause (3, hard=True)

    hide text with dissolve
    stop sound fadeout 1.5
    return
    
label start:
    
    stop music 
    
    scene openning at Pan((0, 0), (0, 1008), (10.0)) 
    with dissolve
    $ renpy.pause (13, hard=True)
    
    # Чтобы не пряталось текстовое окно при выезде новых спрайтов
    # или смене фонов
    $ _window_during_transitions = True
    
    # после каждого меню (первым в каждой ветке варианта ответа). Выше этой точки прокатиться будет нельзя.
    # $ renpy.block_rollback()
    
    $ t = gett()
    "Now is [t]."
    
    show girl blink
    pause
    # «проверка микрофона»
    show girl talk
    play sound "music/bla.mp3"
    "Бла-бла-бла..."
    "конец"
    stop sound
    return
    