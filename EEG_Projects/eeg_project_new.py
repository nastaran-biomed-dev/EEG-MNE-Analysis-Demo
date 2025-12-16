import mne
import numpy as np

# -----------------------------
# 1. Load data
# -----------------------------
# RAW_FNAME = "path/to/your/data.edf.edf" # Change this path when running locally
# print("NOTE: Data file path is currently commented out for GitHub push.")

print("Loading EEG data...")
raw = mne.io.read_raw_edf(RAW_FNAME, preload=True)
raw.pick("eeg")

# -----------------------------
# 2. Band-pass filter
# -----------------------------
raw.filter(0.5, 30)

# -----------------------------
# 3. Time-domain EEG (EEGLAB-like)
# -----------------------------
raw.plot(
    duration=10,        
    n_channels=20,     
    scalings='auto'
)


# -----------------------------
# 4. Frequency-domain (PSD)
# -----------------------------
raw.plot_psd(fmin=1, fmax=30)

input("Press ENTER to close...")
print("Done.")