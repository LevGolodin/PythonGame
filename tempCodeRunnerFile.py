        if not is_jump and keys[pygame.K_SPACE]:
                is_jump = True
        elif is_jump and keys[pygame.K_UP]:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 13
        elif is_jump and keys[pygame.K_DOWN]:
            if jump_count > 0:
                player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 13