import tkinter as tk
from tkinter import filedialog
import TKinterModernThemes as TKMT
import tscribe

class App(TKMT.ThemedTKinterFrame):
	def __init__(self):
		super().__init__("JSON to Docx Converter", "sun-valley", "light")
		self.frame = self.addLabelFrame("Converter")
		
		# Create StringVars to store the selected file path and output directory
		self.input_file_path_var = tk.StringVar()
		self.output_directory_var = tk.StringVar()
		
		# Add labels to display the selected file path and output directory
		self.input_file_label = self.frame.Label("Selected Input File:")
		self.input_file_label.grid(row=0, column=1)

		self.output_dir_label = self.frame.Label("Output Directory:")
		self.output_dir_label.grid(row=1, column=1)

		# Add buttons to trigger file selections
		self.frame.Button("Set Input File", self.browse_input_file).grid(row=0, column=0)
		self.frame.Button("Set Output Directory", self.browse_output_directory).grid(row=1, column=0)
		self.frame.Button("Convert", self.convert).grid(row=2, column=0)

		# Run the main loop
		self.run()

	def browse_input_file(self):
        # Open a file dialog to select a JSON file
		file_path = filedialog.askopenfilename(initialdir="/",
                                                title="Select Input File",
                                                filetypes=(("json files", "*.json*"),
                                                           ("all files", "*.*")))

        # Update the StringVar with the selected file path
		self.input_file_path_var.set(file_path)

        # Update the label to display the selected file path
		self.input_file_label.config(text=f"Selected Input File: {file_path}")

	def browse_output_directory(self):
		# Open a directory dialog to select an output directory
		dir_path = filedialog.askdirectory(initialdir="/",
                                           title="Select Output Directory")

		# Update the StringVar with the selected output directory
		self.output_directory_var.set(dir_path)

        # Update the label to display the selected output 
		self.output_dir_label.config(text=f"Output Directory: {dir_path}")

	def convert(self):
		tscribe.write(self.input_file_path_var.get(), save_as=self.output_directory_var.get() + "/transcript.docx")
	
# Create an instance of the App class
app = App()
