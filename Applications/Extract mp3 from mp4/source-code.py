import os
import moviepy.editor as mpy
from typing import Optional


def extract_mp3(input_path: str, output_path: Optional[str] = None) -> None:
	"""Extract audio from `input_path` video and write to `output_path` (defaults to input name + .mp3).

	Raises ValueError if `input_path` doesn't exist.
	"""
	if not os.path.exists(input_path):
		raise ValueError(f"Input file does not exist: {input_path}")

	if output_path is None:
		base, _ = os.path.splitext(input_path)
		output_path = f"{base}.mp3"

	video = mpy.VideoFileClip(input_path)
	audio = video.audio
	audio.write_audiofile(output_path)


def main():
	try:
		input_path = input("Enter path to video file: ").strip()
	except (EOFError, KeyboardInterrupt):
		print("No input provided. Exiting.")
		return

	try:
		extract_mp3(input_path)
		print("Audio extracted successfully.")
	except Exception as exc:
		print("Failed to extract audio:", exc)


if __name__ == "__main__":
	main()

