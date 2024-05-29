from openai import OpenAI
import json
import os
from agents.helpers.list_to_bullet import list_to_bullet
from colorama import Fore, Style

def fix_prompt(
  current_prompt: str,
  improvements: list[str],
) -> str:
  """
  Fix prompt based on improvements.

  Paramters:
    current_prompt(str)
    improvements(list): list of improvements suggested by evaluation_agent
  
  Returns:
    str: Fixed prompt
  """

  agent_prompt: str = f"""
あなたは大規模言語モデルのプロンプトエンジニアです。
大規模言語モデルを使ったチャットシステムのシステムプロンプトを、指摘された改善点に基づいて、修正するのがあなたの仕事です。
修正されたシステムプロンプトは、言語モデルに対する「指示」である必要があります。言語モデルが実際のチャットの応答で返すような会話口調の表現は使わずに、客観的に書いてください。

システムプロンプト:
```
{current_prompt}
```

改善点
```
{list_to_bullet(improvements)}
```
  """

  print(Fore.LIGHTBLUE_EX + "*****プロンプト修正エージェント*****")
  print("現在のプロンプト:", current_prompt)
  print(f"""改善点:
{list_to_bullet(improvements)}""")

  client = OpenAI()

  response = client.chat.completions.create( #type: ignore
    model=os.environ.get("LLM_MODEL"),
    messages=[{"role": "system", "content": agent_prompt }],
    functions=[
      {
        "name": "fix_prompt",
        "description": "現在のプロンプトを改善点に基づいて修正する。修正内容は「指示」とする。",
        "parameters": {
          "type": "object",
          "properties": {
            "fixed_prompt": {
              "type": "string"
            }
          }
        }
      }
    ],
    function_call={ "name": "fix_prompt"},
    temperature=0
  )

  response_dump = response.model_dump(exclude_unset=True)

  response_message = response_dump["choices"][0]["message"] #type: ignore
  function_args = json.loads(response_message["function_call"]["arguments"]) #type: ignore
  fixed_prompt = function_args['fixed_prompt']
  print("↓\n修正されたプロンプト:", fixed_prompt, "\n")
  print(Style.RESET_ALL)

  return fixed_prompt
