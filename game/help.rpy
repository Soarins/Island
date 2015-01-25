screen help: 
    #С помощью этих двух функций мы меняем фон, add можно не использовать 
    tag menu 
    add "gfx/fon.jpeg" 
    frame:  
        #Создаем площадь где будет находиться текст, два последних параметра это ширина и высота. 
        area (0,0,1280,720)  
        #Делаем вертикальную полосу прокрутки 
        viewport mousewheel True scrollbars "vertical": 
            has vbox 
            text "Краткая информация об игре:"  
            #С помощью этой функции мы опускаем следующий текст на 15 пикселей. 
            null height 15 
            text "Эта игра посвящена знаменитому аниме To Love Ru. В ней вы можете изменить судьбу нашего развратника Юки Рито)" 
    #Здесь создается ссылка на главное меню 
    frame: 
        style_group "mm" 
        xalign .98 
        yalign .98 

        has vbox 

        textbutton "Главное меню" action ShowMenu("main_menu") 