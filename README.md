# EEG Signal Analysis and Denoising Demo (MNE-Python)

This repository demonstrates advanced EEG signal processing workflows using the **MNE-Python** framework. It covers a full pipeline from synthetic data generation and noise simulation to real-world clinical data processing.

##  Key Features
* **Synthetic Signal Generation:** Creating realistic EEG data with embedded alpha rhythms and power-line interference.
* **Artifact Removal:** Implementing Notch and Band-pass filters to clean corrupted signals.
* **Clinical Data Processing:** Handling real-world brainwave recordings in `.edf` and `.fif` formats.
* **Spectral Analysis:** Visualization of Power Spectral Density (PSD) to validate denoising efficiency.

##  Project Structure
* `eeg_denoising.py`: The core script for synthetic data generation and digital filtering.
* `eeg_project_new.py`: A module dedicated to processing clinical `.edf` data files.
* `mne_raw_processing.py`: Utilization of standard MNE datasets for technical info extraction.
* `plots/`: Comprehensive visual results showcasing the signal before and after processing.

## Visual Analysis (Results)
The following plots (located in the `plots/` directory) illustrate the denoising performance:

### 1. Original Raw Data
Displays the initial synthetic EEG signal corrupted with 50Hz power-line noise and random artifacts.

### 2. PSD of Original Data
The Power Spectral Density plot reveals a sharp, unwanted peak at 50Hz, indicating significant electrical interference.

### 3. Filtered Raw Data
The time-domain signal after applying a **Notch filter** (at 50Hz) and a **Band-pass filter** (0.5–40Hz). The signal is now smooth and clear.

### 4. PSD Comparison (Original vs. Filtered)
A side-by-side spectral comparison. It shows the successful elimination of the 50Hz noise spike and the preservation of essential frequency bands.

## 🛠 Prerequisites
Install the required dependencies using:
```bash
pip install -r requirements.txt
