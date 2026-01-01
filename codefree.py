import os
import sys
import time
import base64

CONFIG_FILE = 'config.txt'
CODES_FILE = 'codes.txt'
REASON_FILE = 'lost_codes_reason.txt'


def create_default_config():
    """Cria o arquivo config.txt base, se não existir."""
    if not os.path.isfile(CONFIG_FILE):
        print(f"Arquivo '{CONFIG_FILE}' não encontrado. Criando arquivo padrão...")
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            f.write("import codefree\n")
            f.write("code1 #escreva aqui\n")
        print(f"Arquivo '{CONFIG_FILE}' criado.\n")


def generate_codes_file():
    """Gera o arquivo codes.txt em base64 a partir do config.txt."""
    codes = {}

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('import'):
                continue
            parts = line.split(' ', 1)
            if len(parts) < 2:
                continue
            key_value = parts[1]
            if '=' not in key_value:
                continue
            name, func_part = key_value.split('=', 1)
            name = name.strip()
            func_part = func_part.strip()
            if func_part.startswith('function{') and func_part.endswith('}'):
                func_name = func_part[len('function{'):-1]
                codes[name] = func_name

    content = ''
    for name, func_name in codes.items():
        content += f'{name} is function"{func_name}"\n'

    encoded = base64.b64encode(content.encode('utf-8'))

    with open(CODES_FILE, 'wb') as f:
        f.write(encoded)
    print(f"Arquivo '{CODES_FILE}' gerado com sucesso a partir do '{CONFIG_FILE}'.\n")


def dramatic_message():
    """Mostra a mensagem dramática e melancólica."""
    lines = [
        "😔 ... 'codes.txt' desapareceu. O coração do programa está vazio.",
        "Sem ele, nada funciona. A essência se foi.",
        "Este arquivo não é só um pedaço de código; é a alma que move tudo.",
        "",
        "Se apagou por engano, não tema: é possível restaurar.",
        "Basta manter o arquivo 'config.txt' intacto — a fonte da verdade.",
        "",
        "Para restaurar, o programa tentará criar 'codes.txt' a partir do 'config.txt'.",
        "Se o 'config.txt' não existir, a restauração não será possível.",
        "",
        "Pense antes de agir. Cada arquivo tem seu valor.",
        "Pressione Enter para tentar restaurar e seguir em frente.",
        "Ou feche este programa e reflita sobre o vazio deixado para trás.",
    ]
    for line in lines:
        print(line)
        time.sleep(3)


def log_reason(reason):
    """Grava a resposta do usuário no arquivo de razões."""
    with open(REASON_FILE, 'a', encoding='utf-8') as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'Resposta em {timestamp}: {reason}\n')


def restore_codes():
    """Tenta restaurar o codes.txt a partir do config.txt."""
    if not os.path.isfile(CONFIG_FILE):
        return False

    try:
        codes = {}

        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('import'):
                    continue
                parts = line.split(' ', 1)
                if len(parts) < 2:
                    continue
                key_value = parts[1]
                if '=' not in key_value:
                    continue
                name, func_part = key_value.split('=', 1)
                name = name.strip()
                func_part = func_part.strip()
                if func_part.startswith('function{') and func_part.endswith('}'):
                    func_name = func_part[len('function{'):-1]
                    codes[name] = func_name

        content = ''
        for name, func_name in codes.items():
            content += f'{name} is function"{func_name}"\n'

        encoded = base64.b64encode(content.encode('utf-8'))

        with open(CODES_FILE, 'wb') as f:
            f.write(encoded)

        return True
    except Exception as e:
        print(f"Erro na restauração: {e}")
        return False


def check_codes_file():
    """Verifica se o codes.txt existe. Se não, mostra a mensagem melancólica e tenta restaurar."""
    if not os.path.isfile(CODES_FILE):
        dramatic_message()
        reason = input("\nPor favor, escreva algo para continuar: ")
        log_reason(reason)
        print("\nTentando restaurar o arquivo 'codes.txt'...")
        if restore_codes():
            print("\nRestaurado com sucesso! Reinicie o programa para continuar.")
        else:
            print("\nNão foi possível restaurar. Por favor, providencie o arquivo 'codes.txt' manualmente.")
        sys.exit(0)


def main():
    create_default_config()
    generate_codes_file()
    check_codes_file()
    print("Arquivo 'codes.txt' encontrado. O programa seguirá normalmente.\n")
    # Aqui você pode continuar com o resto do seu programa CodeFree


if __name__ == "__main__":
    main()
