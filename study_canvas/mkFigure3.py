# いちばんやさしいPython入門教室
# クリックしたところに円を移動する
# coding:utf-8

import tkinter as tk

# 円の座標
x = 300
y = 200

def click(event):
    # global宣言をすることで、関数外で定義した変数に代入した値を変更できる
    global x, y
    # いまの円を消す
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white", width=0)
    x = event.x
    print(x)
    y = event.y
    canvas.create_oval(x - 20, y -20, x + 20, y + 20, fill="red", width=0)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)
canvas.bind("<Button-1>",click)

root.mainloop()