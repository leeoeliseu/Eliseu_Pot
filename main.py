# main.py
"""
Eliseu Pot - Ragnarok Helper
Arquivo principal de inicialização
"""
import sys
import os

# Adiciona o diretório atual ao path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Função principal do aplicativo"""
    print("🚀 Iniciando Eliseu Pot...")
    
    # Verifica privilégios administrativos PRIMEIRO
    try:
        from core.admin import run_as_admin
        if not run_as_admin():
            # Se retornou False, não conseguiu privilégios
            print("❌ Não foi possível obter privilégios administrativos")
            sys.exit(1)
        # Se chegou aqui, está rodando como admin
        print("✅ Privilégios administrativos confirmados")
    except Exception as e:
        print(f"❌ Erro na verificação de admin: {e}")
        sys.exit(1)
    
    try:
        # Imports do PyQt5
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtGui import QFont
        print("✅ PyQt5 importado")
        
        # Imports da aplicação
        from ui.main_window import MainWindow
        from ui.styles import get_dark_stylesheet, setup_dark_palette
        print("✅ Módulos da aplicação importados")
        
        # Inicializa aplicação Qt
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(True)
        
        # Configura fonte padrão
        font = QFont()
        font.setPointSize(11)
        app.setFont(font)
        print("✅ Aplicação Qt inicializada")
        
        # Aplica tema escuro
        try:
            palette = setup_dark_palette()
            app.setPalette(palette)
            app.setStyleSheet(get_dark_stylesheet())
            print("✅ Tema escuro aplicado")
        except Exception as e:
            print(f"⚠️  Aviso: Erro ao aplicar tema: {e}")
        
        # Cria e exibe janela principal
        print("🎨 Criando interface...")
        window = MainWindow()
        window.show()
        print("✅ Interface criada e exibida")
        
        # Inicia loop da aplicação
        print("🔄 Iniciando loop da aplicação...")
        result = app.exec_()
        print(f"✅ Aplicação finalizada (código: {result})")
        sys.exit(result)
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("📦 Instale as dependências:")
        print("   pip install PyQt5 pymem keyboard pywin32")
        input("Pressione Enter para sair...")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Erro geral: {e}")
        import traceback
        traceback.print_exc()
        input("Pressione Enter para sair...")
        sys.exit(1)


if __name__ == "__main__":
    main()
