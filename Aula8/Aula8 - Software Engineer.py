class Filme:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

class Catalogo:
    def __init__(self, titulo, qtd_filmes):
        self.titulo = titulo
        self.qtd_filmes = qtd_filmes
        self.lista_filmes = [] # Agregação (os filmes existem fora daqui)

    def add_filme(self, novo_filme):
        self.lista_filmes.append(novo_filme)
        self.qtd_filmes = len(self.lista_filmes)

    def listar_filmes(self):
        print(f"\n--- Catálogo: {self.titulo} ---")
        for filme in self.lista_filmes:
            print(f"Filme: {filme.titulo} | Duração: {filme.duracao} min | Gênero: {filme.genero}")

class Plataforma:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
        self.catalogo_da_plataforma = None # Onde o catálogo será guardado

    def definir_catalogo(self, objeto_catalogo):
        # Aqui acontece a Composição: a plataforma agora "tem" um catálogo
        self.catalogo_da_plataforma = objeto_catalogo
        print(f"Sistema: Catálogo '{objeto_catalogo.titulo}' vinculado à {self.nome}.")

class Avaliacao:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

class Usuario:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.minhas_avaliacoes = {} # Composição (a avaliação pertence ao usuário)

    def avaliar(self, filme_alvo, objeto_avaliacao):
        self.minhas_avaliacoes[filme_alvo.titulo] = objeto_avaliacao
        print(f"Sucesso: {self.nome} avaliou o filme {filme_alvo.titulo}")

    def ver_avaliacoes(self):
        print(f"\n--- Minhas Avaliações ({self.nome}) ---")
        for titulo_filme in self.minhas_avaliacoes:
            av = self.minhas_avaliacoes[titulo_filme]
            print(f"Filme: {titulo_filme} | Nota: {av.nota} | Comentário: {av.comentario}")

# --- EXECUÇÃO CONFORME SOLICITADO ---

# 1. Instanciando Plataforma e Catálogo
netflix = Plataforma("Netflix", "EUA")
catalogo = Catalogo("Filmes em Destaque", 0)

# Vinculando o catálogo à plataforma (Regra da Composição)
netflix.definir_catalogo(catalogo)

# 2. Criando os filmes
filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie", 114, "Comédia")

# 3. Adicionando filmes ao catálogo (Regra da Agregação)
catalogo.add_filme(filme1)
catalogo.add_filme(filme2)

# 4. Criando usuário e sua avaliação
usuario = Usuario("Ana", "ana@email.com", "Premium")
avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")

# 5. Realizando as ações
usuario.avaliar(filme1, avaliacao)
catalogo.listar_filmes()
usuario.ver_avaliacoes()