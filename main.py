from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import onnxruntime as ort
import numpy as np
import sounddevice as sd

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Text input für die Spracheingabe
        self.text_input = TextInput(hint_text="Geben Sie den Text ein...", multiline=False)
        layout.add_widget(self.text_input)
        
        # Button zur Sprachsynthese
        synth_button = Button(text="Sprachsynthese starten")
        synth_button.bind(on_press=self.synthesize_speech)
        layout.add_widget(synth_button)
        
        return layout

    def synthesize_speech(self, instance):
        text = self.text_input.text
        if text:
            print(f"Synthesizing: {text}")
            # Lade das ONNX-Modell
            model_path = "assets/models/tts_model.onnx"
            ort_session = ort.InferenceSession(model_path)
            
            # Hier konvertieren wir den Text zu Sprachdaten (Platzhalter für ein echtes Modell)
            input_data = np.random.randn(1, 80).astype(np.float32)  # Beispielinput für ein TTS-Modell
            output_data = ort_session.run(None, {"input": input_data})[0]
            
            # Wiedergabe der Audiodaten (platzhalterweise Zufallsdaten)
            sd.play(output_data[0], samplerate=22050)
            sd.wait()

if __name__ == "__main__":
    MainApp().run()
