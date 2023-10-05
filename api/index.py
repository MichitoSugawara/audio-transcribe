# import os
# import uuid
from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import JSONResponse
# import whisperx
# from datetime import timedelta
# from tqdm import tqdm

app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/api/hello")
async def hello():
    return {"message": "Hello World"}

# @app.post("/api/upload")
# async def upload_data(audio: UploadFile = File(...)):
#     _, extension = os.path.splitext(audio.filename)
#     # 取得したデータを保存したり、処理したりすることができます。
#     # 例として音声データだけを保存するコードを示します。
#     filepath = f"uploaded_files/{uuid.uuid4()}{extension}"
#     with open(filepath, "wb") as f:
#         f.write(audio.file.read())
#     try:
#         result = transcribe(filepath, 2, 2)
#     except Exception as e:
#         raise e
#     finally:
#         os.remove(filepath)
#     print(result)
#     return JSONResponse(content=result)

# def transcribe(audio_file: str, min_speakers: int|None = None, max_speakers: int|None = None):
#     device ="cpu"
#     batch_size = 8 # GPUメモリが不足している場合は減らす
#     compute_type = "int8" # GPUメモリが少ない場合は "int8"に変更する（精度が落ちる可能性がある）

#     model = whisperx.load_model("large-v2", device, compute_type=compute_type, language="ja")
#     audio = whisperx.load_audio(audio_file)
#     result = model.transcribe(audio, batch_size=batch_size, language="ja")

#     model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
#     result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
#     diarize_model = whisperx.DiarizationPipeline("pyannote/speaker-diarization-3.0", use_auth_token="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", device=device)
#     diarize_segments = diarize_model(audio_file, min_speakers=min_speakers, max_speakers=max_speakers)
#     result = whisperx.assign_word_speakers(diarize_segments, result)

#     segment_array = []
#     speaker_array = []
#     for segment in tqdm(result["segments"], desc="Processing segments"):
#         segment_dict = {
#             # "start_time": str(timedelta(seconds=segment["start"])),
#             # "end_time": str(timedelta(seconds=segment["end"])),
#             "speaker": segment["speaker"],
#             "text": segment["text"]
#             }
#         segment_array.append(segment_dict)
        
#         if not(segment["speaker"] in speaker_array): speaker_array.append(segment["speaker"])
        
        
#     return {
#         "segments": segment_array,
#         "speakers": speaker_array
#     }