# Reimportar as bibliotecas após o reset
import bcrypt
import time

# Gerar timestamp no formato Unix (segundos desde 1970)
timestamp = str(int(time.time()))  # Converte para string

# Concatenar a string com o timestamp
senha = f"mude-me{timestamp}".encode()  # Converte para bytes

# Gerar hash Bcrypt
hash_bcrypt = bcrypt.hashpw(senha, bcrypt.gensalt())

# Exibir hash gerado
print(hash_bcrypt.decode())
