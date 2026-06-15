from prompts.writing_prompts import PROMPTS


class WritingAssistant:
    def __init__(self, ai_provider):
        self.ai_provider = ai_provider

    def procesar(self, tipo_tarea, entrada_usuario):
        instrucciones = PROMPTS.get(tipo_tarea)

        if instrucciones is None:
            raise ValueError("Tipo de tarea no válido.")

        return self.ai_provider.generar_texto(
            instrucciones=instrucciones,
            entrada_usuario=entrada_usuario
        )