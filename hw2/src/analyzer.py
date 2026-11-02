import parselmouth
import numpy as np

class AudioAnalyzer:
    def __init__(self, file_path, time_step=0.01, f0_min=75, f0_max=500, formant_max=5000, relax=False):
        self.file_path = file_path
        self.time_step = time_step
        if relax:
            self.f0_min = f0_min * 0.7
            self.f0_max = f0_max * 1.5
        else:
            self.f0_min = f0_min
            self.f0_max = f0_max
        self.formant_max = formant_max

        self.snd = parselmouth.Sound(file_path)
        self.pitch = self.snd.to_pitch(self.time_step, self.f0_min, self.f0_max)
        self.f0_values = self.pitch.selected_array["frequency"]
        self.voiced_indices = self.f0_values > 0
        self.voiced_timestamp = self.pitch.xs()[self.voiced_indices]


    def get_f0_f1_f2(self):
        f0 = self.get_pitch()
        f1, f2 = self.get_formants()
        return f0, f1, f2

    def get_pitch(self, return_std=False):
        voiced_f0_values = self.f0_values[self.voiced_indices]
        if return_std:
            return np.median(voiced_f0_values), np.std(voiced_f0_values)
        return np.median(voiced_f0_values)
    
    def get_formants(self):
        formant = self.snd.to_formant_burg(self.time_step, 5, self.formant_max, 0.025, 50)
        f1 = []
        f2 = []
        for t in self.voiced_timestamp:
            f1.append(formant.get_value_at_time(1, t))
            f2.append(formant.get_value_at_time(2, t))
        f1 = np.array(f1)
        f2 = np.array(f2)
        return np.median(f1), np.median(f2)

    def get_duration(self):
        return self.snd.xmax - self.snd.xmin