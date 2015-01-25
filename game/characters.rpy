init:


    #первый персонаж
    image nop = Solid("#00000000") # пустой прозрачный фон
    image glaz:
        "image_sprite/glaz.png" # закрытые глаза
        0.1
        "nop" # пусто - т.е. видно картинку с открытыми глазами
        3.0
        "image_sprite/glaz.png" # закрытые глаза
        0.1
        "nop" # пусто - т.е. видно картинку с открытыми глазами
        1.0
        "image_sprite/glaz.png" # закрытые глаза
        0.1
        "nop" # пусто - т.е. видно картинку с открытыми глазами
        3.0
        "image_sprite/glaz.png" # закрытые глаза
        0.1
        "nop" # пусто - т.е. видно картинку с открытыми глазами
        4.0
        "image_sprite/glaz.png" # закрытые глаза
        0.1
        "nop" # пусто - т.е. видно картинку с открытыми глазами
        3.0
        repeat
    image rot:
        "image_sprite/rot.png" # закрытый рот
        0.25
        "nop"
        0.05
        "image_sprite/rot.png"
        0.20
        "nop"
        0.15
        repeat
    # собираем девочку, глаза и рот в кучку
    image girl talk = LiveComposite((400, 720),
        (0, 0), "image_sprite/girl.png",
        (90, 210), "glaz",
        (120, 280), "rot")
    # просто моргает. молча
    image girl blink = LiveComposite((400, 720),
        (0, 0), "image_sprite/girl.png",
        (90, 210), "glaz")
        
        
        