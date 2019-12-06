import pyttsx3

try:
    from PIL import Image
except ImportError:
    import Image
	
import pytesseract


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
	
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

txt = ocr_core('tex1.png')
print(txt)
speak(txt)	
#speak("Good Morning!")
