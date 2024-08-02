import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# File path to the Excel file
file_path = r"Channel list.xlsx"

# Global DataFrame variable
df = pd.DataFrame()

def load_data():
    global df
    try:
        df = pd.read_excel(file_path)
        if 'UP-LINK' in df.columns:
            df['UP-LINK'] = df['UP-LINK'].astype(str).str.replace('MHz', '').astype(float)
        if 'DOWN-LINK' in df.columns:
            df['DOWN-LINK'] = df['DOWN-LINK'].astype(str).str.replace('MHz', '').astype(float)
        print("Data loaded successfully:\n", df.head())
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Band Name', 'Bands', 'UP-LINK', 'DOWN-LINK', 'ERFCN', 'Carrier'])
        print("File not found, creating new DataFrame")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        df = pd.DataFrame(columns=['Band Name', 'Bands', 'UP-LINK', 'DOWN-LINK', 'ERFCN', 'Carrier'])

def save_to_excel():
    global df
    try:
        df.to_excel(file_path, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

def search():
    column = column_var.get()
    value = entry.get()
    output_text.delete('1.0', tk.END)
    
    if column and value:
        try:
            print(f"Searching for {value} in {column}")
            
            if column in ['UP-LINK', 'DOWN-LINK']:
                value = float(value)
                result = df[df[column] == value]
            else:
                result = df[df[column].astype(str) == value]
            
            if not result.empty:
                info = ""
                for idx, row in result.iterrows():
                    uplink = f"{row['UP-LINK']} MHz"
                    downlink = f"{row['DOWN-LINK']} MHz"
                    
                    info += (f"Band Name: {row['Band Name']}\n\n"  # Added spacing
                             f"Bands: {row['Bands']}\n\n"
                             f"UP-LINK: {uplink}\n\n"
                             f"DOWN-LINK: {downlink}\n\n"
                             f"ERFCN: {row['ERFCN']}\n\n"
                             f"Carrier: {row['Carrier']}\n\n")
                output_text.insert(tk.END, info)
            else:
                messagebox.showinfo("Info", f"No results found for {value} in {column}")
        except ValueError:
            messagebox.showerror("Error", "Invalid value entered")
    else:
        messagebox.showerror("Error", "Please select a column and enter a value")

def submit_data():
    new_data = {
        'Band Name': band_name_entry.get(),
        'Bands': bands_entry.get(),
        'UP-LINK': uplink_entry.get(),
        'DOWN-LINK': downlink_entry.get(),
        'ERFCN': erfcn_entry.get(),
        'Carrier': carrier_entry.get()
    }
    
    if any(value.strip() == '' for value in new_data.values()):
        messagebox.showerror("Error", "All fields must be filled")
        return
    
    new_data['UP-LINK'] = f"{new_data['UP-LINK']} MHz"
    new_data['DOWN-LINK'] = f"{new_data['DOWN-LINK']} MHz"
    
    new_data_df = pd.DataFrame([new_data])
    global df
    df = pd.concat([df, new_data_df], ignore_index=True)
    save_to_excel()
    load_data()
    
    band_name_entry.delete(0, tk.END)
    bands_entry.delete(0, tk.END)
    uplink_entry.delete(0, tk.END)
    downlink_entry.delete(0, tk.END)
    erfcn_entry.delete(0, tk.END)
    carrier_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "New data added successfully")

root = tk.Tk()
root.title("Lookup Tool & Data Entry")
root.geometry('500x600')

# Set up styles
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10)
style.map('TButton',
          background=[('active', 'lightgreen')],
          foreground=[('active', 'black')])

# Set up styles for notebook tabs and content
style.configure('TNotebook', background='lightblue')
style.configure('TNotebook.Tab', background='lightgreen', padding=[10, 5], relief='flat')
style.map('TNotebook.Tab', background=[('selected', 'lightblue')])

# Load existing data
load_data()

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Create frames for tabs
lookup_tab = tk.Frame(notebook, bg='lightblue')
add_data_tab = tk.Frame(notebook, bg='lightblue')

# Add tabs to the notebook
notebook.add(lookup_tab, text="Lookup Tool")
notebook.add(add_data_tab, text="Add New Data")

column_var = tk.StringVar()
columns = list(df.columns)
tk.Label(lookup_tab, text="Select Column:", font=('Arial', 14), background='lightblue').pack(pady=5)
column_menu = ttk.Combobox(lookup_tab, textvariable=column_var, values=columns, state="readonly", font=('Arial', 14))
column_menu.pack(pady=5)

tk.Label(lookup_tab, text="Enter Value:", font=('Arial', 14), background='lightblue').pack(pady=5)
entry = ttk.Entry(lookup_tab, font=('Arial', 14))
entry.pack(pady=5)

ttk.Button(lookup_tab, text="Search", command=search, style='TButton').pack(pady=10)

output_text = tk.Text(lookup_tab, wrap="word", width=70, height=20, font=('Arial', 14), bg='#9fccc7', fg='black')
output_text.pack(pady=30)

tk.Label(add_data_tab, text="Band Name:", font=('Arial', 14,), background='lightblue').grid(row=0, column=0, padx=10, pady=5, sticky='e')
band_name_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
band_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

tk.Label(add_data_tab, text="Bands:", font=('Arial', 14,), background='lightblue').grid(row=1, column=0, padx=10, pady=5, sticky='e')
bands_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
bands_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

tk.Label(add_data_tab, text="UP-LINK :", font=('Arial', 14,), background='lightblue').grid(row=2, column=0, padx=10, pady=5, sticky='e')
uplink_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
uplink_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

tk.Label(add_data_tab, text="DOWN-LINK :", font=('Arial', 14,), background='lightblue').grid(row=3, column=0, padx=10, pady=5, sticky='e')
downlink_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
downlink_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

tk.Label(add_data_tab, text="ERFCN:", font=('Arial', 14,), background='lightblue').grid(row=4, column=0, padx=10, pady=5, sticky='e')
erfcn_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
erfcn_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

tk.Label(add_data_tab, text="Carrier:", font=('Arial', 14,), background='lightblue').grid(row=5, column=0, padx=10, pady=5, sticky='e')
carrier_entry = ttk.Entry(add_data_tab, font=('Arial', 14))
carrier_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')

ttk.Button(add_data_tab, text="Submit", command=submit_data, style='TButton').grid(row=6, column=1, columnspan=2, pady=20)

root.mainloop()
