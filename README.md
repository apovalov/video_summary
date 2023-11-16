# Video summary

The task can be formulated as generating a text description or summarizing a video.

The input is a video on the YouTube platform. The output is a clear text description of what the video is about.


Libraries for working with video: First, extract the audio track from the video using specialized libraries.
Whisper for audio transcription: Using the Whisper library, convert the audio into text form.
Chat GPT API for generating a description: With the resulting text, we turn to the Chat GPT API to generate a short and informative description of the video.
Streamlit for interface generation: Finally, let's create a user interface for our solution using the Streamlit tool.
