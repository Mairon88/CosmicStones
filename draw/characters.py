import pygame

word = 'gracz 1'
num = ''

def characters(event, option):
    global word, num
    if event.type == pygame.KEYDOWN:
        if option == 'player_names':
            if len(word) < 15:
                if event.key == pygame.K_a:
                    word += "a"
                if event.key == pygame.K_b:
                    word += "b"
                if event.key == pygame.K_c:
                    word += "c"
                if event.key == pygame.K_d:
                    word += "d"
                if event.key == pygame.K_e:
                    word += "e"
                if event.key == pygame.K_f:
                    word += "f"
                if event.key == pygame.K_g:
                    word += "g"
                if event.key == pygame.K_h:
                    word += "h"
                if event.key == pygame.K_i:
                    word += "i"
                if event.key == pygame.K_j:
                    word += "j"
                if event.key == pygame.K_k:
                    word += "k"
                if event.key == pygame.K_l:
                    word += "l"
                if event.key == pygame.K_m:
                    word += "m"
                if event.key == pygame.K_n:
                    word += "n"
                if event.key == pygame.K_o:
                    word += "o"
                if event.key == pygame.K_p:
                    word += "p"
                if event.key == pygame.K_r:
                    word += "r"
                if event.key == pygame.K_s:
                    word += "s"
                if event.key == pygame.K_t:
                    word += "t"
                if event.key == pygame.K_w:
                    word += "w"
                if event.key == pygame.K_z:
                    word += "z"
                if event.key == pygame.K_q:
                    word += "q"
                if event.key == pygame.K_x:
                    word += "x"
                if event.key == pygame.K_y:
                    word += "y"
                if event.key == pygame.K_u:
                    word += "u"
                if event.key == pygame.K_v:
                    word += "v"
                if event.key == pygame.K_0:
                    word += "0"
                if event.key == pygame.K_SPACE:
                    word += " "
                if event.key == pygame.K_1:
                    word += "1"
                if event.key == pygame.K_2:
                    word += "2"
                if event.key == pygame.K_3:
                    word += "3"
                if event.key == pygame.K_4:
                    word += "4"
                if event.key == pygame.K_5:
                    word += "5"
                if event.key == pygame.K_6:
                    word += "6"
                if event.key == pygame.K_7:
                    word += "7"
                if event.key == pygame.K_8:
                    word += "8"
                if event.key == pygame.K_9:
                    word += "9"
            if event.key == pygame.K_BACKSPACE:
                if len(word) > 0:
                    word = word[:-1]
        elif option == 'num_of_players':
            if event.key == pygame.K_2:
                num = 2
            if event.key == pygame.K_3:
                num = 3
            if event.key == pygame.K_4:
                num = 4





