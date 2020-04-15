import librosa
import librosa.display
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from lib import plot_wave_composition
SAMPLING_RATE=16000

# path_to_file="output.wav"
path_to_file="LibriSpeech/train-clean-360/14/208/14-208-0000.flac"

# wave, _ = librosa.load(path_to_file, sr=SAMPLING_RATE)
# librosa.display.waveplot(wave, sr=SAMPLING_RATE)
# sns.lineplot(data=gen_sin(3, 1))

wave_defs = [
    (3, 1)
        # (2, 1),
        # (3, 0.8),
        # (5, 0.2),
        # (7, 0.1),
        # (9, 0.25)
    ]
waves, the_sum = plot_wave_composition(wave_defs)

ffts = np.fft.fft(the_sum)
freqs = np.fft.fftfreq(len(the_sum))

frequencies, coeffs = zip(
    *list(
        filter(
            lambda row: row[1] > 10, # arbitrary threshold but let’s not make it too complex for now
            [ (int(abs(freq * 1000)), coef) for freq, coef in zip(freqs[0:(len(ffts) // 2)], np.abs(ffts)[0:(len(ffts) // 2)]) ]
        )
    )
)

sns.barplot(x=list(frequencies), y=coeffs)

plt.show()