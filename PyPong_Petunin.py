import pygame as pg
import sys
import random as r
#__________________________________________________________________________________________________________________________________________
#testBranch
<<<<<<< Updated upstream
=======
#testBranch2
#stashTest
>>>>>>> Stashed changes
def Start():
    pg.init()
    sc = pg.display.set_mode((1200, 800))
    pg.display.set_caption("PyPong v1.0")
    pg.mixer.music.load('sound/bit.ogg')
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.3)
    
    font = pg.font.SysFont("monospace", 75)
    font1 = pg.font.SysFont("monospace", 60)
    font2 = pg.font.SysFont("monospace", 40)
    font3 = pg.font.SysFont("monospace", 30)
    
    HELLO = font.render("HELLO", True,(255, 255, 255))
    WELCOME = font1.render("welcome to PyPong", True,(255, 255, 255))
    START = font3.render("(press Entert to START)",True,(255, 255, 255))
    CREATEBY = font2.render("created by SERGEI PETUNIN",True,(255, 255, 255))
    
    while 1:
        
        sc.blit(HELLO, (300,300))
        sc.blit(WELCOME, (300,400))
        sc.blit(CREATEBY, (300, 500))
        sc.blit(START, (400, 700))
        
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_RETURN:
                    Game()
                    
                elif i.key == pg.K_ESCAPE:                  
                    sys.exit()
                         
        pg.display.update()
#____________________________________________________________________________________________________________________________________________   
def Game():
    # initialize pygame
    pg.init()
    pg.display.set_caption("PyPong v1.0")
    font = pg.font.SysFont("monospace", 75)
    f1 = pg.font.Font(None, 25)
    f2 = pg.font.Font(None, 40)
    f3 = pg.font.Font(None, 30)

    #pygame.mixer.music – для добавления фоновой музыки.
    pg.mixer.music.load('sound/balalajka.ogg') #pygame.mixer.music – для добавления фоновой музыки.
    pg.mixer.music.play(-1) #функция запускает трек, - значение зацикливает, если + то еказываем количество повторов
    pg.mixer.music.set_volume(0.3)
    
    pg.mouse.set_visible(0) # невыдимая мышка на игровом поле

    # размер основного и доп.экрана
    WIN_WIDTH = 1200
    WIN_HEIGHT = 800
    SURF_WIDTH = 800
    SURF_HEIGHT = 600

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255,215,0)
    GREEN = (0,105,100)
    GREEN1 = (150,255,51)

    FPS = 60
    clock = pg.time.Clock()

    # initialize score
    player1_score = 0
    player2_score = 0
    #игра до 5 очков
    score = 5
    score = 5
    
    # draw racket
    racket_right_x = 987
    racket_right_y = 300
    racket_right_w = 20
    racket_right_h = 200
    racket_left_x = 200
    racket_left_y = 300
    racket_left_w = 20
    racket_left_h = 200

    # ball globals
    ball_x = (WIN_WIDTH / 2)
    ball_y = (WIN_HEIGHT / 2)
    ball_r = 25
    #start spdeed
    ball_xv = 0
    ball_yv = 0

    sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # левая белая поверхность,
    # равная половине окна
    surf_left = pg.Surface((SURF_WIDTH//2, SURF_HEIGHT))
    surf_left.fill(WHITE)

    # правая черная поверхность,
    # равная другой половине окна
    surf_right = pg.Surface((SURF_WIDTH//2, SURF_HEIGHT))
    surf_right.fill(BLACK)

    #Звуки
    soundHit = pg.mixer.Sound('sound/hit.ogg')
    soundGoal = pg.mixer.Sound('sound/goal.wav')
    soundLeft = pg.mixer.Sound('sound/left.wav')
    soundRight = pg.mixer.Sound('sound/right.wav')

    #Управление
    text1 = f3.render("BLACK W/S", True,(WHITE))
    text2 = f3.render("WHITE UP/DOWN", True,(WHITE))
    text3 = f3.render("ESC-выход | Музыка:1-пауза  2-продолжить | ENTER-начать подачу", True,(WHITE))
    text4 = font.render("GAME OVER",True,(WHITE))
    BLACK_WIN = f2.render("BLACK WIN",True,(WHITE))
    WHITE_WIN = f2.render("WHITE WIN",True,(WHITE))
    RESTART = f3.render("(RESTART press R)", True, (WHITE))

    #Катринка
    pic_surf = pg.image.load('pic/play.jpg')
    pic_ball = pg.image.load('pic/faceBall.png')
    #pic_surf.set_colorkey((255, 255, 255)) Если нужен прозрачный фон
    man_right = pic_surf.get_rect(bottomright=(WIN_WIDTH, WIN_HEIGHT))
    man_left = pic_surf.get_rect(bottomleft=(0,800))
#__________________________________________________________________________________________________________________________________________
#---------В цикле обрабатываем анимацию,события клавишь, соприкосновение поверхностей и рисуем объекты--------

    game = True
    game_over = False
    while game:
        #Анимация мяча
        #МЯЧ
        #ball = pg.draw.circle(sc,YELLOW,(ball_x, ball_y), ball_r)
        #новый мяч виде картинки
        new_ball = pic_surf.get_rect(center=(ball_x+65,ball_y+90))
        # обновляем местоположение мяча
        ball_x += ball_xv
        ball_y += ball_yv
        
        # Соприкосновение мяча с верхом и низом экрана
        if ball_y - ball_r <= 100 or ball_y + ball_r >= SURF_HEIGHT + 100:
            ball_yv *= -1.0
            soundHit.play()
         
        #Соприкосновение ракеток с верхом низом, движение в верх в них по Y
        if racket_left_y < 0:
            racket_left_y = 0
        elif racket_left_y + racket_left_h > SURF_HEIGHT + 100:
            racket_left_y = SURF_HEIGHT - racket_left_h

        if racket_right_y < 0:
            racket_right_y = 0
        elif racket_right_y + racket_right_h > SURF_HEIGHT + 100:
            racket_right_y = SURF_HEIGHT - racket_right_h

        # левая ракетка
        if ball_x - 25 < racket_left_x + racket_left_w and ball_y >= racket_left_y and ball_y <= racket_left_y + racket_left_h:
            ball_xv *= -1
            ball_yv += r.randint(-5,5)
            soundLeft.play()

        # правая ракетка
        if ball_x + 25 > racket_right_x and ball_y >= racket_right_y and ball_y <= racket_right_y + racket_right_h:
            ball_xv *= -1
            ball_yv += r.randint(-5,5)
            soundRight.play()

        #главный экран
        sc.fill(GREEN)
        
        # размещаем поверхности на главной,
        # указывая координаты
        # их верхних левых углов
        
        sc.blit(surf_left, (200, 100))
        sc.blit(surf_right, (607, 100))
        net = pg.draw.line(sc, GREEN1, (601,699), (601,100),10)
        
        #left border
        pg.draw.line(sc,BLACK, (200,699), (200,100),5)
        pg.draw.line(sc,BLACK, (200,100), (601,100),5)
        pg.draw.line(sc,BLACK, (200,699), (601,699),5)
        
        #right border
        pg.draw.line(sc,WHITE, (1008,699), (1008,100),5)
        pg.draw.line(sc,WHITE, (1008,100), (603,100),5)
        pg.draw.line(sc,WHITE, (1008,698), (603,698),5)
        
        #рисуем ракетки и мячик
        racket_left = pg.draw.rect(sc,BLACK,(racket_left_x,racket_left_y,racket_left_w,racket_left_h))    
        racket_right = pg.draw.rect(sc,WHITE,(racket_right_x,racket_right_y,racket_right_w,racket_right_h))
        
        #Отображение управления(текст)
        sc.blit(text1, (40, 50))
        sc.blit(text2, (1000, 50))
        sc.blit(text3, (300,770))
        
        #рисуем pic
        sc.blit(pic_surf, man_right)
        sc.blit(pic_surf, man_left)
        sc.blit(pic_ball, new_ball)
        
        #счёт
        score_text = font.render(str(player1_score) + ":" + str(player2_score), 1, WHITE)
        sc.blit(score_text, (WIN_WIDTH / 2 - score_text.get_width() / 2, 10))
        
         # счётчик очков игроков 
        if ball_x <= 222:
            player2_score += 1
            ball_x = (WIN_WIDTH / 2)
            ball_y = (WIN_HEIGHT / 2)
            ball_xv = 6
            ball_yv = r.randint(-6,6)
            soundGoal.play()
            if ball_yv == 0:
                ball_yv += 1
            
        elif ball_x >=983:
            player1_score += 1
            ball_x = (WIN_WIDTH / 2)
            ball_y = (WIN_HEIGHT / 2)
            ball_xv = -6
            ball_yv = r.randint(-6,6)
            soundGoal.play()
            if ball_yv == 0:
                ball_yv += 1
            
        if player1_score == score:
            game_over = True
            
        elif player2_score == score:
            game_over = True
        
        if game_over:
            ball_xv = 0
            ball_yv = 0
            sc.fill(BLACK)
            sc.blit(text4, (400,350))
            sc.blit(RESTART, (515,600))
            
            if player1_score == score:
                sc.blit(BLACK_WIN, (530,430))
            elif player2_score == score:
                sc.blit(WHITE_WIN, (530,430))
#__________________________________________________________________________________________________________________________________________  
        for i in pg.event.get(): 
            if i.type == pg.QUIT:
                sys.exit()
                
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_w:
                    if racket_left_y >= 150:
                        racket_left_y -= 50
                                                             
                elif i.key == pg.K_s:
                    if racket_left_y <= SURF_HEIGHT-150:
                        racket_left_y += 50
                                                            #движение ракеток вверх вних левая W/S правая UP/DOWN
                elif i.key == pg.K_UP:
                    if racket_right_y >= 150:
                        racket_right_y -= 50
                        
                elif i.key == pg.K_DOWN:
                    if racket_right_y <= SURF_HEIGHT-150:
                        racket_right_y += 50
                        
                elif i.key == pg.K_ESCAPE:                  # ESCAPE выход 
                    sys.exit()
                                                                   
                elif i.key == pg.K_RETURN:                  # старт мяча
                    ball_xv = 6
                    ball_yv = r.randint(-6,6)
                    if ball_yv == 0:
                        ball_yv += 1
                    
                elif i.key == pg.K_r:
                    Game()
                    
                elif i.key == pg.K_1:
                    pg.mixer.music.pause()
                    
                elif i.key == pg.K_2:
                    pg.mixer.music.unpause()
                    #pg.mixer.music.set_volume(0.1)
#______________________________________________________________________________________________________________________________________
        #обновляем экран
        pg.display.update()
        clock.tick(FPS)
Start()