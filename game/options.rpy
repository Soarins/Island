﻿## Этот файл содержит некоторые опции которые можно изменить для настройки
## вашей игры на Ren'Py. Он содержит только самые часто используемые настройки...
## Их на самом деле гораздо больше.
##
## Строки, начинающиеся с двух знаков '#' являются комментариями, и вы
## не должны их раскомментировать. Строки, начинающиеся с одного
## знака '#' являются закоментированным кодом, и вы можете их
## раскомментировать в подходящих вам ситуациях.

init -1 python hide:

    ## Включать ли нам инструменты разработчика? Здесь нужно
    ## поставить False перед выпуском игры, чтобы
    ## пользователь не смог мошенничать, используя эти инструменты.
    config.mouse = { 'default' : [ ('image_install/Cursor.png', 0, 0)] }
    
    config.developer = True
    
    # Эта запускает активацию автосохранения
    
    config.has_autosave = True
    
    ## Эти управляют шириной и высотой экрана.

    config.screen_width = 1280
    config.screen_height = 720

    ## Это управляет заголовком окна, когда Ren'Py
    ## запущен в оконном режиме.

    config.window_title = u"Island"

    # Эти управляют именем и версией игры, которые указываются
    # в журналах отладки.
    config.name = "Island"
    config.version = "1.0"

    #########################################
    # Темы

    ## Затем, мы захотим вызвать функцию темы. theme.roundrect
    ## это тема, поддерживающая круглые прямоугольники.
    ##
    ## Функция темы берет несколько параметров, которые
    ## настраивают цветовую схему.

    theme.threeD(
        ## Theme: 3D
        ## Color scheme: Colorblind

        ## The color of an idle widget face.
        widget = "#898989",

        ## The color of a focused widget face.
        widget_hover = "#464646",

        ## The color of the text in a widget.
        widget_text = "#CCCCCC",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#F2F2F2",

        ## The color of a disabled widget face.
        disabled = "#898989",

        ## The color of disabled widget text.
        disabled_text = "#666666",

        ## The color of informational labels.
        label = "#c2c2c2",

        ## The color of a frame containing widgets.
        frame = "#252525",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#393939",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#393939",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,
        

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )

        
        
    #########################################
    ## Эти настройки позволяют вам настроить окно,
    ## содержащее диалоги и текст "от автора", замещая его
    ## изображением.

    ## Фон окна. В Frame, числа символизируют размер
    ## левого/правого и верхнего/нижнего бордюров
    ## соответственно.
 
    # style.window.background = Frame("frame.png", 12, 12)

    ## Внешние поля - пространство, окружающее окно, на котором
    ## не рисуется фон.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Внутренние поля - пространство внутри окна, где
    ## рисуется фон.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Это минимальная высота окна, включая поля.

    # style.window.yminimum = 250


    #########################################
    ## Это позволит вам изменить расположение главного меню.

    ## Это работает так: мы находим точку-якорь внутри
    ## объекта и точку позиции (pos) на экране.
    ## Затем, мы размещаем объект так, чтобы эти точки совпадали.

    ## Якорь/pos можно задавать как целое или действительное число.
    ## Если целое, оно принимается как кол-во пикселей от
    ## левого верхнего угла. Если действительное, число
    ## принимается как доля размера объекта или экрана.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Это позволяет настроить шрифт текста в Ren'Py.

    ## Файл, содержащий шрифт.

    # style.default.font = "DejaVuSans.ttf"

    ## Размер текста по умолчанию.

    # style.default.size = 22

    ## Заметьте, что это изменит стиль лишь некоторого
    ## текста. У других кнопок свои стили.


    #########################################
    ## Эти настройки позволят изменить некоторые звуки
    ## Ren'Py.

    ## Установите False если в игре нет звуковых эффектов.

    config.has_sound = True

    ## Установите False если в игре нет музыки.

    config.has_music = True

    ## Установите True если в игре есть озвучка.

    config.has_voice = False

    ## Звуки при нажатии на кнопки и imagemap-ы.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки при входе и выходе из игрового меню.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук для проверки громкости.

    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.

    config.main_menu_music = "music/Tenmon.mp3"


    #########################################
    ## Справка.

    ## Это позволит настроить опцию справки в меню Ren'Py.
    ## Это могут быть:
    ## - Метка в сценарии. В этом случае эта метка вызывается
    ##   для показа помощи.
    ## - Имя файла отнсоительно основной директории.
    ##   Он будет открыт в веб-браузере.
    ## None. Помощь будет выключена.
    config.help = "README.html"


    #########################################
    ## Переходы.

    ## Используется при входе в игровое меню.
    config.enter_transition = None

    ## Используется при выходе из игрвого меню.
    config.exit_transition = None

    ## Используется между экранами игрового меню.
    config.intra_transition = None

    ## Используется при входе в игровое меню из главного.
    config.main_game_transition = None

    ## Используется при возвращении в главное меню из игры.
    config.game_main_transition = None

    ## Используется при переходе в главное меню из окна загрузки.
    config.end_splash_transition = None

    ## Используется при переходе в главное меню после окончания игры.
    config.end_game_transition = None

    ## Используется при загрузке игры.
    config.after_load_transition = None

    ## Используется при отображении окна.
    config.window_show_transition = None

    ## Используется при скрытии окна.
    config.window_hide_transition = None

    ## Используется при переходе в режим NVL сразу после режима ADV.
    config.adv_nvl_transition = dissolve

    ## Используется при переходе в режим ADV сразу после режима NVL.
    config.nvl_adv_transition = dissolve

    ## Используется при отображении yesno.
    config.enter_yesno_transition = None

    ## Используется при скрытии yesno.
    config.exit_yesno_transition = None

    ## Используется при входе в реплей.
    config.enter_replay_transition = None

    ## Используется при выходе из реплея.
    config.exit_replay_transition = None

    ## Используется при изменении изображения с помощью "say" с изобразительными атрибутами.
    config.say_attribute_transition = None

    #########################################
    ## Имя директории, где хранятся данные игры.
    ## (это необходимо задать рано, чтобы постоянная информация могла быть
    ## найдена на стадии инициализации.)
python early:
    config.save_directory = "Island-1420937576"

init -1 python hide:
    #########################################
    ## Стандартные значения настроек.

    ## Эти опции используются лишь при первом запуске игры.
    ## Чтобы применить их снова, удалите game/saves/persistent.

    ## Запустить в полноэкранном режиме?

    config.default_fullscreen = False

    ## Скорость текста по умолчанию, в знаках в секунду. 0 - бесконечность.

    config.default_text_cps = 0
    
    ## Время авто-режима по умолчанию.

    config.default_afm_time = 10

    #########################################
    ## Остальные настройки могут быть ниже.
    
    config.window_icon = "image_install/logo.png" #yourgameicon.png = твоя иконка.
    build.classify('game/**', 'archive')

## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Island-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Island"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    build.classify('**/.**', None) 
    build.classify('**/#**', None) 
    build.classify('**/thumbs.db', None) 
    build.documentation('*.html') 
    build.documentation('*.txt') 
    build.archive("scripts", "all") 
    build.archive("images", "all") 
    build.classify("game/**.rpy", "scripts") 
    build.classify("game/**.rpyc", "scripts") 
    build.classify('game/**.png', 'archive') 
    build.classify('game/**.jpg', 'archive')
    