import os
import parselmouth
import numpy as np
from parselmouth.praat import call

class AudioModifier: # using PSOLA
    def __init__(self, audio_path, time_step=0.01, f0_min=75, f0_max=500):
        self.input_name = os.path.basename(audio_path).split(".")[0]
        self.snd = parselmouth.Sound(audio_path)
        self.time_step = time_step
        self.f0_min = f0_min
        self.f0_max = f0_max

    def create_manipulation(self):
        return call(self.snd, "To Manipulation", self.time_step, self.f0_min, self.f0_max)

    def apply_effect(self, effect):
        effect_type, factor = effect
        if effect_type == "pitch":
            return self.modify_pitch(factor)
        elif effect_type == "duration":
            return self.modify_duration(factor)
        elif effect_type == "monotone":
            return self.modify_monotone()
        else:
            raise ValueError(f"Unknown effect type: {effect_type}")
        
    def modify_pitch(self, ratio):
        # ratio = pitch after / pitch before
        m = self.create_manipulation()
        pt = call(m, "Extract pitch tier")
        call(pt, "Multiply frequencies", self.snd.xmin, self.snd.xmax, ratio)
        call([pt, m], "Replace pitch tier")
        new = call(m, "Get resynthesis (overlap-add)")
        return new

    def modify_duration(self, ratio):
        # ratio = duration after / duration before
        m = self.create_manipulation()
        dt = call(m, "Extract duration tier")
        call(dt, "Add point", self.snd.xmin + 0.001, ratio)
        call([dt, m], "Replace duration tier")
        new = call(m, "Get resynthesis (overlap-add)")
        return new

    def modify_monotone(self):
        m = self.create_manipulation()
        pitch = self.snd.to_pitch(self.time_step, self.f0_min, self.f0_max)
        f0_values = pitch.selected_array["frequency"]
        median_f0 = np.median(f0_values[f0_values > 0])

        flat = call("Create PitchTier", "flat", self.snd.xmin, self.snd.xmax)
        call(flat, "Add point", self.snd.xmin, median_f0)
        call([flat, m], "Replace pitch tier")
        new = call(m, "Get resynthesis (overlap-add)")
        return new
