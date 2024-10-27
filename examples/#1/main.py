from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
import onnxruntime as ort
import numpy as np
import sounddevice as sd

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Text input für die Spracheingabe
        self.text_input = TextInput(hint_text="Geben Sie den Text ein...", multiline=False)
        self.layout.add_widget(self.text_input)
        
        # Button zur Sprachsynthese
        synth_button = Button(text="Sprachsynthese starten")
        synth_button.bind(on_press=self.open_file_chooser)
        self.layout.add_widget(synth_button)
        
        return self.layout

    def open_file_chooser(self, instance):
        filechooser = FileChooserListView()
        filechooser.bind(on_selection=self.load_onnx_model)
        self.layout.add_widget(filechooser)

    def load_onnx_model(self, filechooser, selection):
        if selection:
            model_path = selection[0]
            self.synthesize_speech(model_path)

    def synthesize_speech(self, model_path):
        text = self.text_input.text
        if text and model_path:
            print(f"Synthesizing: {text}")
            ort_session = ort.InferenceSession(model_path)
            
            # Placeholder input data for TTS model
            input_data = np.random.randn(1, 80).astype(np.float32)
            output_data = ort_session.run(None, {"input": input_data})[0]
            
            # Play the audio data
            sd.play(output_data[0], samplerate=22050)
            sd.wait()

if __name__ == "__main__":
    MainApp().run()
