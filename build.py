import os
import sys
import subprocess
import shutil
import signal
import atexit

VENV_DIR = 'virtual_idor_lab'
REQUIREMENTS = 'requirements.txt'
APP_FILE = 'app.py'

def cleanup():
    if os.path.exists(VENV_DIR):
        print(f'Removendo ambiente virtual {VENV_DIR}...')
        shutil.rmtree(VENV_DIR)
        print('Ambiente virtual removido.')


atexit.register(cleanup)
signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))

if not os.path.exists(VENV_DIR):
    print(f'Criando ambiente virtual em {VENV_DIR}...')
    subprocess.check_call([sys.executable, '-m', 'venv', VENV_DIR])

pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
print('Instalando dependências...')
subprocess.check_call([pip_path, 'install', '-r', REQUIREMENTS])

python_path = os.path.join(VENV_DIR, 'bin', 'python')
print('Iniciando o servidor Flask (Ctrl+C para sair)...')
try:
    subprocess.check_call([python_path, APP_FILE])
except subprocess.CalledProcessError as e:
    print(f'Erro ao rodar o app: {e}')
finally:
    cleanup()