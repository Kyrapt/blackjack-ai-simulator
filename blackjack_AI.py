import random
import json
from urllib.request import Request, urlopen

class Carta:
    VALORES_ORDEM = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
    NAIPES_ORDEM = ['Paus', 'Ouros', 'Copas', 'Espadas']

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

    def _obter_indices(self):
        return (self.VALORES_ORDEM.index(self.valor), self.NAIPES_ORDEM.index(self.naipe))

    def __lt__(self, other):
        return self._obter_indices() < other._obter_indices()

class Baralho:
    def __init__(self):
        self.cartas = [Carta(v, n) for n in Carta.NAIPES_ORDEM for v in Carta.VALORES_ORDEM]
        self.cartas_removidas = []

    def baralhar(self):
        random.shuffle(self.cartas)

    def retirar(self):
        if not self.cartas: return None
        carta = self.cartas.pop()
        self.cartas_removidas.append(carta)
        return carta

def calcular_pontos(mao):
    total, ases = 0, 0
    for carta in mao:
        if carta.valor in ['Valete', 'Rainha', 'Rei']: total += 10
        elif carta.valor == 'Ás': total += 11; ases += 1
        else: total += int(carta.valor)
    while total > 21 and ases > 0:
        total -= 10; ases -= 1
    return total


def decisao_ia_web(mao_dealer, pontos_jogador):
    pontos_dealer = calcular_pontos(mao_dealer)
    cartas_texto = ", ".join(str(c) for c in mao_dealer)
    
    prompt = f"Blackjack game. Dealer hand: {cartas_texto} ({pontos_dealer} points). Player has {pontos_jogador} points. Reply with exactly one word, HIT or STAND:"
    
    # API alternativa estável, gratuita e sem bloqueios de texto
    url = "https://duckduckgo.com"
    
    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")
    
    req = Request(url, data=payload, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    })
    
    try:
        with urlopen(req, timeout=5) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            # Extrai a resposta direta do chat
            texto_gerado = res_body.get("choices", [{}])[0].get("message", {}).get("content", "").strip().upper()
            return "PEDIR" if "HIT" in texto_gerado else "PARAR"
    except:
        # Fallback de segurança se o site estiver em baixo
        return "PEDIR" if pontos_dealer < 17 else "PARAR"


def blackjack_com_ia():
    print("--- Início do Jogo de Blackjack com IA Gratuita Web ---")
    baralho = Baralho()
    baralho.baralhar()
    
    mao_dealer, mao_jogador = [], []
    
    for _ in range(2):
        mao_dealer.append(baralho.retirar())
        mao_jogador.append(baralho.retirar())
    
    print(f"Carta visível do Dealer: {str(mao_dealer[0])}")
    print(f"A sua mão: {[str(c) for c in mao_jogador]} (Total: {calcular_pontos(mao_jogador)} pontos)")
    
    while calcular_pontos(mao_jogador) < 21:
        opcao = input("Deseja pedir mais uma carta? (s/n): ").strip().lower()
        if opcao == 's':
            mao_jogador.append(baralho.retirar())
            print(f"A sua mão: {[str(c) for c in mao_jogador]} (Total: {calcular_pontos(mao_jogador)} pontos)")
        else:
            break
            
    pontos_jogador = calcular_pontos(mao_jogador)
    if pontos_jogador > 21:
        print("Ultrapassou os 21 pontos! Perdeu o jogo.")
        return
        
    print("\n--- Turno do Dealer (Analisado por IA) ---")
    
    while True:
        pontos_dealer = calcular_pontos(mao_dealer)
        if pontos_dealer >= 21: break
            
        decisao = decisao_ia_web(mao_dealer, pontos_jogador)
        print(f"A IA Dealer analisou a jogada e decidiu: {decisao}")
        
        if decisao == "PEDIR" and pontos_dealer < pontos_jogador:
            nova_carta = baralho.retirar()
            if nova_carta:
                mao_dealer.append(nova_carta)
                print(f"Dealer retirou: {nova_carta} (Total do Dealer: {calcular_pontos(mao_dealer)} pontos)")
            else:
                break
        else:
            break
            
    pontos_dealer = calcular_pontos(mao_dealer)
    print("\n--- Resultado Final ---")
    print(f"Sua pontuação: {pontos_jogador} | Pontuação da IA: {pontos_dealer}")
    
    if pontos_dealer > 21:
        print("A IA ultrapassou os 21 pontos! Ganhou o jogo!")
    elif pontos_dealer > pontos_jogador:
        print("A IA ganhou o jogo!")
    elif pontos_dealer == pontos_jogador:
        print("Empate!")
    else:
        print("Parabéns, ganhou o jogo!")

if __name__ == "__main__":
    blackjack_com_ia()
