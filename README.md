# flask_app_standard_logs_output
 A minimal Flask application configured to run on port 8080, with logs directed to standard output.

![image.png](/flask_app_standard_logs_output/img/image.png)

Certainly! Here's a minimal Flask application configured to run on port 8080, with logs directed to standard output. These logs can be captured on your AWS EC2nstance via a volume mapped to `/var/log`.

---

### 📁 Project Structure

```
flask_app/
├── app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

```

---

### 🐍 app.py

```python
from flask import Flask
import logging
import sys

app = Flask(__name__)

# Configure logging to output to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Accessed '/' route")
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

```

---

### 📦 requirements.txt

```
flask

```

---

### 🐳 Dockerfile

```



FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

```

---

### 🐙 docker-compose.yml

```yaml

version: '3.8'

```

---

### 🚀 Deployment Steps on AWS EC2

1. **Connect to Your EC2 Instance:**
    
    ```bash
    ssh -i your-key.pem ec2-user@your-ec2-ip
    
    ```
    
2. **Install Docker and Docker Compose:**
    
    ```bash
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    
    ```
    
3. **Clone Your Application Repository:**
    
    ```bash
    git clone https://github.com/your-repo/flask_app.git
    cd flask_app
    
    ```
    
4. **Build and Run the Application:**
    
    ```bash
    docker-compose up -d
    
    ```
    
5. **Access the Application:**
    
    Open your browser and navigate to `http://your-ec2-ip:8080`.
    
6. **Verify Logs on Host:**
    
    ```bash
    ls /var/log
    
    ```
    
    You should see Docker-generated log files corresponding to your container.
    

---

**Note:** Ensure that your EC2 security group allows inbound traffic on port 8080.

Let me know if you need further assistance or modifications!

Seu `Dockerfile` está perfeito para empacotar a aplicação Flask. Ele já está leve (`python:3.12-slim`) e eficiente. Sugestões opcionais:

1. **Evitar cache da layer COPY:** para mudanças em código não reexecutarem `pip install` desnecessariamente, inverta as cópias:

```
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

```

(que você já fez corretamente 👏)

1. **Adicionar `EXPOSE` para clareza (não obrigatório):**

```
EXPOSE 8080

```

1. **Verificar que o `requirements.txt` contém `flask`.**

Se quiser, posso revisar também o `app.py`. Deseja?

COM ISSO A VM DO APP ESTÁ OK!

1 - Adicionar esta VM no Load Balancer

2 - Fazer testes de acesso. 

3 - Subam quantos HelloWorld vcs quiserem. Pode subir mais de uma instancia na mesma vm em portas diferentes exemplo:

```bash

services:
  web:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - /var/log:/var/log
    logging:
      driver: "json-file"
      options:
        max-size: "10m"

  web2:
    build: .
    ports:
      - "8081:8080"
    volumes:
      - /var/log:/var/log
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

4 - Façam Mais testes. 

5 - Adicionem a estrutura do prof Leo: 

![image.png](Sem%20ti%CC%81tulo%201d7aa7b7018b802e9fb8d8c56fd08d66/image.png)

6 - Adicionem esta estrutura em scripts -Ansilble —> para que possa provisionar uma VM instantaneamente com esta estrutura. (podem começar pelo 6)