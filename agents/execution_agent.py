from openai import OpenAI
import os
from colorama import Fore, Style

def execute(
  system_prompt: str,
  user_prompt: str
) -> str:
  """
  Execute a prompt and return the output

  Paramters:
    system_propmt: str
    user_propmt: str
  
  Returns:
    str: output of the fixed prompt
  """

  print(Fore.RED + "*****実行エージェント*****")
  print("システムプロンプト:", system_prompt)
  print("ユーザプロンプト:", user_prompt)

  client = OpenAI()

  response = client.chat.completions.create( #type: ignore
    model=os.environ.get("LLM_MODEL"),
    messages=[
      {"role": "system", "content": system_prompt },
      {"role": "user", "content": user_prompt },
    ],
    temperature=0
  )
  output = response.choices[0].message.content #type: ignore
  print("↓\n出力:", output) #type: ignore
  print(Style.RESET_ALL)
  return output #type: ignore
