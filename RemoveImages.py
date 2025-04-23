import os
from pathlib import Path
from hashlib import md5

def calcHash(path: str):
    with open(path, 'rb') as f:
        return md5(f.read()).hexdigest()
    
def removePage1Images(directory: Path):
    for arquivo in directory.rglob("page1_img*.*"):
        arquivo.unlink()

def removeUnnecessarilyImages():
    path = "C:\\Users\\migue\\OneDrive\\Documentos\\ProvaExtract"

    diretorio = Path(path)

    if not diretorio.is_dir():
        print(f"Erro: {diretorio} não é um diretório válido.")
        return
    
    removePage1Images(diretorio)

    images_hash = {}
    images_to_be_removed = []
    hash_duplicated = ''

    for arquivo in diretorio.rglob("*.png"):
        hash_atual = calcHash(arquivo)

        if hash_atual in images_hash:
            print(f"Duplicado: {arquivo} (igual a {images_hash[hash_atual]}) — Adicionando ao hashMap...")
            arquivo.unlink()
            images_to_be_removed.append(arquivo)
            hash_duplicated = hash_atual
        else:
            images_hash[hash_atual] = arquivo

    if(images_hash[hash_duplicated]):
        unnecessarily_root_image = images_hash[hash_duplicated]
        unnecessarily_root_image.unlink()

    print(f"\n✅ Total de duplicatas removidas: {len(images_to_be_removed)}")