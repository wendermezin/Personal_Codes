def click_position(x, y):
    pyautogui.click(x, y)

positions_to_click = [
    (1267, 517),  # opcoes
    (1151, 599),  # editar
    (750, 607),   # dependencia
    (841, 520),   # patrimonio
    (1000, 652)   # confirmar
]

tempo_total_execucao = 600 * 60

start_time = time.time()
while (time.time() - start_time) < tempo_total_execucao:
    time.sleep(5)

    for pos in positions_to_click:
        click_position(*pos)
        time.sleep(3)
