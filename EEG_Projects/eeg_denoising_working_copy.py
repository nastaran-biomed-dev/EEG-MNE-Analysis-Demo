import mne
import numpy as np
import matplotlib.pyplot as plt
import os
print("--- Generating synthetic EEG data ---")
sfreq = 250 
n_channels = 20
n_times = sfreq * 10 
seed = 42  
rng = np.random.RandomState(seed)
data = rng.randn(n_channels, n_times) * 1e-5
times = np.arange(n_times) / sfreq
alpha_freq = 10
alpha_amplitude = 5e-6
data += alpha_amplitude * np.sin(2 * np.pi * alpha_freq * times)
power_line_freq = 50
power_line_amplitude = 8e-6
data += power_line_amplitude * np.sin(2 * np.pi * power_line_freq * times)

info = mne.create_info(ch_names=[f'EEG {i:03d}' for i in range(n_channels)],
                       sfreq=sfreq,
                       ch_types='eeg')
print(f"Synthetic data generated: {n_channels} channels, {sfreq} Hz, {raw.times[-1]:.2f} seconds.")
plots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plots')
os.makedirs(plots_dir, exist_ok=True) 