# Pong - Dois Jogadores

Jogo Pong simples para duas pessoas usando Pygame.

Controles:
- Jogador esquerdo: W (para cima), S (para baixo)
- Jogador direito: Setas para cima e para baixo

Instalação:

1. Crie um ambiente virtual (opcional):

   python -m venv .venv
   ; .venv\Scripts\Activate.ps1

2. Instale dependências:

   pip install -r requirements.txt

Execução:

   python main.py

Melhorias possíveis:

- Suavizar a física da bola e aumentar variação de ângulo.
- Adicionar tela de menu e pausa.
- Sons e efeitos quando a bola bate ou ponto marcado.
- Sistema de partidas (melhor de N) e salvar melhores scores.

Notas de manutenção:

- Código dividido em módulos pequenos para facilitar testes e manutenção.
- Para escalar, separar lógica de render/entrada e adicionar testes unitários para a física da bola.

