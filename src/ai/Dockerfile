FROM python:3.10-slim
WORKDIR /usr/src/ai
RUN apt-get update && apt-get install -y libgl1-mesa-glx ffmpeg
COPY capture_engine/ ./capture_engine/
RUN pip install opencv-python numpy
CMD ["python","-u","capture_engine/orchestrator.py"]
