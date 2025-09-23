import sounddevice
from scipy.io.wavfile import write


def record(duration_seconds=None, out_file='out.wav', fs=44100):
	"""Record audio for the given duration (seconds) and write to out_file."""
	if duration_seconds is None:
		try:
			duration_seconds = int(input("Enter the time duration in second: "))
		except ValueError:
			print("Invalid duration; using 5 seconds as default.")
			duration_seconds = 5

	if duration_seconds <= 0:
		print("Duration must be positive; using 5 seconds.")
		duration_seconds = 5

	print("Recording....\n")
	record_voice = sounddevice.rec(int(duration_seconds * fs), samplerate=fs, channels=2)
	sounddevice.wait()
	write(out_file, fs, record_voice)
	print(f"Finished...\nSaved to {out_file}")


if __name__ == '__main__':
	record()
