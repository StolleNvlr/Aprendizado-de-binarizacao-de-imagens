from PIL import Image

def transformar_em_cinza(imagem):
    """Converte uma imagem colorida para tons de cinza."""
    return imagem.convert("L")  # Converte para escala de cinza

def binarizar(imagem_cinza, limiar=127):
    """Converte uma imagem em tons de cinza para binarizada."""
    # Aplica a binarização: pixels acima do limiar viram 255, abaixo viram 0
    return imagem_cinza.point(lambda p: 255 if p > limiar else 0)

# Caminho da imagem original
caminho_imagem = "1_the_rock_2_easy_resize_com_-28692002.jpg"

# Abrir a imagem usando Pillow
imagem_colorida = Image.open(caminho_imagem)

# Converter para tons de cinza
imagem_cinza = transformar_em_cinza(imagem_colorida)

# Salvar a imagem em tons de cinza
imagem_cinza.save("imagem_cinza.jpg")
print("Imagem em tons de cinza salva como 'imagem_cinza.jpg'.")

# Converter para binarizada
imagem_binarizada = binarizar(imagem_cinza)

# Salvar a imagem binarizada
imagem_binarizada.save("imagem_binarizada.jpg")
print("Imagem binarizada salva como 'imagem_binarizada.jpg'.")
