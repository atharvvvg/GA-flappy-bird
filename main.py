import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

# Font for displaying score
font = pygame.font.Font(None, 36)

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def display_score(window, score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

def main():
    pipes_spawn_time = 10
    score = 0

    while True:
        quit_game()

        config.window.fill((0, 0, 0))

        # Spawn Ground
        config.ground.draw(config.window)

        # Spawn Pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
                score += 1  # Increment score when a pipe goes off screen

        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()
            score = 0  # Reset score when all players are extinct

        # Display the score
        display_score(config.window, score)

        clock.tick(60)
        pygame.display.flip()

main()
