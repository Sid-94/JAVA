import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# arquivos
#audio_mp3 = r'C:\Users\RSB\Videos\chico_buarque_joão_e_mari.mp3'
audio_wav = r'C:\Users\RSB\Videos\A_Cabritinha.wav'

# conversão de mp3 para wav
#sound = AudioSegment.from_mp3(audio_mp3)
#sound.export(audio_wav, format='wav')

# selecionando audio
audio = AudioSegment.from_file(audio_wav, 'wav')
# Tamanho em milisegundos
tamanho = 30000
# divisão do audio em partes
partes = make_chunks (audio, tamanho) 
partes_audio =[]
for i, parte in enumerate(partes):
    # Enumerando arquivo particionado
    parte_name = 'A{0}.wav'.format(i)
    # Guardando os nomes das partições em uma lista
    partes_audio.append(parte_name)
    # Exportando arquivos
    parte.export(parte_name, format='wav')
    
def transcreve_audio(nome_audio):
  # Selecione o audio para reconhecimento
  r = sr.Recognizer()
  with sr.AudioFile(nome_audio) as source:
    audio = r.record(source)  # leitura do arquivo de audio

  # Reconhecimento usando o Google Speech Recognition
  try:
    print('Google Speech Recognition: ' + r.recognize_google(audio,language='pt-BR'))
    texto = r.recognize_google(audio,language='pt-PT')
  except sr.UnknownValueError:
    print('Google Speech Recognition NÃO ENTENDEU o audio')
    texto = ''
  except sr.RequestError as e:
    print('Erro ao solicitar resultados do serviço Google Speech Recognition; {0}'.format(e))
    texto = ''
  return texto

texto = ''
for parte in partes_audio:
  texto = texto + ' ' + transcreve_audio(parte)