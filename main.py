
from core_framework import MultimodalSNN
from nlu_tts_modules import NLUModule, TTSModule
from servo_control_module import ServoControlModule

def main():
    snn = MultimodalSNN(initial_neurons=100)
    nlu_module = NLUModule()
    tts_module = TTSModule()
    servo_control_module = ServoControlModule(port='/dev/ttyUSB0', baudrate=9600)

    snn.set_modules(nlu_module, tts_module, servo_control_module)
    snn.train(iterations=1000)

    # Handling inputs for NLU, TTS, and Servo Control
    sentiment_result = snn.handle_input('nlu', 'Hello, how are you?', task='sentiment')
    qa_result = snn.handle_input('nlu', {'text': 'Who is the president of the United States?', 'task': 'qa', 'context': 'Joe Biden is the president of the United States.'})
    audio_data = snn.handle_input('tts', 'This is a test.', lang='en', slow=False)
    
    with open('test_audio.mp3', 'wb') as f:
        f.write(audio_data)
    
    servo_response = snn.handle_input('servo', {'servo_1': 90, 'servo_2': 45})

    # Print results
    print("Sentiment Analysis Result:", sentiment_result)
    print("Question Answering Result:", qa_result)
    print("Servo Control Response:", servo_response)

    # Close the serial connection
    servo_control_module.close()

if __name__ == "__main__":
    main()
