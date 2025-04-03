import requests

# URL do webhook
url = "http://localhost:8101/webhook-test/d02bc081-c5e0-42e4-810a-b64c57ef6df5"

# Caminho para o arquivo PDF a ser enviado
pdf_path = "ATA AUD CONC - 2200353707.pdf"

# Abre o arquivo em modo binário e envia via POST
with open(pdf_path, "rb") as pdf_file:
    files = {"file": (pdf_path, pdf_file, "application/pdf")}
    response = requests.post(url, files=files)

# Exibe o status e o conteúdo da resposta
print("Status Code:", response.status_code)
print("Response Text:", response.text)
