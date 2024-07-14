
from transformers import pipeline
from gtts import gTTS
import io

class NLUModule:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.ner_pipeline = pipeline("ner", grouped_entities=True)
        self.qa_pipeline = pipeline("question-answering")
        self.summarization_pipeline = pipeline("summarization")
        self.translation_pipeline = pipeline("translation_en_to_fr")
        
    def process(self, text, task="sentiment", **kwargs):
        try:
            if task == "sentiment":
                analysis = self.sentiment_pipeline(text)
            elif task == "ner":
                analysis = self.ner_pipeline(text)
            elif task == "qa":
                context = kwargs.get("context", "")
                question = kwargs.get("question", text)
                analysis = self.qa_pipeline(question=question, context=context)
            elif task == "summarization":
                analysis = self.summarization_pipeline(text, max_length=50, min_length=25, do_sample=False)
            elif task == "translation":
                analysis = self.translation_pipeline(text)
            else:
                analysis = {"error": "Unsupported task"}
            return analysis
        except Exception as e:
            return {"error": str(e)}

class TTSModule:
    def convert(self, text, lang="en", slow=False):
        try:
            tts = gTTS(text, lang=lang, slow=slow)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            audio_signal = fp.read()
            return audio_signal
        except Exception as e:
            return {"error": str(e)}
