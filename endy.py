import argparse
import subprocess
import os

parser = argparse.ArgumentParser()
parser.add_argument("command", nargs=argparse.REMAINDER, help="Comando a ejecutar")
args = parser.parse_args()

# Ejecuta el comando
p = subprocess.run(args.command)

# Mostrar notificación si el comando ha terminado con éxito
if p.returncode == 0:
    tool_name = args.command[0]
    sound_path = "/endy/complete.oga"
    os.system(f'notify-send --hint=string:sound-file:{sound_path} --hint=int:transient:1 "Ejecución de {tool_name} completada"')
else:
    print(f"Error: {p.stderr}")