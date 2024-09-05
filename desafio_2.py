def jogada(game_state,i, n):
    game_state[n] = game_state[n] - i
    return game_state
def fim_de_jogo(jogo):
    for i in jogo:
        if i != 0:
            return False
    return True

def leftmost_1(nim_sum):
    posicao = 0
    while nim_sum > 1:
        nim_sum = nim_sum >> 1
        posicao += 1
        
    return posicao
def bit_pos(number,check):
    binary_number = bin(number)[2:].zfill(4)[::-1]
    if binary_number[check] == "1":
        return True
def checa_bits(jogo,check):
    for n in range(len(jogo)):
        if bit_pos(jogo[n],check):
            return n
def melhor_jogada(jogo):
    nim_sum = 0
    for n in jogo:
        nim_sum ^= n
    if nim_sum != 0:
        leftmost_nim = leftmost_1(nim_sum)
        col = checa_bits(jogo, leftmost_nim)
        palitos_retirados = 0
        for i in range(len(jogo)):
            if i != col:
                palitos_retirados ^= jogo[i]
        palitos_retirados = jogo[col] - palitos_retirados
        return palitos_retirados, col
    elif nim_sum == 0:
        for n in range(len(jogo)):
            if jogo[n] != 0:
                return 1, n


        


def main():
    i = int(input("digite quantos palitos cada coluna tera:"))
    n = int(input("digite quantas colunas tera o jogo:"))

    jogo = [i for _ in range(n)]

    print(jogo)

    player = int(input("digite 1 para comecar ou 0 para deixar o computador comecar:"))
    while not fim_de_jogo(jogo):
        if player == 1:
            """n = int(input("digite a coluna:")) - 1
            if n >= len(jogo) or n <= 0:
                print("coluna inexistente, digite outra")
                continue
            elif jogo[n] == 0:
                print("coluna vazia, digite outra")
                continue
  
            i = int(input("digite quantos palitos deseja retirar:"))
            if i > jogo[n]:
                print("numero de palitos maior que o disponivel, digite outro")
                continue
            if i == 0:
                print("numero de palitos invalido, digite outro")
                continue """
            #jogo = jogada(jogo, i, n)
            move = melhor_jogada(jogo)
            jogo = jogada(jogo, move[0], move[1])
            print(jogo)
            player = 0
        else:
            move = melhor_jogada(jogo)
            jogo = jogada(jogo, move[0], move[1])
            print(jogo)
            player = 1
main()

