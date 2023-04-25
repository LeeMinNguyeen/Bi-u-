import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.figure import Figure
from tkinter import filedialog

fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)

root = tk.Tk()
root.title("Đồ thị vui vẻ")

# Tạo đường kẻ trục x và y
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)

# Thêm nhãn cho trục x và y
ax.set_xlabel('x')
ax.set_ylabel('y')

# Tùy chỉnh vị trí của các nhãn trên trục x và y
ax.set_xticks(np.arange(-10, 11, 2))
ax.set_yticks(np.arange(-10, 11, 2))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(relx=0.001, rely= 0.00, relwidth = 0.5, relheight = 1)

# Tạo label với tiêu đề "Vẽ biểu đồ vui vẻ"
label = tk.Label(root, text="Đồ thị vui vẻ", fg = 'white', bg = '#48d1cc', font=("Cooper Black", 24, "bold"))
label.place(relx=0, rely= 0, relwidth = 0.5, relheight = 0.07)

# Tạo label tên nhóm
label = tk.Label(root, text="HAPPY WITH P", fg = '#48d1cc', bg = 'white', font=("Cooper Black", 24, "bold"))
label.place(relx=0.5, rely=0, relwidth = 0.5, relheight = 0.07)

root.configure(bg="#48d1cc")

# Tạo khung
frame = tk.LabelFrame(root, text="Đặt kích thước x và y", labelanchor="n", bg="#b0e0e6")

# Hiển thị khung
frame.place(relx=0.54, rely=0.16, relwidth=0.2, relheight=0.3)

# Tạo entry cho giá trị tối đa và tối thiểu của cột x và y
label_xmin = tk.Label(frame, text="x min:")
entry_xmin = tk.Entry(frame)
label_xmax = tk.Label(frame, text="x max:")
entry_xmax = tk.Entry(frame)
label_ymin = tk.Label(frame, text="y min:")
entry_ymin = tk.Entry(frame)
label_ymax = tk.Label(frame, text="y max:")
entry_ymax = tk.Entry(frame)

# Hiển thị entry cho giá trị tối đa và tối thiểu của cột x và y
label_xmin.grid(row=1, column=1, padx=10, pady=10)
entry_xmin.grid(row=1, column=15, padx=10, pady=10)
label_xmax.grid(row=2, column=1, padx=10, pady=10)
entry_xmax.grid(row=2, column=15, padx=10, pady=10)
label_ymin.grid(row=3, column=1, padx=10, pady=10)
entry_ymin.grid(row=3, column=15, padx=10, pady=10)
label_ymax.grid(row=4, column=1, padx=10, pady=10)
entry_ymax.grid(row=4, column=15, padx=10, pady=10)

# Hàm cập nhật giới hạn trục x và y
def update_limits():
    xmin = float(entry_xmin.get()) if entry_xmin.get() else None
    xmax = float(entry_xmax.get()) if entry_xmax.get() else None
    ymin = float(entry_ymin.get()) if entry_ymin.get() else None
    ymax = float(entry_ymax.get()) if entry_ymax.get() else None
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Vẽ lại đường kẻ trục x và y
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)

    # Cập nhật lại các nhãn trục x và y
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xticks(np.arange(xmin, xmax + 1, 2))
    ax.set_yticks(np.arange(ymin, ymax + 1, 2))

# Hàm số bậc nhất
def ham_so_bac_mot():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        x = np.linspace(-10, 10, 100)
        y = a * x + b
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")
 # Hàm số bậc hai
def ham_so_bac_hai():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        x = np.linspace(-10, 10, 100)
        y = a * x**2 + b * x + c
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Hàm số bậc ba
def ham_so_bac_ba():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        x = np.linspace(-10, 10, 100)
        y = a * x**3 + b * x**2 + c * x + d
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Hàm số logarit
def ham_so_logarit():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        x = np.linspace(-10, 10, 100)
        y = a * np.log(b * x)
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Hàm số lượng giác sin(x)
def ham_so_luong_giac_sinx():
    try:
        a = float(entry_a.get())
        x = np.linspace(-10, 10, 100)
        y = a * np.sin(x)
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")


# Hàm số lượng giác cos(x)
def ham_so_luong_giac_cosx():
    try:
        a = float(entry_a.get())
        x = np.linspace(-10, 10, 100)
        y = a * np.cos(x)
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Hàm số lượng giác tan(x)
def ham_so_luong_giac_tanx():
    try:
        a = float(entry_a.get())
        x = np.linspace(-10, 10, 100)
        y = a * np.tan(x)
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")


# Hàm số lượng giác cot(x)
def ham_so_luong_giac_cotx():
    try:
        a = float(entry_a.get())
        x = np.linspace(-10, 10, 100)
        y = a * np.cot(x)
        ax.axis('equal')
        ax.clear()
        update_limits()
        ax.plot(x, y)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Hàm số mũ
def ham_so_mu():
    try:
        a = float(entry_a.get())
        x = np.linspace(-10, 10, 100)
        y = a ** x
        ax.plot(x, y)
        ax.axis('equal')
        ax.clear()
        update_limits()
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Lỗi", "Vui lòng nhập vào một số thực")

# Tạo danh sách các chức năng
function_list = ["Hàm số bậc nhất", "Hàm số bậc hai", "Hàm số bậc ba",
                 "Hàm số Logarit", "Hàm số sin(x)", "Hàm số cos(x)",
                 "Hàm số tan(x)", "Hàm số cot(x)", "Hàm số mũ"]

# Tạo combobox và đặt giá trị mặc định
selected_function = tk.StringVar()
function_combobox = Combobox(root, values=function_list, textvariable=selected_function)
function_combobox.current(0)
function_combobox.place(relx=0.77, rely=0.16, relwidth=0.2, relheight=0.05)

# Định nghĩa hàm xử lý khi chọn chức năng từ danh sách
def select_function(event=None):
    if selected_function.get() == "Hàm số bậc nhất":
        # Hiển thị các label và entry cho hàm số bậc nhất
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        label_b.place(relx=0.77, rely=0.28, relwidth=0.05, relheight=0.04)
        entry_b.place(relx=0.83, rely=0.28, relwidth=0.05, relheight=0.04)

        # Ẩn các label và entry cho các hàm số khác
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số bậc hai":
        # Hiển thị các label và entry cho hàm số bậc hai
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        label_b.place(relx=0.77, rely=0.28, relwidth=0.05, relheight=0.04)
        entry_b.place(relx=0.83, rely=0.28, relwidth=0.05, relheight=0.04)
        label_c.place(relx=0.77, rely=0.33, relwidth=0.05, relheight=0.04)
        entry_c.place(relx=0.83, rely=0.33, relwidth=0.05, relheight=0.04)

        # Ẩn các label và entry cho các hàm số khác
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số bậc ba":
        # Hiển thị các label và entry cho hàm số bậc ba
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        label_b.place(relx=0.77, rely=0.28, relwidth=0.05, relheight=0.04)
        entry_b.place(relx=0.83, rely=0.28, relwidth=0.05, relheight=0.04)
        label_c.place(relx=0.77, rely=0.33, relwidth=0.05, relheight=0.04)
        entry_c.place(relx=0.83, rely=0.33, relwidth=0.05, relheight=0.04)
        label_d.place(relx=0.77, rely=0.38, relwidth=0.05, relheight=0.04)
        entry_d.place(relx=0.83, rely=0.38, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác

    elif selected_function.get() == "Hàm số Logarit":
        # Hiển thị các label và entry cho hàm số Logarit
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        label_b.place(relx=0.77, rely=0.28, relwidth=0.05, relheight=0.04)
        entry_b.place(relx=0.83, rely=0.28, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số sin(x)":
        # Hiển thị các label và entry cho hàm số lượng giác(sin(x))
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_b.place_forget()
        entry_b.place_forget()
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số cos(x)":
        # Hiển thị các label và entry cho hàm số lượng giác(cos(x))
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_b.place_forget()
        entry_b.place_forget()
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số tan(x)":
        # Hiển thị các label và entry cho hàm số lượng giác(tan(x))
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_b.place_forget()
        entry_b.place_forget()
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số cot(x)":
        # Hiển thị các label và entry cho hàm số lượng giác(cot(x))
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_b.place_forget()
        entry_b.place_forget()
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

    elif selected_function.get() == "Hàm số mũ":
        # Hiển thị các label và entry cho hàm số mũ
        label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
        entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)
        # Ẩn các label và entry cho các hàm số khác
        label_b.place_forget()
        entry_b.place_forget()
        label_c.place_forget()
        entry_c.place_forget()
        label_d.place_forget()
        entry_d.place_forget()

label_a = tk.Label(root, text="Hệ số a:", font=("Arial", 11, "italic"))
label_a.place(relx=0.77, rely=0.23, relwidth=0.05, relheight=0.04)
entry_a_var = tk.DoubleVar()
entry_a = tk.Entry(root, textvariable=entry_a_var)
entry_a.place(relx=0.83, rely=0.23, relwidth=0.05, relheight=0.04)

label_b = tk.Label(root, text="Hệ số b:", font=("Arial", 11, "italic"))
label_b.place(relx=0.77, rely=0.28, relwidth=0.05, relheight=0.04)
entry_b_var = tk.DoubleVar()
entry_b = tk.Entry(root, textvariable=entry_b_var)
entry_b.place(relx=0.83, rely=0.28, relwidth=0.05, relheight=0.04)

label_c = tk.Label(root, text="Hệ số c:", font=("Arial", 11, "italic"))
label_c.place(relx=0.77, rely=0.33, relwidth=0.05, relheight=0.04)
entry_c_var = tk.DoubleVar()
entry_c = tk.Entry(root, textvariable=entry_c_var)
entry_c.place(relx=0.83, rely=0.33, relwidth=0.05, relheight=0.04)

label_d = tk.Label(root, text="Hệ số d:", font=("Arial", 11, "italic"))
label_d.place(relx=0.77, rely=0.38, relwidth=0.05, relheight=0.04)
entry_d_var = tk.DoubleVar()
entry_d = tk.Entry(root, textvariable=entry_d_var)
entry_d.place(relx=0.83, rely=0.38, relwidth=0.05, relheight=0.04)

def show_graph():
    if selected_function.get() == "Hàm số bậc nhất":
        ham_so_bac_mot()
    elif selected_function.get() == "Hàm số bậc hai":
        ham_so_bac_hai()
    elif selected_function.get() == "Hàm số bậc ba":
        ham_so_bac_ba()
    elif selected_function.get() == "Hàm số Logarit":
        ham_so_logarit()
    elif selected_function.get() == "Hàm số sin(x)":
        ham_so_luong_giac_sinx()
    elif selected_function.get() == "Hàm số cos(x)":
        ham_so_luong_giac_cosx()
    elif selected_function.get() == "Hàm số tan(x)":
        ham_so_luong_giac_tanx()
    elif selected_function.get() == "Hàm số cot(x)":
        ham_so_luong_giac_cotx()
    elif selected_function.get() == "Hàm số mũ":
        ham_so_mu()

# Tạo Button Hiển thị đồ thị
button_show_graph = tk.Button(root, text="Hiển thị đồ thị", bg = 'blue', fg = 'white', command=show_graph)
button_show_graph.place(relx=0.57, rely=0.55, relwidth=0.08, relheight=0.05)

# Hàm xóa đồ thị
def clear_graph():
    result = tk.messagebox.askquestion("Xóa đồ thị", "Xác nhận xóa?")
    if result == "yes":
        ax.clear()
        update_limits()
        canvas.draw()

# Tạo button Xóa đồ thị
button_clear = tk.Button(root, text="Xóa đồ thị", bg = 'red', fg = 'white', command=clear_graph)
button_clear.place(relx=0.67, rely=0.55, relwidth=0.08, relheight=0.05)

# Tạo Combobox "Các tính năng khác"
other_features_cb = Combobox(root)

# Thiết lập các giá trị cho Combobox
other_features_cb["values"] = ["Tính năng khác", "Lưu biểu đồ", "Chọn màu Canvas", "Chọn màu đồ thị"]

# Thiết lập giá trị mặc định cho Combobox
other_features_cb.current(0)

# Hàm lưu biểu đồ
def save_figure():
    # Hiển thị hộp thoại chọn file để lưu
    file_path = filedialog.asksaveasfilename(defaultextension='.png')

    # Nếu người dùng đã chọn tên file
    if file_path:
        # Lưu biểu đồ với tên file được chọn
        fig.savefig(file_path)
        # Hiển thị thông báo đã lưu biểu đồ
        tk.messagebox.showinfo("Thông báo", "Đã lưu biểu đồ")

# Hàm thay đổi màu Canvas
def change_canvas_color():
    # Tạo bảng chọn màu
    color = colorchooser.askcolor(title="Chọn màu Canvas")
    # Nếu người dùng chọn màu
    if color[1] is not None:
        # Cập nhật màu nền của đồ thị
        fig.patch.set_facecolor(color[1])
        # Cập nhật màu nền của Canvas
        canvas.get_tk_widget().configure(bg=color[1])
        # Vẽ lại đồ thị
        canvas.draw()

# Hàm đổi màu đồ thị
def change_graph_color():
    color = colorchooser.askcolor(title="Chọn màu đồ thị")
    if color[1] is not None:
        normalized_color = tuple(map(lambda x: x / 255, color[0]))
        rgba_color = mcolors.to_rgba(normalized_color)
        ax.lines[-1].set_color(rgba_color)
        canvas.draw()

# Thiết lập sự kiện cho Combobox
other_features_cb.bind("<<ComboboxSelected>>", lambda event:
                       save_figure() if other_features_cb.current() == 1
                       else change_canvas_color() if other_features_cb.current() == 2
                       else change_graph_color() if other_features_cb.current() == 3
                       else None)

# Hiển thị Combobox
other_features_cb.place(relx=0.77, rely=0.55, relwidth=0.15, relheight=0.05)

# Hàm zoom out
def zoom_in():
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.set_xlim(xmin * 0.9, xmax * 0.9)
    ax.set_ylim(ymin * 0.9, ymax * 0.9)
    canvas.draw()

# Hàm zoom out
def zoom_out():
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.set_xlim(xmin / 0.9, xmax / 0.9)
    ax.set_ylim(ymin / 0.9, ymax / 0.9)
    canvas.draw()

# Tạo nút zoom im
btn_zoom_in = tk.Button(root, text=" + ", font=16, bg = 'gray', fg = 'white', command=zoom_in)
btn_zoom_in.place(relx=0.86, rely=0.94, relwidth=0.025, relheight=0.04)

# Tạo nút zoom out
btn_zoom_out = tk.Button(root, text=" - ", font=16, bg = 'gray', fg = 'white', command=zoom_out)
btn_zoom_out.place(relx=0.89, rely=0.94, relwidth=0.025, relheight=0.04)

root.mainloop()
