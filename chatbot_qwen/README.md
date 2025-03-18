# chatbot_qwen
Create a Better Chatbot with Qwen + [Jan 27 2025 UPDATE] Deepseek 1.5B Qwen Chatbot

## Requirements
Download <a href="https://docs.docker.com/desktop/" target="_blank">Docker Desktop</a> and make sure the engine is running.

## Video Instructions
<a href="https://youtube.com/shorts/YWUvD6qe56g"><img src="https://github.com/user-attachments/assets/fa2fe923-4622-4e4d-9e01-a338e77afbc1" width="600px"></a>

## Run Qwen Instructions
1. clone this repository using WSL2 with<br>
```git clone https://github.com/MariyaSha/chatbot_qwen.git```
3. navigate there with<br>
```cd chatbot_qwen```
5. build Docker image with<br>
```docker build -t chatbot .```
7. run Docker container with<br>
```docker run -it --gpus=all chatbot```

## Run Deepseek 1.5 Qwen Adaptation
1. change in Dockerfile:
   from ```COPY main.py ./```
   to ```COPY main_deepseek.py ./```
3. repeat the Run Qwen Instructions from Above

## Credits
this tutorial is using the <a href="https://github.com/QwenLM/Qwen" target="_blank">Qwen Large Language Model</a>.
