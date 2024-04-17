from tkinter import filedialog
import os
import shutil
import tkinter as tk
import subprocess
import cv2
from PIL import Image, ImageTk
from ctypes import windll

class HoverButton(tk.Button):
    def __init__(self, master=None, default_image=None, hover_image=None, **kwargs):
        tk.Button.__init__(self, master, image=default_image, bd=0, highlightthickness=0, **kwargs)
        self.default_image = default_image
        self.hover_image = hover_image
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        if self.hover_image:
            self.config(image=self.hover_image)

    def on_leave(self, event):
        if self.default_image:
            self.config(image=self.default_image)


class App:
    BUTTON_SIZE = 400
    FRAME1_WIDTH = 400
    FRAME2_WIDTH = 800
    FRAME_HEIGHT = 800

    def create_frame3(self):

        # Create the third frame (800x800)
        self.frame3 = tk.Frame(self.root, width=self.FRAME2_WIDTH, height=self.FRAME_HEIGHT, bg="white")
        self.frame3.pack(side=tk.RIGHT)

        # Create a Canvas widget in frame3
        self.canvas = tk.Canvas(self.frame3, width=self.FRAME2_WIDTH, height=self.FRAME_HEIGHT, bg="white",
                                highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')

        # Load and set background image for frame3
        image_path = os.path.join("appgrafica", "3_02.png")
        image3 = Image.open(image_path)
        self.photo3 = ImageTk.PhotoImage(image3)

        # Create an image item on the canvas
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo3)

        # Add text to canvas
        text_content = "Verificarea amprentei durează 1 minut."
        self.canvas.create_text(0, 60, text=text_content, font=("JetBrains Mono ExtraLight", 12), anchor='nw',
                                fill='#6c6a8a', tags="text_content")

        # Create an initial image container (empty)
        initial_image_path = os.path.join("appgrafica", "412x768black.png")
        initial_image = Image.open(initial_image_path)
        self.initial_photo = ImageTk.PhotoImage(initial_image)  # Store as an instance variable

        # Create an image item on the canvas for the initial image container
        initial_image_item = self.canvas.create_image(20, 120, anchor='nw', image=self.initial_photo,
                                                      tags="initial_image")
        # Add Exit Button in Frame 3
        exit_button_image = tk.PhotoImage(
            file="C:\\Users\\Daci\\PycharmProjects\\pythonProject3\\appgrafica\\sbe.png")
        exit_hover_image = tk.PhotoImage(
            file="C:\\Users\\Daci\\PycharmProjects\\pythonProject3\\appgrafica\\sbeh.png")
        exit_button = HoverButton(self.frame3, default_image=exit_button_image, hover_image=exit_hover_image,
                                  command=self.exit_application, cursor="hand2")
        exit_button.place(x=737, y=622)  # Adjust the position as needed

        # Add Back Button in Frame 3
        back_button_image = tk.PhotoImage(
            file="C:\\Users\\Daci\\PycharmProjects\\pythonProject3\\appgrafica\\sbb.png")
        back_hover_image = tk.PhotoImage(
            file="C:\\Users\\Daci\\PycharmProjects\\pythonProject3\\appgrafica\\sbbh.png")
        back_button = HoverButton(self.frame3, default_image=back_button_image, hover_image=back_hover_image,
                                  command=self.go_to_frame2, cursor="hand2")
        back_button.place(x=674, y=622)
        # Add a label to display the result image
        self.result_label = tk.Label(self.frame3, text="Result Image", font=("JetBrains Mono ExtraLight", 12), bg="white")
        self.result_label.pack(pady=10)

        # Additional canvas text items for algorithm parameters
        self.canvas.create_text(20, 540, text="", font=("JetBrains Mono ExtraLight", 12), anchor='nw', fill='#ffffff',
                                tags="best_match")

        self.canvas.create_text(20, 560, text="", font=("JetBrains Mono ExtraLight", 12), anchor='nw', fill='#ffffff',
                                tags="score")

        # Display the canvas content
        self.root.update_idletasks()


    def exit_application(self):
        self.root.destroy()

    # Method to go back to Frame 2
    def go_to_frame2(self):
        self.frame3.pack_forget()
        self.frame2.pack(side=tk.RIGHT)

    def __init__(self, root):
        self.root = root
        self.root.title("Amprenta - recunoaștere biometrică")
        self.root.geometry(f"{self.FRAME1_WIDTH + self.FRAME2_WIDTH}x{self.FRAME_HEIGHT}")

        # Create the first frame (400x800)
        self.frame1 = tk.Frame(root, width=self.FRAME1_WIDTH, height=self.FRAME_HEIGHT, bg="white")
        self.frame1.pack(side=tk.LEFT)

        # Load and set background image for frame1
        image1 = Image.open(os.path.join("appgrafica", "1.png"))
        self.photo1 = ImageTk.PhotoImage(image1)
        background_label1 = tk.Label(self.frame1, image=self.photo1)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the second frame (800x800)
        self.frame2 = tk.Frame(root, width=self.FRAME2_WIDTH, height=self.FRAME_HEIGHT, bg="white")
        self.frame2.pack(side=tk.RIGHT)

        # Load and set background image for frame2
        image2 = Image.open(os.path.join("appgrafica", "2.png"))
        self.photo2 = ImageTk.PhotoImage(image2)
        background_label2 = tk.Label(self.frame2, image=self.photo2)
        background_label2.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and set images for buttons
        button_image1 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_1.png")
        hover_image1 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_1_hover.png")
        self.button_photo1 = HoverButton(self.frame2, default_image=button_image1, hover_image=hover_image1,
                                         command=lambda: self.button_clicked(1), cursor="hand2")
        self.button_photo1.place(x=0, y=0)

        button_image2 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_2.png")
        hover_image2 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_2_hover.png")
        self.button_photo2 = HoverButton(self.frame2, default_image=button_image2, hover_image=hover_image2,
                                         command=lambda: self.button_clicked(2), cursor="hand2")
        self.button_photo2.place(x=400, y=0)

        button_image3 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_3.png")
        hover_image3 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_3_hover.png")
        self.button_photo3 = HoverButton(self.frame2, default_image=button_image3, hover_image=hover_image3,
                                         command=lambda: self.button_clicked(3), cursor="hand2")
        self.button_photo3.place(x=0, y=400)

        button_image4 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_4.png")
        hover_image4 = tk.PhotoImage(file="C:/Users/Daci/PycharmProjects/pythonProject3/appgrafica/2_4_hover.png")
        self.button_photo4 = HoverButton(self.frame2, default_image=button_image4, hover_image=hover_image4,
                                         command=lambda: self.button_clicked(4), cursor="hand2")
        self.button_photo4.place(x=400, y=400)


    def button_clicked(self, button_number):
        print(f"Button {button_number} clicked!")
        # Specific actions based on button_number
        if button_number == 4:
            self.root.destroy()  # Exit the Tkinter application
        elif button_number == 3:
            folder_path = r"C:\Users\Daci\PycharmProjects\pythonProject3\data\SOCOFing\Real"
            subprocess.Popen(f'explorer "{folder_path}"')
        elif button_number == 2:
            file_path = filedialog.askopenfilename(title="Select a file to upload", filetypes=[("All files", "*.*")])
            if file_path:
                print(f"Selected file: {file_path}")
                destination_path = r"C:\Users\Daci\PycharmProjects\pythonProject3\data\SOCOFing\Real"
                shutil.copy(file_path, destination_path)
                print(f"File copied to: {destination_path}")
        elif button_number == 1:
            # Introduce a delay of 2000 milliseconds (2 seconds) before running the algorithm
            self.root.after(2000, self.run_algorithm)

    def run_algorithm(self):
        # Display Frame 3 after algorithm execution
        self.frame2.pack_forget()
        self.create_frame3()

        # Open a file dialog for the user to select an image
        file_path = filedialog.askopenfilename(title="Select an image",
                                               filetypes=[("Image files", "*.bmp;*.jpg;*.png")])

        if not file_path:
            print("No file selected. Exiting.")
            exit()

        # Load the selected image
        sample = cv2.imread(file_path)

        best_score = 0
        filename = None
        image = None
        kp1, kp2, mp = None, None, None

        #counter = 0  # debug to check if the loop is... LOOPING! :D
        # "C:/Users/Daci/PycharmProjects/pythonProject2/SOCOFing/Real"
        for file in [file for file in os.listdir("C:/Users/Daci/PycharmProjects/pythonProject3/data/SOCOFing/Real")][:6000]:
           # counter += 1  # debug: end
           # if counter % 10 == 0:  # debug: checking the file actually being processed (prints every 10 items!!)
               # print(counter)
               # print(file)
            fingerprint_image = cv2.imread("C:/Users/Daci/PycharmProjects/pythonProject3/data/SOCOFing/Real/" + file)
            sift = cv2.SIFT_create()

            keypoints_1, descriptors_1 = sift.detectAndCompute(sample, mask=None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, mask=None)
            flann_matcher = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {})
            # Use the FlannBasedMatcher for knnMatch
            matches = flann_matcher.knnMatch(descriptors_1, descriptors_2, k=2)

            match_points = []

            for p, q in matches:
                if p.distance < 0.1 * q.distance:
                    match_points.append(p)
            keypoints = 0
            if len(keypoints_1) < len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)

            if len(match_points) / keypoints * 100 > best_score:
                best_score = len(match_points) / keypoints * 100
                filename = file
                image = fingerprint_image
                kp1, kp2, mp = keypoints_1, keypoints_2, match_points

        if filename is not None:

            # Display algorithm parameters on canvas
            self.canvas.itemconfig("best_match", text="Am găsit o potrivire în baza de date " + filename)
            self.canvas.itemconfig("score", text="Scor " + str(best_score))

            # Display the result image in the result_label
            result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
            result = cv2.resize(result, None, fx=4, fy=4)  # Adjust the scaling factor as needed
            result_image = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB)))
            self.result_label.config(image=result_image)
            self.result_label.image = result_image  # Keep a reference to prevent the image from being garbage collected

            # Update the initial image container with the result image
            self.canvas.itemconfig("initial_image", image=result_image)
            # Display algorithm parameters on canvas
            self.canvas.itemconfig("best_match", text="Am găsit o potrivire în baza de date: " + filename)
            self.canvas.itemconfig("score", text="Scor: " + str(best_score))
        else:
            print("No valid matches found.")


if __name__ == "__main__":
    root = tk.Tk()
    windll.shcore.SetProcessDpiAwareness(1)
    app = App(root)
    root.mainloop()
