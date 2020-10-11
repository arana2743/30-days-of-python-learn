import draw

def play_game():
    result = 'Playing game now'
    return result

def main():
    result = play_game()
    draw.draw_game(result)
    
if __name__ == '__main__':
    main()
