#!/usr/bin/env python3
"""
Script para gerar arquivos estáticos do portfólio Flask para GitHub Pages
"""

import os
import shutil
from app import app


def generate_static_site():
    """Gera os arquivos estáticos do portfólio"""

    # Criar diretório de saída
    output_dir = "dist"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Configurar Flask para modo de produção
    app.config["SERVER_NAME"] = None  # Remover para evitar problemas no GitHub Pages
    app.config["PREFERRED_URL_SCHEME"] = "https"

    with app.app_context():
        # Gerar página principal
        with app.test_client() as client:
            response = client.get("/")

            if response.status_code == 200:
                with open(
                    os.path.join(output_dir, "index.html"), "w", encoding="utf-8"
                ) as f:
                    f.write(response.get_data(as_text=True))
                print("index.html gerado com sucesso")
            else:
                print(f"Erro ao gerar index.html: {response.status_code}")
                return False

    # Copiar arquivos estáticos
    static_source = "static"
    static_dest = os.path.join(output_dir, "static")

    if os.path.exists(static_source):
        shutil.copytree(static_source, static_dest)
        print("Arquivos estáticos copiados com sucesso")

    # Criar arquivo .nojekyll para GitHub Pages
    with open(os.path.join(output_dir, ".nojekyll"), "w") as f:
        f.write("")
    print("Arquivo .nojekyll criado")

    # Criar CNAME se necessário (opcional)
    # with open(os.path.join(output_dir, 'CNAME'), 'w') as f:
    #     f.write('diogojacomini.com')

    print("Site estático gerado com sucesso em ./dist/")
    return True


if __name__ == "__main__":
    success = generate_static_site()
    if not success:
        exit(1)
