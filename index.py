# Criando uma lista de dicionários para armazenar os comentários e emoções
comentarios = [
    {"Autor": "João", "Comentário": "Estou tão feliz hoje", "Sentimento": "positivo"},
    {"Autor": "Maria", "Comentário": "Este filme é triste", "Sentimento": "negativo"},
    {"Autor": "Carlos", "Comentário": "Que dia chuvoso entediante...", "Sentimento": "positivo"},
    {"Autor": "Ana", "Comentário": "Adorei a nova musica da banda!", "Sentimento": "negativo"},
    {"Autor": "Roberto", "Comentário": "Eureka, consegui resolver este problema", "Sentimento": "positivo"}
]

# Função para totalizar a quantidade de comentários negativos e positivos
def contar_sentimentos(comentarios):
    total_negativos = sum(1 for comentario in comentarios if comentario["Sentimento"] == "negativo")
    total_positivos = sum(1 for comentario in comentarios if comentario["Sentimento"] == "positivo")
    return total_negativos, total_positivos

# Função para calcular e mostrar na tela a proporção de cada sentimento em relação ao total de comentários
def proporcao_sentimentos(comentarios):
    total_comentarios = len(comentarios)
    total_negativos, total_positivos = contar_sentimentos(comentarios)
    proporcao_negativos = total_negativos / total_comentarios
    proporcao_positivos = total_positivos / total_comentarios
    print("Proporção de comentários negativos: {:.2%}".format(proporcao_negativos))
    print("Proporção de comentários positivos: {:.2%}".format(proporcao_positivos))

# Função para mostrar apenas os comentários positivos
def mostrar_comentarios_positivos(comentarios):
    comentarios_positivos = [comentario["Comentário"] for comentario in comentarios if comentario["Sentimento"] == "positivo"]
    for comentario in comentarios_positivos:
        print(comentario)

# Adicionando a chave "sentimento_valor" em cada dicionário
for comentario in comentarios:
    comentario["sentimento_valor"] = 1 if comentario["Sentimento"] == "positivo" else 0

# Exibindo as informações
print("Total de comentários negativos e positivos:")
print("Negativos:", contar_sentimentos(comentarios)[0])
print("Positivos:", contar_sentimentos(comentarios)[1])
print("\nProporção de cada sentimento:")
proporcao_sentimentos(comentarios)
print("\nComentários positivos:")
mostrar_comentarios_positivos(comentarios)
