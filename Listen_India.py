import moviepy.editor as mp
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from moviepy.editor import VideoFileClip, AudioFileClip

# def Extrect_Audio_From_Video(video_file):
import sys

try:
    print(sys.argv[1])
except:
    print('error in video direc')
videodir = sys.argv[1]

video = mp.VideoFileClip(videodir)

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("test.wav")

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("test.wav") as source:
    data = r.record(source)
    text = r.recognize_google(data)

def translate_to_other_language(text,destination):
    translator = Translator()
    print("sfsdfsdf    ",text)
    translated_text = translator.translate(text, src='en', dest=destination)
    print(translated_text)
    return translated_text.text

def attach_audio_to_video(video_path, audio_path, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Load audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set audio of the video clip
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the result to a new file
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)

languages = ['hi','bn',"gu","ta","kn","mr"]

for every_lng in languages:
    text_lng = translate_to_other_language(text,every_lng)
    obj_lng = gTTS(text = text_lng, lang =every_lng)
    obj_lng.save('/home/ravish/Desktop/Listen_India/output_voice/'+str(every_lng)+r".mp3")

    if every_lng == 'hi' or every_lng == 'bn':
        attach_audio_to_video(videodir, '/home/ravish/Desktop/Listen_India/output_voice/'+str(every_lng)+r".mp3", '/home/ravish/Desktop/Listen_India/output_video/'+str(every_lng)+'outvideo.mp4')