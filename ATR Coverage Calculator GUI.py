from datetime import date
import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# class mainWindow(tk.Frame):
class mainWindow():
  max_height = 800
  max_width = 1200
  splash_delay = 1500  

  # Branding logo
  image_logo = Image.open('./Images/Zebra_Logo_W.png')

  # Icon image
  image_ico = Image.open('./Images/Zebra_Logo_K_ico.png')


  def __init__(self, master):
    self.master = master
    # tk.Frame.__init__(self, self.master)
    self.configure_gui()
    self.create_widgets()
    self.destroy_splash_and_start()
    
  
  def about(self):
    messagebox.showinfo('About', \
      f'ATR Coverage Calculator\
      \n\n\tVersion: 3.0.4\
      \n\n\tRelease Date: Tueday October 18 2022\
      \n\nhttps://github.com/cddevs/ATR-Coverage-Calculator/releases\
      \n\n©{self.current_date.year} C. D\'Costa'
    )
  
  
  def configure_gui(self):
    self.SoM_values = set_SoM("Metric")
    self.SoM_units = tk.StringVar()
    self.SoM_units.set(self.SoM_values[1])
    self.create_menu_bar()
    self.master.title('ATR Coverage Calculator')
    self.master.geometry('1200x800')
    self.master.resizable(False, False)
    self.master.configure(background='#000000', menu=self.menubar)
    self.image_ico = ImageTk.PhotoImage(self.image_ico)
    self.master.iconphoto(True, self.image_ico)   
    

  def create_widgets(self):
    self.create_frame_header()
    self.create_frame_content()
    self.create_frame_footer()
    self.create_results_display()
  

  def create_frame_header(self):
    self.frame_header = tk.Frame(self.master, background='#000000', height=80, width=self.max_width-200)
    self.frame_header.pack()

    # Add logo to header frame
    self.image_logo = ImageTk.PhotoImage(self.image_logo)
    self.label_logo = tk.Label(self.frame_header, background='#000000', image=self.image_logo)
    self.label_logo.place(width=235)

    # Add title to header frame
    self.label_title = tk.Label(self.frame_header, anchor="e", background='#000000', foreground='#FFFFFF', font=('Arial', 35), text='ATR Coverage Calculator')
    self.label_title.place(height=80, width=765, x=235)


  def create_frame_content(self):
    self.frame_content = tk.Frame(self.master, background='#000000', height=670, width=self.max_width-200)
    self.frame_content.pack()

    # Open and ATR Coverage Image
    self.image_ATR_coverage = Image.open('./Images/ATR_Coverage.png')
    
    # Add ATR Coverage Image to content frame
    self.image_ATR_coverage = ImageTk.PhotoImage(self.image_ATR_coverage)
    self.label_ATR_coverage = tk.Label(self.frame_content, background='#000000', image=self.image_ATR_coverage)
    self.label_ATR_coverage.place(height=379, width=689, x=145.5, y=155.5)    
  

  def create_frame_footer(self):
    self.frame_footer = tk.Frame(self.master, background='#000000', height=50, width=self.max_width-200)
    self.frame_footer.pack(side='bottom')
    
    # Add text to footer frame
    self.current_date = date.today()
    self.footer_text = f'ZEBRA and the stylized Zebra head are trademarks of Zebra Technologies Corp., registered in many jurisdictions worldwide. All other trademarks are the property of their respective owners.\n©{self.current_date.year} Zebra Technologies Corp. and/or its affiliates. All rights reserved.'
    self.label_footer = tk.Label(self.frame_footer, background='#000000', foreground='#FFFFFF', text=self.footer_text)
    self.label_footer.place(anchor='nw')


  def create_menu_bar(self):
    self.menubar = tk.Menu(self.master, tearoff=0)
    
    self.SoM = tk.StringVar()
    self.SoM.set('Metric')
    menu_system_of_measurement = tk.Menu(self.master, tearoff=0)
    menu_system_of_measurement.add_radiobutton(label='Metric', variable=self.SoM, value='Metric', command=self.update_SoM) 
    menu_system_of_measurement.add_radiobutton(label='Imperial', variable=self.SoM, value='Imperial', command=self.update_SoM) 
    self.menubar.add_cascade(label='System of Measurement', menu=menu_system_of_measurement)
    
    self.atr_height_override = tk.StringVar()
    self.atr_height_override.set('Disable')
    menu_atr_height_override = tk.Menu(self.master, tearoff=0)
    menu_atr_height_override.add_radiobutton(label='Enable', variable=self.atr_height_override, value='Enable', command=self.update_atr_height_override) 
    menu_atr_height_override.add_radiobutton(label='Disable', variable=self.atr_height_override, value='Disable', command=self.update_atr_height_override) 
    self.menubar.add_cascade(label='ATR Height Override', menu=menu_atr_height_override)
    
    self.menubar.add_command(label='About', command=self.about)


  def create_results_display(self):
    self.results_output_height_atr = tk.StringVar()
    self.results_output_height_tag = tk.StringVar()
    self.results_output_height_max_accuracy = tk.StringVar()
    self.results_output_default_circle_radius = tk.StringVar()
    self.results_output_default_spacing = tk.StringVar()
    self.results_output_default_circle_area = tk.StringVar()
    self.results_output_default_hex_cell_area = tk.StringVar()
    self.results_output_typical_circle_radius = tk.StringVar()
    self.results_output_typical_spacing = tk.StringVar()
    self.results_output_typical_circle_area = tk.StringVar()
    self.results_output_typical_hex_cell_area = tk.StringVar()
    self.results_output_max_accuracy_spacing = tk.StringVar()
    self.results_output_max_accuracy_hex_cell_area = tk.StringVar()

    # Frame to contain Results Table frames
    self.frame_results = tk.Frame(self.frame_content, background='#000000', height=290)
    self.frame_results.place(x=50, rely = 0.48)
    
    label_results_max_accuracy_note = tk.Label(self.frame_results, background='#000000', foreground='#FFFFFF', font=('Arial', 12), text=f'\n* For maximum accuracy coverage, ATR spacing has been reduced by 15%')
    label_results_max_accuracy_note.pack(side='bottom')

    # Frame for Results Table row headings
    self.frame_results_headings = tk.Frame(self.frame_results, background='#000000', height=290)
    self.frame_results_headings.pack(side='left')

    label_heading_spacer = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15))
    label_heading_spacer.pack(anchor='e')
    label_heading_height_atr = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'ATR Mount Height')
    label_heading_height_atr.pack(anchor='e')
    label_heading_elevation_scan_angle = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'Elevation Scan Angle')
    label_heading_elevation_scan_angle.pack(anchor='e')
    label_heading_height_tag = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'Maximum/Average Tag Height')
    label_heading_height_tag.pack(anchor='e')
    label_heading_atr_hexagonal_coverage_area = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'ATR Hexagonal Coverage Area')
    label_heading_atr_hexagonal_coverage_area.pack(anchor='e')
    label_heading_atr_spacing = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'ATR Spacing')
    label_heading_atr_spacing.pack(anchor='e')
    label_heading_circle_coverage = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'FYI - Circle Coverage')
    label_heading_circle_coverage.pack(anchor='w')
    label_heading_circle_coverage_radius = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'Radius')
    label_heading_circle_coverage_radius.pack(anchor='e')
    label_heading_circle_coverage_diametre = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'Diametre')
    label_heading_circle_coverage_diametre.pack(anchor='e')
    label_heading_circle_coverage_area = tk.Label(self.frame_results_headings, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'Area')
    label_heading_circle_coverage_area.pack(anchor='e')

    # Frame for Results Table Default coloumn
    self.frame_results_default = tk.Frame(self.frame_results, background='#000000', height=290)
    self.frame_results_default.pack(side='left')

    label_results_default = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f' Default Coverage ')
    label_results_default.pack()
    label_results_default_height_atr = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_atr}')
    label_results_default_height_atr.pack()    
    label_results_default_elevation_scan_angle = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'60.00\N{DEGREE SIGN}')
    label_results_default_elevation_scan_angle.pack()
    label_results_default_height_tag = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_tag}')
    label_results_default_height_tag.pack()
    label_results_default_hex_cell_area = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_default_hex_cell_area}')
    label_results_default_hex_cell_area.pack()
    label_results_default_spacing = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_default_spacing}')
    label_results_default_spacing.pack()
    label_results_default_circle_coverage_spacer = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'')
    label_results_default_circle_coverage_spacer.pack()
    label_results_default_circle_radius = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_default_circle_radius}')
    label_results_default_circle_radius.pack()    
    label_results_default_circle_diametre = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_default_spacing}')
    label_results_default_circle_diametre.pack()
    label_results_default_circle_area = tk.Label(self.frame_results_default, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_default_circle_area}')
    label_results_default_circle_area.pack()
    

    # Frame for Results Table Typical coloumn
    self.frame_results_typical = tk.Frame(self.frame_results, background='#000000', height=290)
    self.frame_results_typical.pack(side='left')

    label_results_typical = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f' Typical Coverage ')
    label_results_typical.pack()
    label_results_typical_height_atr = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_atr}')
    label_results_typical_height_atr.pack()    
    label_results_typical_elevation_scan_angle = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'54.70\N{DEGREE SIGN}')
    label_results_typical_elevation_scan_angle.pack()
    label_results_typical_height_tag = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_tag}')
    label_results_typical_height_tag.pack()
    label_results_typical_hex_cell_area = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_hex_cell_area}')
    label_results_typical_hex_cell_area.pack()
    label_results_typical_spacing = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_spacing}')
    label_results_typical_spacing.pack()
    label_results_typical_circle_coverage_spacer = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'')
    label_results_typical_circle_coverage_spacer.pack()
    label_results_typical_circle_radius = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_circle_radius}')
    label_results_typical_circle_radius.pack()    
    label_results_typical_circle_diametre = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_spacing}')
    label_results_typical_circle_diametre.pack()
    label_results_typical_circle_area = tk.Label(self.frame_results_typical, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_circle_area}')
    label_results_typical_circle_area.pack()
    

    # Frame for Results Table Max Accuracy coloumn
    self.frame_results_max_accuracy = tk.Frame(self.frame_results, background='#000000', height=290)
    self.frame_results_max_accuracy.pack(side='left')
    
    label_results_max_accuracy = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f' Maximum Accuracy Coverage ')
    label_results_max_accuracy.pack()
    label_results_max_accuracy_height_atr = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_atr}')
    label_results_max_accuracy_height_atr.pack()    
    label_results_max_accuracy_elevation_scan_angle = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'54.70\N{DEGREE SIGN}')
    label_results_max_accuracy_elevation_scan_angle.pack()
    label_results_max_accuracy_height_tag = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_height_tag}')
    label_results_max_accuracy_height_tag.pack()
    label_results_max_accuracy_hex_cell_area = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_max_accuracy_hex_cell_area}')
    label_results_max_accuracy_hex_cell_area.pack()
    label_results_max_accuracy_spacing = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_max_accuracy_spacing}')
    label_results_max_accuracy_spacing.pack()
    label_results_max_accuracy_circle_coverage_spacer = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), text=f'')
    label_results_max_accuracy_circle_coverage_spacer.pack()
    label_results_max_accuracy_circle_radius = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_circle_radius}')
    label_results_max_accuracy_circle_radius.pack()    
    label_results_max_accuracy_circle_diametre = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_spacing}')
    label_results_max_accuracy_circle_diametre.pack()
    label_results_max_accuracy_circle_area = tk.Label(self.frame_results_max_accuracy, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.results_output_typical_circle_area}')
    label_results_max_accuracy_circle_area.pack()

    self.frame_results.place_forget()
  
  
  def calculate(self, som, height_atr, height_tag):
    user_input_height_atr = height_atr
    user_input_height_tag = height_tag
    if float(user_input_height_atr) > 0:
      if check_input_number(user_input_height_atr, som[2], som[3]) or self.atr_height_override.get() == 'Enable':
        if check_input_number(user_input_height_tag, 0, user_input_height_atr):
          self.results = results = calculate_coverage(user_input_height_atr, user_input_height_tag)
          self.update_results_display()
          
          # # Print out the default results - Uncomment if output to command line required.
          # description = f"Default"
          # printout_coverage(description, som[1], 60.00, results["height_atr"], 0, results["default_hex_cell_area"], results["default_spacing"], results["default_circle_radius"], results["default_spacing"], results["default_circle_area"])

          # # Print out the typical results
          # description = f"Typical"
          # printout_coverage(description, som[1], 54.70, results["height_atr"], results["height_tag"], results["typical_hex_cell_area"], results["typical_spacing"], results["typical_circle_radius"], results["typical_spacing"], results["typical_circle_area"])

          # # Print out the max results
          # description = f"Maximum Accuracy"
          # notes = "Please note, to achieve maximum accuracy, spacing has been reduced by 15%."
          # printout_coverage(description, som[1], 54.70, results["height_atr"], results["height_tag"], results["max_accuracy_hex_cell_area"], results["max_accuracy_spacing"], results["typical_circle_radius"], results["typical_spacing"], results["typical_circle_area"], notes)
        else:
          # print(f'\nError: Invalid Tag height. Accepted values are between 0.00 and {user_input_height_atr} {som[1]} inclusive.')
          messagebox.showerror('Error', \
            f'Invalid Tag height.\
              \n\nAccepted values are between 0.00 and {user_input_height_atr} {som[1]} inclusive.'
          )
      else:
        # print(f"\nError: Invalid ATR height. Accepted values are between {som[2]:.4f} and {som[3]:.4f} {som[1]} inclusive.")
        messagebox.showerror('Error', \
          f'Invalid ATR height.\
            \n\nAccepted values are between {som[2]:.4f} and {som[3]:.4f} {som[1]} inclusive.'
        )
    else:
        messagebox.showerror('Error', \
          f'Invalid ATR height.\
            \n\nAccepted value needs to be greater then 0.00.'
        )


  def calculation_input(self):
    self.label_height_atr = tk.Label(self.frame_content, background='#000000', foreground='#FFFFFF', font=('Arial', 20), text="Enter the Height of ATR7000 from the Ground")
    position_x = (self.frame_content.winfo_width() - self.label_height_atr.winfo_reqwidth())/2
    self.label_height_atr.place(x = position_x, rely = 0.03)

    self.entry_height_atr_input = tk.StringVar()
    self.entry_height_atr_input.set(self.SoM_values[2])
    self.entry_height_atr = tk.Entry(self.frame_content, justify='right', textvariable=self.entry_height_atr_input)
    position_x = (self.frame_content.winfo_width() - self.entry_height_atr.winfo_reqwidth()*2)/2 - 5
    self.entry_height_atr.place(x = position_x, rely = 0.11)

    self.label_height_atr_som = tk.Label(self.frame_content, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.SoM_units}')
    position_x = (self.frame_content.winfo_width())/2 + 5
    self.label_height_atr_som.place(x = position_x, rely = 0.10)
    

    self.label_height_tag = tk.Label(self.frame_content, background='#000000', foreground='#FFFFFF', font=('Arial', 20), text="Enter the Maximum or Average Tag Height")
    position_x = (self.frame_content.winfo_width() - self.label_height_tag.winfo_reqwidth())/2
    self.label_height_tag.place(x = position_x, rely = 0.22)

    self.entry_height_tag_input = tk.StringVar()
    self.entry_height_tag_input.set('0')
    self.entry_height_tag = tk.Entry(self.frame_content, justify='right', textvariable=self.entry_height_tag_input)
    position_x = (self.frame_content.winfo_width() - self.entry_height_tag.winfo_reqwidth()*2)/2 - 5
    self.entry_height_tag.place(x = position_x, rely = 0.31)

    self.label_height_atr_som = tk.Label(self.frame_content, background='#000000', foreground='#FFFFFF', font=('Arial', 15), textvariable=f'{self.SoM_units}')
    position_x = (self.frame_content.winfo_width())/2 + 5
    self.label_height_atr_som.place(x = position_x, rely = 0.30)


    self.button_calculate = tk.Button(self.frame_content, command=lambda: self.calculate(self.SoM_values, self.entry_height_atr_input.get(), self.entry_height_tag_input.get()), font=('Arial', 15), text="Calculate")
    position_x = (self.frame_content.winfo_width() - self.button_calculate.winfo_reqwidth()*2)/2 - 5
    self.button_calculate.place(x = position_x, rely = 0.38)

    self.button_clear = tk.Button(self.frame_content, command=self.reset, font=('Arial', 15), text="Reset")
    position_x = (self.frame_content.winfo_width())/2 + 5
    self.button_clear.place(x = position_x, rely = 0.38)

    
  def destroy_splash_and_start(self):            
    self.label_ATR_coverage.after(self.splash_delay,self.label_ATR_coverage.destroy)    
    self.frame_content.after(self.splash_delay,self.calculation_input)
    

  def reset(self):
    self.entry_height_atr_input.set(self.SoM_values[2])
    self.entry_height_tag_input.set('0')
    self.frame_results.place_forget()


  def update_results_display(self):
    self.results_output_height_atr.set(f'{self.results["height_atr"]:.2f} {self.SoM_units.get()}')
    self.results_output_height_tag.set(f'{self.results["height_tag"]:.2f} {self.SoM_units.get()}')
    self.results_output_height_max_accuracy.set(self.results["height_max_accuracy"])
    self.results_output_default_circle_radius.set(f'{self.results["default_circle_radius"]:.2f} {self.SoM_units.get()}')
    self.results_output_default_spacing.set(f'{self.results["default_spacing"]:.2f} {self.SoM_units.get()}')
    self.results_output_default_circle_area.set(f'{self.results["default_circle_area"]:.2f} {self.SoM_units.get()}\N{SUPERSCRIPT TWO}')
    self.results_output_default_hex_cell_area.set(f'{self.results["default_hex_cell_area"]:.2f} {self.SoM_units.get()}\N{SUPERSCRIPT TWO}')
    self.results_output_typical_circle_radius.set(f'{self.results["typical_circle_radius"]:.2f} {self.SoM_units.get()}')
    self.results_output_typical_spacing.set(f'{self.results["typical_spacing"]:.2f} {self.SoM_units.get()}')
    self.results_output_typical_circle_area.set(f'{self.results["typical_circle_area"]:.2f} {self.SoM_units.get()}\N{SUPERSCRIPT TWO}')
    self.results_output_typical_hex_cell_area.set(f'{self.results["typical_hex_cell_area"]:.2f} {self.SoM_units.get()}\N{SUPERSCRIPT TWO}')
    self.results_output_max_accuracy_spacing.set(f'{self.results["max_accuracy_spacing"]:.2f} {self.SoM_units.get()} *')
    self.results_output_max_accuracy_hex_cell_area.set(f'{self.results["max_accuracy_hex_cell_area"]:.2f} {self.SoM_units.get()}\N{SUPERSCRIPT TWO}')
    
    self.frame_results.place(x=50, rely = 0.48)

  
  def update_atr_height_override(self):
    self.reset()
    messagebox.showwarning('ATR Height',\
      f'Override: {self.atr_height_override.get()}d.')


  def update_SoM(self):
    self.SoM_values = set_SoM(self.SoM.get())
    self.SoM_units.set(self.SoM_values[1])
    self.reset()
    messagebox.showinfo('System of Measurement',\
      f'System of Measurement set to: {self.SoM_values[0]}\
        \n\nPlease input all height measurements in {self.SoM_units.get()}.')
    
    
    

# End of mainWindow() Class Defintion






def calculate_coverage(height_atr, height_tag):
    height_atr = float(height_atr)
    height_tag = float(height_tag)
    height_max_accuracy = height_atr - height_tag
    
    # Radius calculation validated using https://www.omnicalculator.com/math/triangle-30-60-90
    default_circle_radius = math.tan(math.radians(60)) * height_atr
    default_spacing = 2 * default_circle_radius #This is also equal to the default circle diameter
    default_circle_area = math.pi * default_circle_radius**2
    
    default_hex_cell_area = math.sqrt(3)/2 * default_spacing**2

    typical_circle_radius = math.tan(math.radians(54.7)) * height_max_accuracy
    typical_spacing = 2 * typical_circle_radius #This is also equal to the typical circle diameter
    typical_circle_area = math.pi * typical_circle_radius**2

    typical_hex_cell_area = math.sqrt(3)/2 * typical_spacing**2

    max_accuracy_spacing = 0.85 * typical_spacing
    max_accuracy_hex_cell_area = math.sqrt(3)/2 * max_accuracy_spacing**2
    
    # Build a dictionary that will be returned and contains all the calculated values
    results = {
        "height_atr" : height_atr,
        "height_tag" : height_tag,
        "height_max_accuracy" : height_max_accuracy,
        "default_circle_radius" : default_circle_radius,
        "default_spacing": default_spacing,
        "default_circle_area" : default_circle_area,
        "default_hex_cell_area" : default_hex_cell_area,
        "typical_circle_radius" : typical_circle_radius,
        "typical_spacing" : typical_spacing,
        "typical_circle_area" : typical_circle_area,
        "typical_hex_cell_area" : typical_hex_cell_area,
        "max_accuracy_spacing" : max_accuracy_spacing,
        "max_accuracy_hex_cell_area" : max_accuracy_hex_cell_area
    }

    return results


def check_input_number(input, minimum, maximum):
    try:
        # Try to convert it to float & test it is within the accepted range.
        return float(input) >= float(minimum) and float(input) <= float(maximum)
    except ValueError:
        return False


def printout_coverage(description, uom, scan_angle, height_atr, height_tag, hex_cell_area, spacing, circle_radius, circle_diametre, circle_area, notes = ""):
    print(f"\n\n{description} Coverage Area:")
    
    print(f"\n\tATR mount height = {height_atr:.2f} {uom}")
    print(f"\tElevation scan angle = {scan_angle}\N{DEGREE SIGN}")
    print(f"\tMaximum/Average Tag Height = {height_tag:.2f} {uom}")
    
    print(f"\n\tATR Hexagonal Coverage Area = {hex_cell_area:.2f} {uom}\N{SUPERSCRIPT TWO}")
    print(f"\tThe spacing between each ATR = {spacing:.2f} {uom}")
    
    if notes != "":
        print(f"\t\t{notes}")
    
    print(f"\n\tAs an FYI, Circle Coverage:")
    print(f"\n\t\tRadius = {circle_radius:.2f} {uom}")
    print(f"\t\tDiametre = {circle_diametre:.2f} {uom}")
    print(f"\t\tArea = {circle_area:.2f} {uom}\N{SUPERSCRIPT TWO}")



def set_SoM(choice):
    while True:
        if choice == "Imperial":
            return ["Imperial", "feet", 12.00, 20.00]
        else:
            return ["Metric", "metres", 3.6576, 6.0960]



def main():
  root = tk.Tk()
  main_app =  mainWindow(root)
  root.mainloop()


# Check if program is being called explicitly
if __name__ == '__main__':
   main()