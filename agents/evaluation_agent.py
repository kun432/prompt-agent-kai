from openai import OpenAI
import json
import os
from colorama import Fore, Style
from agents.helpers.list_to_bullet import list_to_bullet


def evaluate(
  output: str,
  desired_output: str,
) -> list[str]:
  """
  Evaluate output compared to desired output, and return a list of improvements

  Paramters:
    output(str)
    desired_output(str)
  
  Returns:
    list[str]: Improvments for desired output
  """

  agent_prompt: str = f"""
  現在の出力と理想の出力を比較して、現在の出力が理想の出力に近づくための改善点をリストアップしてください。

  現在の出力
  ```
  {output}
  ```

  理想の出力
  ```
  {desired_output}
  ```
  """

  print(Fore.GREEN + "*****評価エージェント*****")
  print("出力:", output)
  print("理想の出力:", desired_output)

  client = OpenAI()

  response = client.chat.completions.create( #type: ignore
    model=os.environ.get("LLM_MODEL"),
    messages=[{"role": "system", "content": agent_prompt }],
    functions=[
      {
        "name": "show_improvements",
        "description": "現在の出力と理想の出力を比較して、現在の出力が理想の出力に近づくための改善点を「客観的」にリストアップする。実際の応答例を使ってはいけない。",
        "parameters": {
          "type": "object",
          "properties": {
            "improvements": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      }
    ],
    function_call={ "name": "show_improvements"},
    temperature=0
  )
  response_dump = response.model_dump(exclude_unset=True)

  response_message = response_dump["choices"][0]["message"] #type: ignore
  function_args = json.loads(response_message["function_call"]["arguments"]) #type: ignore
  improvements = function_args["improvements"]
  print(f"""↓
改善点:
{list_to_bullet(improvements)}
""")
  print(Style.RESET_ALL)
  return improvements
