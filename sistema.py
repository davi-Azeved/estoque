# Definindo a classe Produto
class Produto:
    def __init__(self, nome, categoria, quantidade):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade

# Definindo a classe ControleEstoque
class ControleEstoque:
    def __init__(self):
        # Inicialização das listas e dicionários para armazenar os produtos e informações de estoque
        self.produtos = []  # Lista para armazenar objetos da classe Produto
        self.categorias = set()  # Conjunto para armazenar categorias únicas
        self.valor_minimo_por_categoria = {
            'eletronicos': 10,
            'vestuario': 20,
            'alimentos': 30
        }  # Dicionário que associa categorias a valores mínimos de estoque

    def registrar_entrada(self, nome, categoria, quantidade):
        # Método para registrar uma entrada de produto no estoque
        produto = Produto(nome, categoria, quantidade)  # Cria um objeto Produto com as informações fornecidas
        self.produtos.append(produto)  # Adiciona o produto à lista de produtos
        self.categorias.add(categoria)  # Adiciona a categoria ao conjunto de categorias

    def calcular_estoque_total(self):
        # Método para calcular o estoque total de todos os produtos
        estoque_total = 0
        for produto in self.produtos:
            estoque_total += produto.quantidade  # Somando as quantidades de todos os produtos
        return estoque_total

    def exibir_porcentagem_por_categoria(self):
        # Método para exibir a porcentagem de estoque por categoria
        estoque_total = self.calcular_estoque_total()  # Calcula o estoque total
        for categoria in self.categorias:
            # Para cada categoria presente no conjunto de categorias
            quantidade_por_categoria = sum(produto.quantidade for produto in self.produtos if produto.categoria == categoria)
            # Calcula a quantidade total de produtos na categoria atual
            porcentagem = (quantidade_por_categoria / estoque_total) * 100
            # Calcula a porcentagem de estoque da categoria
            print(f'Categoria: {categoria} - Porcentagem em estoque: {porcentagem:.2f}%')

# Criando um objeto ControleEstoque
controle = ControleEstoque()

# Registrando entradas de produtos
controle.registrar_entrada('Celular', 'eletronicos', 50)
controle.registrar_entrada('Camiseta', 'vestuario', 30)
controle.registrar_entrada('Arroz', 'alimentos', 100)

# Exibindo a porcentagem de estoque por categoria
controle.exibir_porcentagem_por_categoria()