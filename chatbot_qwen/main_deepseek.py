from transformers import pipeline
import torch
from sty import fg

# set device to GPU if available
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
    
# set pipeline
pipe = pipeline(
    "text-generation", 
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", 
    device_map = device
)

def ask_question(message):
    # generate response
    response = pipe(
        message, 
        max_new_tokens = 2048
    )[0]['generated_text'][-1]["content"].split("</think>")
    
    think = response[0].strip().replace("<think>", "")
    say = response[1].strip()
    
    # display thinking in yellow
    print(fg.green + think + fg.rs)
       
    # display response in yellow
    print("\n" + fg.yellow + say + fg.rs)

message = [
    {
        "role": "system",
        "content": """
        You are a friendly chatbot named Chatty
        """
    },
    {
        "role": "user", 
        "content": """
        Please introduce yourself and add
        'how can I help you today?' at
        the end of the response
        """
    }
]

# ask introductory question
ask_question(message)

while True:
    # collect user input
    prompt = input("\nYour question:")
    # set user input as user message
    message[1]["content"] = prompt
    # stop loop if user types exit
    if prompt == "exit":
        break
    else:    
        # ask questions continuously
        ask_question(message)