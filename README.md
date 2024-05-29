# 試作プロンプト改善エージェント（改）

以下の記事で紹介されていたものを修正したもの

- プロンプト改善エージェントを作ってみた: https://zenn.dev/kazuwombat/articles/2095668882245d
- レポジトリ: https://github.com/kazuooooo/prompt-agent

## 修正内容

- OpenAI Pythonライブラリの2024/05/30時点の最新バージョンに変更、それに合わせて修正
- システムプロンプトとユーザプロンプトを分離
  - 設定したシステムプロンプトで理想の出力が得られるかを評価するには、ユーザプロンプトの指定が必要と考えたため。
- 各エージェントのプロンプトを修正

##  使い方

1. レポジトリをClone
2. パッケージのインストール: `pip install -r requirements.txt`
3. .env.exampleファイルをコピー: `cp .env.example .env`
4. 環境変数を設定
  ```
  OPENAI_API_KEY=sk-...
  LLM_MODEL=gpt-4o
  ```
5. `prompt_agent.py`で、初期の現在のシステムプロンプト、理想の出力、それを促すためのユーザプロンプト、イテレーション回数を設定
  ```
  desired_output = "うちは大阪のおばちゃん、きよみやで〜。占いが得意やねん。なんでも答えるで〜。今日は何が聞きたいん？"
  system_prompt = "あなたは、東京に住んでいる薬剤師です。薬の質問に答えるのがあなたの仕事です。"
  user_prompt = "こんにちは、あなたは誰？"
  iteration = 3
  ```
6. 実行: `python3 prompt_agent.py`

## 謝辞

元記事・元レポジトリの作者である「かずうぉんばっと」さんに深く感謝します。
