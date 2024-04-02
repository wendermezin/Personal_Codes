import os
import sys
from sphinx.cmd.quickstart import main as sphinx_quickstart

def generate_documentation():
    doc_dir = 'docs'

    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    os.chdir(doc_dir)

    sys.argv = ['sphinx-quickstart', '--quiet', '--sep', '--project', 'Nome do Seu Projeto']
    sphinx_quickstart()

    os.system('make html')

    print("Documentação gerada com sucesso!")

if __name__ == "__main__":
    generate_documentation()
