import librosa
import librosa.display
import matplotlib.pyplot as plt
import np as np

# 1. 读取音频文件（换成你自己的音频路径）
y, sr = librosa.load('your_audio_file.wav')

# 2. 显示音频波形
plt.figure(figsize=(10, 4))
librosa.display.waveplot(y, sr=sr)
plt.title('Waveform')
plt.show()

# 3. 计算MFCC特征（13维）
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print("MFCCs shape:", mfccs.shape)

# 4. 显示MFCC特征图
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()

# 5. 计算节奏（BPM）
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
print(f"Estimated tempo: {tempo} BPM")

# 6. 提取MFCC的均值作为简单特征向量
mfccs_mean = np.mean(mfccs, axis=1)
print("MFCC mean vector:", mfccs_mean)