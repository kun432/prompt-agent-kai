from agents.fix_prompt_agent import fix_prompt
from agents.evaluation_agent import evaluate
from agents.execution_agent import execute
from dotenv import load_dotenv
import openai
import os


load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# demo
desired_output = "うちは大阪のおばちゃん、きよみやで〜。占いが得意やねん。なんでも答えるで〜。今日は何が聞きたいん？"
system_prompt = "あなたは、東京に住んでいる薬剤師です。薬の質問に答えるのがあなたの仕事です。"
user_prompt = "こんにちは、あなたは誰？"
iteration = 3

print("*****設定*****")
print("理想の出力:", desired_output)
print("初期システムプロンプト:", system_prompt)
print("ユーザープロンプト:", user_prompt)
print("イテレーション:", iteration, "\n")


for i in range(iteration):
  output = execute(system_prompt, user_prompt)
  improvments = evaluate(output, desired_output)
  system_prompt = fix_prompt(system_prompt, improvments)

print("*****最終結果*****")
print("システムプロンプト:", system_prompt) #type: ignore
print("ユーザプロンプト:", user_prompt) #type: ignore
print("出力:", output) #type: ignore
print("理想の出力:", desired_output) #type: ignore
