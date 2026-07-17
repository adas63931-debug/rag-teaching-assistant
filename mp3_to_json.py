import os
import whisper
import json

model = whisper.load_model("large-v2")

audios = os.listdir("audios")

for audio in audios:
    

    if "_" in audio:
        number = audio.split("_")[5]
        title = audio.split("_")[4][:-4]
    else:
        number = "Unknown"
        title = os.path.splitext(audio)[0]

    print(number, title)
    result = model.transcribe(audio = f"audios/{audio}",
    # result = model.transcribe(audio = f"audios/output.mp3",
                            task = "translate",
                            word_timestamps=False 
                            )
    
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number": number, "title":title, "start":segment["start"], "end":segment["end"], "text":segment["text"]})

    
    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata,f)


