import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# 1. 读取音频
y, sr = librosa.load("236014__delphidebrain__jazz-the-dog-howl-bark-137.wav", sr=None)  # sr=None 保持原采样率

# 2. 设置窗口长度和步长
n_fft = 2048       # 每段做傅里叶变换长度
hop_length = 512   # 窗口移动步长

# 3. 做 STFT，得到复数频谱
D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)

# 4. 转成幅度谱（Magnitude Spectrum）
magnitude = np.abs(D)

# 5. 可视化频谱
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(magnitude, ref=np.max),
                         sr=sr, hop_length=hop_length, y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title("6 second voice")
plt.tight_layout()
plt.show()
