import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk
import random,csv

def getfile():
    
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
         cur_filename.set(filename)
    else:
         cur_filename.set('您没有选择任何文件')

root_window = tk.Tk()
root_window.title('随机美食')
root_window.geometry('500x300')
root_window.iconbitmap('美食.ico')
root_window.resizable(0,0)
root_window.config(bg='#FFE4E1')
time_cbox = ttk.Combobox(root_window)
time_cbox['value'] = ('早饭','午饭','晚饭')
time_cbox.current(0)    

def random_select():
    n = int(number_entry.get()) 
    namelist = []
    with open(cur_filename.get()) as fp:
        csv_reader = csv.reader(fp)
        next(csv_reader)
        for row in csv_reader:
            namelist.append(row[0])
    if n == 1:
        food_name = random.choice(namelist)
        result_txt = '今天吃：'+food_name
    else:
        food_name = random.sample(namelist, n)
        result_txt = '今天吃：'+food_name
if time_cbox['value'] == ('早饭'):
    filename="早饭.csv"

elif time_cbox['value'] ==('午饭'):
    filename="午饭.csv"

elif time_cbox['value'] ==('晚饭'):
    filename="晚饭.csv"

    foodname.config(text= result_txt)



info = tk.Label(root_window,text='终结选择困难的时候到了！',bg='#FFE4E1',fg='black',font=('黑体',20,'normal'))
cur_filename = tk.StringVar()

seleclt_file = tk.Button(root_window,text = '早饭/午饭/晚饭：',command = getfile)

number_txt = tk.Label(root_window,text='饭饭:',bg='#FFE4E1',fg='black',font=('黑体',20,'normal'))
number_entry = tk.Entry(root_window)
select_number = tk.Button(root_window,text = '随机美食',command = random_select)
foodname = tk.Label(root_window,text='',bg='#FFE4E1',fg='black',font=('黑体',20,'normal'))

info.grid(row=0,columnspan=2,padx=10, pady=5)
seleclt_file.grid(row=1,column=0,padx=10, pady=5)
time_cbox.grid(row=1,column=1,padx=10, pady=5,sticky='w')

number_txt.grid(row=2,column=0,padx=10, pady=5)
number_entry.grid(row=2,column=1,padx=10, pady=5)
select_number.grid(row=3,column=0,padx=10, pady=5)
foodname.grid(row=4,columnspan=2,padx=10, pady=5)

root_window.mainloop()