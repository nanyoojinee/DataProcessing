from openai import Completion

api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    print("API 키를 찾을 수 없습니다.")
else:
    # OpenAI 객체를 만들어서 사용합니다.
    openai.api_key = api_key

    # Chat Completions API를 사용하여 응답을 얻습니다.
    response = Completion.create(
        model="gpt-3.5-turbo",
        prompt="Who won the world series in 2020?",
        temperature=0.7,
        max_tokens=150
    )

    print(f'A: {response["choices"][0]["text"]}')
