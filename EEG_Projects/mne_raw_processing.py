import mne
import os

print("--- Step 1: Loading Raw Data for Processing ---")

try:

    data_root = mne.datasets.sample.data_path()
    sample_data_folder = os.path.join(data_root, 'MEG', 'sample')
    fif_file_path = os.path.join(sample_data_folder, 'sample_audvis_raw.fif')

    print(f"\nAttempting to load Raw data from: {fif_file_path}")

  
    raw = mne.io.read_raw_fif(fif_file_path, preload=True, verbose=False)
    print("Raw data loaded successfully!")


    print("\n--- Raw Info (Initial) ---")
    print(raw)
    print(f"Sampling frequency: {raw.info['sfreq']} Hz")
    print(f"Number of channels: {len(raw.ch_names)}")
    print(f"Duration: {raw.n_times / raw.info['sfreq']:.2f} seconds")

    

    print("\nRaw data is now loaded and ready for the next processing steps!")

    

except FileNotFoundError:
    print(f"\nError: The file {fif_file_path} was not found.")
    print("Please make sure the 'sample' dataset is downloaded correctly by MNE.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("Please ensure MNE is correctly installed.")

print("\n--- Data Loading Process Complete ---")