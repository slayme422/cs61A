import tkinter as tk
from tkinter import messagebox
class Music:
    all=[]
    def __init__(self,name,singer_name,length,music_type):
        """音乐分类成 name:革命,singer_name:歌手名字,length:歌曲时长,type:音乐种类"""
        self.name=name
        self.singer_name=singer_name
        self.length=length
        self.music_type=music_type
        Music.all.append(self)
    def similar(self, k, similarity):
        """返回k个与SELF相似的列表"""
        others=[song for song in Music.all if self!=song]
        others.sort(key=lambda s:abs(similarity(self)-similarity(s)))
        return others[:k]
    def __repr__(self):
        return f"Song🎵:<{self.name}>, Artist🧑: <{self.singer_name}>"
    
m1=Music("CRG","Central Cee",192,"Rap")
m2=Music("Passionfruit","Drake",299,"Rap")
m3=Music("Two Can Win","J Dilla",107,"Rap")
current=m1

 # GUI部分
root = tk.Tk()
root.title("音乐匹配器")

info = tk.Label(root, text=f"{current.name} by {current.singer_name}\nLength: {current.length} min\nType: {current.music_type}")
info.pack()

def show_similar():
    result = current.similar(2, lambda m: len(m.music_type))
    names = "\n".join([f"{i+1}. {m.name}" for i, m in enumerate(result)])
    messagebox.showinfo("推荐结果", names)

btn = tk.Button(root, text="推荐相似音乐", command=show_similar)
btn.pack()

root.mainloop()