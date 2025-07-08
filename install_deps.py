# install_dependencies.py
"""
Script para instalar automaticamente todas as dependências
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Executa um comando e retorna se foi bem-sucedido"""
    try:
        print(f"Executando: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Sucesso")
            return True
        else:
            print(f"❌ Erro: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exceção: {e}")
        return False

def main():
    print("=== INSTALADOR DE DEPENDÊNCIAS - ELISEU POT ===")
    print(f"Python: {sys.version}")
    print(f"Pip: ", end="")
    
    # Verifica se pip está disponível
    if not run_command("pip --version"):
        print("❌ Pip não encontrado!")
        print("Instale o Python com pip primeiro.")
        input("Pressione Enter para sair...")
        return
    
    # Lista de dependências
    dependencies = [
        "PyQt5",
        "pymem", 
        "keyboard",
        "pywin32"
    ]
    
    print(f"\nInstalando {len(dependencies)} dependências...")
    
    failed = []
    for dep in dependencies:
        print(f"\n📦 Instalando {dep}...")
        if run_command(f"pip install {dep}"):
            print(f"✅ {dep} instalado com sucesso")
        else:
            print(f"❌ Falha ao instalar {dep}")
            failed.append(dep)
    
    print("\n=== RESUMO ===")
    if not failed:
        print("✅ Todas as dependências foram instaladas com sucesso!")
        print("\nVocê pode agora executar:")
        print("  python debug_startup.py  (para diagnóstico)")
        print("  python main_debug.py     (versão debug)")
        print("  python main.py           (versão normal)")
    else:
        print(f"❌ Falha ao instalar: {', '.join(failed)}")
        print("\nTente instalar manualmente:")
        for dep in failed:
            print(f"  pip install {dep}")
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()