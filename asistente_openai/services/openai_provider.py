from openai import OpenAI


class OpenAIProvider:
    def __init__(self, api_key, model):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generar_texto(self, instrucciones, entrada_usuario):
        response = self.client.responses.create(
            model=self.model,
            instructions=instrucciones,
            input=entrada_usuario
        )

        return response.output_text