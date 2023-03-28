while True:
    path1 = ["D:\\music\\music3\\朱彦安,张诗莉 - 柳叶笺.mp3",
             "D:\\music\\music3\\Sawako碎花 - 帝国少女（Cover 初音ミク）.mp3",
             "D:\\music\\music3\\Hozier - Take Me To Church.mp3",
             "D:\\music\\music3\\Reyanna Maria,Tyga - So Pretty.mp3",
             "D:\\music\\music3\\Adam Christopher - So Far Away (Acoustic).mp3",
             "D:\\music\\music3\\Imagine Dragons - Demons.mp3",
             "D:\\music\\music3\\ROSÉ - On The Ground.mp3",
             "D:\\music\\music3\\sapientdream - Promise.mp3",
             "D:\\music\\music3\\SLANDER,Dylan Matthew - Love Is Gone (Acoustic).mp3",
             "D:\\music\\music3\\The Chainsmokers,Coldplay - Something Just Like This.mp3"]
    path2 = ["[柳叶笺]",
             "[帝国少女]",
             "[Take Me To Church]",
             "[So Pretty]",
             "[So Far Away]",
             "[Demons]",
             "[On The Ground]",
             "[Promise]",
             "[Love Is Gone]",
             "[Something Just Like This]"]
    import random

    i = random.randint(0, 9)
    print(path2[i], '\n')

    import pygame

    pygame.mixer.init()
    pygame.mixer.music.load(path1[i])
    pygame.mixer.music.set_volume(0.5)  # 声音大小[0<j<1]  J = float(input("调节音量：J="))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # time.sleep(5)
        # pygame.mixer.music.stop()
        pass

