import mne
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Part 1: Generating Synthetic EEG Data ---

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

raw = mne.io.RawArray(data, info)

print(f"Synthetic data generated: {n_channels} channels, {sfreq} Hz, {raw.times[-1]:.2f} seconds.")

plots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plots')
os.makedirs(plots_dir, exist_ok=True) # Ensure the 'plots' directory exists

# --- Plotting Original Raw Data ---
print("\nPlotting original synthetic EEG raw data (first 5 seconds)...")
fig_raw = raw.plot(duration=5, n_channels=n_channels, scalings={'eeg': 50e-6}, title='Original Synthetic EEG Data (first 5s)', show=False)
fig_raw.savefig(os.path.join(plots_dir, '01_original_raw_data.png'))
plt.close(fig_raw)

print("\n--- Data Generation and Plotting Complete ---")

# --- Part 2: Analyzing Power Spectral Density (PSD) of original data ---

print("\n--- Analyzing Power Spectral Density (PSD) of original data ---")

# The .plot() method for BaseSpectrum (returned by compute_psd)
# does not accept 'ax' or 'title' in newer MNE versions.
# We plot it standalone and save.
fig_psd_original = raw.compute_psd(method='welch', fmax=sfreq/2, picks='eeg', verbose=False).plot(
    average=True, spatial_colors=False, exclude='bads',
    xscale='log', show=False
)
# Set title for this figure explicitly after plot call, if needed, before saving
fig_psd_original.suptitle('PSD of Original Synthetic EEG Data') # Using suptitle for the figure
fig_psd_original.savefig(os.path.join(plots_dir, '02_psd_original.png'))
plt.close(fig_psd_original)

print("\n--- PSD Analysis Complete ---")

# --- Part 3: Denoising and Filtering ---

print("\n--- Applying filtering to remove noise ---")

raw_filtered = raw.copy()

print(f"Applying Notch filter at {power_line_freq} Hz...")
raw_filtered.notch_filter(freqs=power_line_freq, picks='eeg', verbose=False)

f_low, f_high = 0.5, 40
print(f"Applying Band-pass filter ({f_low}-{f_high} Hz)...")
raw_filtered.filter(l_freq=f_low, h_freq=f_high, picks='eeg', verbose=False)

print("\n--- Filtering Complete ---")

# --- Part 4: Plotting filtered data and comparing PSDs ---

print("\n--- Plotting filtered EEG data and comparing PSDs ---")

fig_raw_filtered = raw_filtered.plot(duration=5, n_channels=n_channels, scalings={'eeg': 50e-6}, title='Filtered Synthetic EEG Data (first 5s)', show=False)
fig_raw_filtered.savefig(os.path.join(plots_dir, '03_filtered_raw_data.png'))
plt.close(fig_raw_filtered)

# For comparison plots, we need to get the axes from subplots first,
# then plot the PSDs to those axes using .plot(axes=...) on the PSD object.
# The previous direct .plot() on compute_psd() did not support 'ax'.
# Let's get the PSD objects first, then plot them.

# Get PSD objects
spectrum_original = raw.compute_psd(method='welch', fmax=sfreq/2, picks='eeg', verbose=False)
spectrum_filtered = raw_filtered.compute_psd(method='welch', fmax=sfreq/2, picks='eeg', verbose=False)


fig_comparison, axes = plt.subplots(1, 2, figsize=(15, 6), sharex=True, sharey=True)

# Plotting to specific axes for comparison
spectrum_original.plot(
    axes=axes[0], average=True, spatial_colors=False, exclude='bads',
    xscale='log', show=False
)
axes[0].set_title('PSD of Original Data') # Set title using axes object

spectrum_filtered.plot(
    axes=axes[1], average=True, spatial_colors=False, exclude='bads',
    xscale='log', show=False
)
axes[1].set_title('PSD of Filtered Data') # Set title using axes object


axes[0].set_ylabel('Power / Frequency (dB/Hz)')
axes[0].set_xlabel('Frequency (Hz)')
axes[1].set_xlabel('Frequency (Hz)')

plt.suptitle('Comparison of Power Spectral Density: Original vs. Filtered Data')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_comparison.savefig(os.path.join(plots_dir, '04_psd_comparison.png'))
plt.close(fig_comparison)


print("\n--- Project Complete! ---")
print(f"You have successfully generated synthetic EEG data, applied denoising filters, and saved the plots to the '{plots_dir}' directory.")
print("You can find the generated images in the 'plots' folder inside your project directory.")