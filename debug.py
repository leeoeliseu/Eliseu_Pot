# debug_startup.py
"""
Script de diagnóstico para identificar problemas na inicialização
"""
import sys
import os
import traceback

print("=== DIAGNÓSTICO DE INICIALIZAÇÃO ===")
print(f"Python versão: {sys.version}")
print(f"Diretório atual: {os.getcwd()}")
print(f"Argumentos: {sys.argv}")

# Teste 1: Verificar se é Windows
print("\n1. Verificando sistema operacional...")
if sys.platform != "win32":
    print("❌ ERRO: Este script só funciona no Windows!")
    input("Pressione Enter para sair...")
    sys.exit(1)
print("✅ Sistema Windows detectado")

# Teste 2: Verificar dependências
print("\n2. Verificando dependências...")
missing_deps = []

try:
    import PyQt5
    print("✅ PyQt5 instalado")
except ImportError as e:
    print(f"❌ PyQt5 não encontrado: {e}")
    missing_deps.append("PyQt5")

try:
    import pymem
    print("✅ pymem instalado")
except ImportError as e:
    print(f"❌ pymem não encontrado: {e}")
    missing_deps.append("pymem")

try:
    import keyboard
    print("✅ keyboard instalado")
except ImportError as e:
    print(f"❌ keyboard não encontrado: {e}")
    missing_deps.append("keyboard")

try:
    import win32gui
    print("✅ pywin32 instalado")
except ImportError as e:
    print(f"❌ pywin32 não encontrado: {e}")
    missing_deps.append("pywin32")

if missing_deps:
    print(f"\n❌ DEPENDÊNCIAS FALTANDO: {', '.join(missing_deps)}")
    print("Para instalar:")
    for dep in missing_deps:
        print(f"  pip install {dep}")
    input("Pressione Enter para sair...")
    sys.exit(1)

# Teste 3: Verificar estrutura de arquivos
print("\n3. Verificando estrutura de arquivos...")
required_files = [
    "main.py",
    "config/__init__.py",
    "config/constants.py",
    "config/settings.py",
    "core/__init__.py",
    "core/admin.py",
    "core/memory.py",
    "core/input.py",
    "threads/__init__.py",
    "threads/autopot.py",
    "threads/skillspam.py",
    "threads/monitor.py",
    "ui/__init__.py",
    "ui/main_window.py",
    "ui/dialogs.py",
    "ui/styles.py",
    "ui/tabs/__init__.py",
    "ui/tabs/autopot_tab.py",
    "ui/tabs/skillspam_tab.py",
    "ui/tabs/profiles_tab.py",
    "utils/__init__.py",
    "utils/profiles.py",
    "utils/hotkeys.py"
]

missing_files = []
for file in required_files:
    if os.path.exists(file):
        print(f"✅ {file}")
    else:
        print(f"❌ {file}")
        missing_files.append(file)

if missing_files:
    print(f"\n❌ ARQUIVOS FALTANDO: {len(missing_files)} arquivos")
    print("Arquivos necessários que não foram encontrados:")
    for file in missing_files:
        print(f"  - {file}")
    input("Pressione Enter para sair...")
    sys.exit(1)

# Teste 4: Verificar imports
print("\n4. Testando imports...")
try:
    sys.path.insert(0, os.getcwd())
    
    print("  Testando config...")
    from config.constants import HP_ADDRESS
    from config.settings import app_settings
    print("  ✅ config OK")
    
    print("  Testando core...")
    from core.admin import run_as_admin
    from core.memory import GameMemoryReader
    from core.input import send_key
    print("  ✅ core OK")
    
    print("  Testando threads...")
    from threads.autopot import AutoPotThread
    from threads.skillspam import SkillSpamThread
    from threads.monitor import GameMonitorThread
    print("  ✅ threads OK")
    
    print("  Testando ui...")
    from ui.main_window import MainWindow
    from ui.dialogs import ProcessSelectionDialog
    from ui.styles import get_dark_stylesheet
    print("  ✅ ui OK")
    
    print("  Testando utils...")
    from utils.profiles import ProfileManager
    from utils.hotkeys import HotkeyManager
    print("  ✅ utils OK")
    
except Exception as e:
    print(f"❌ ERRO DE IMPORT: {e}")
    print(f"Traceback completo:")
    traceback.print_exc()
    input("Pressione Enter para sair...")
    sys.exit(1)

# Teste 5: Verificar privilégios administrativos
print("\n5. Verificando privilégios...")
try:
    import ctypes
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        print("✅ Executando como administrador")
    else:
        print("⚠️  NÃO está executando como administrador")
        print("   Isso pode causar problemas com hotkeys globais")
except Exception as e:
    print(f"❌ Erro ao verificar privilégios: {e}")

# Teste 6: Tentar inicializar aplicação
print("\n6. Tentando inicializar aplicação...")
try:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt
    
    # Criar aplicação sem mostrar janela
    app = QApplication(sys.argv)
    print("✅ QApplication criada com sucesso")
    
    # Testar criação da janela principal
    from ui.main_window import MainWindow
    print("✅ MainWindow pode ser importada")
    
    app.quit()
    print("✅ Aplicação finalizada corretamente")
    
except Exception as e:
    print(f"❌ ERRO NA INICIALIZAÇÃO: {e}")
    print("Traceback completo:")
    traceback.print_exc()
    input("Pressione Enter para sair...")
    sys.exit(1)

print("\n=== DIAGNÓSTICO CONCLUÍDO ===")
print("✅ Todos os testes passaram!")
print("A aplicação deveria funcionar corretamente.")
print("\nSe ainda assim não abrir, execute:")
print("python main.py")
print("\nOu tente o modo debug:")
print("python -v main.py")

input("\nPressione Enter para sair...")