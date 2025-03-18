from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import torch
from sty import fg

# set device to GPU if available
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# Quantization:
# ---------------------------------
# Reduce the precision of the model
# So it runs on less memory
# ---------------------------------
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

# Choose model
model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"

# Set text generation pipeline
pipe = pipeline(
    "text-generation", 
    model=model_id, 
    model_kwargs={"quantization_config": quantization_config}
)

# Ask question function
def ask_question(message):
    """
    generate and print model response to the console
    - thinking component printed in yellow
    - response in green
    """
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

# Set model role and initial prompt
message = [
    {
        "role": "system",
        "content": """
        You are a friendly chatbot named Llama
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

# Process initial prompt
ask_question(message)

# Collect user input continuously
while True:
    # collect user input
    prompt = input("\nYour question:")
    # set user input as user message
    message[1]["content"] = prompt
    
    if prompt == "exit":
        # stop loop if user types exit
        break
    else:    
        ask_question(message)