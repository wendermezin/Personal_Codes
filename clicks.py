def print_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f'X: {x} Y: {y}'
            print(position_str)
            time.sleep(3)
    except KeyboardInterrupt:
        print('\nCoordenadas do mouse interrompidas.')

print("Move o mouse para a posição desejada e aguarde...")
print("Pressione Ctrl+C para interromper.")

print_mouse_position()
