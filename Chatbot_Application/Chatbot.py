from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pathlib

#SETTINGS
FONT = "Helvetica 11"
FONT_2 = "Helvetica 13 bold"
BACKROUND_COLOR = "#006652"
BACKROUND_GRAY = "#909aa2"
TEXT_COLOR = "#EAECEE"


global AI_name
AI_name='Alec'
global chatbot
chatbot = ChatBot(AI_name, 

	logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Sorry, I don't understand, try asking:\n\n- What do you sell?\n\n- Can I get a refund?\n\n- do you have coupons?\n\n- How much is shipping?\n\n- What are your sizes?",
            'maximum_similarity_threshold': 0.7
            
        },

    ],
 )

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    str(pathlib.Path().absolute())+'/english/',
)


class AppBot:
    
    def __init__(self):
        self.frame = Tk()
        self.create_main_area()
        
    def play(self):
        self.frame.mainloop()
        
    def create_main_area(self):
        self.frame.title("You're Speaking With AI Alec")

        self.frame.configure(width=490, height=560, bg=BACKROUND_COLOR)
        
        top_area = Label(self.frame, bg=BACKROUND_COLOR, fg=TEXT_COLOR, # header
                           text="Online Clothing Store -- ChatBot", font=FONT_2, pady=11)
        top_area.place(relwidth=1)
        
        seperate = Label(self.frame, width=470, bg=BACKROUND_GRAY) #line seperator
        seperate.place(relwidth=1, rely=0.07, relheight=0.012)
        
        self.text_widget = Text(self.frame, width=21, height=3, bg=BACKROUND_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=20, pady=20)
        self.text_widget.place(relheight=0.75, relwidth=1, rely=0.07)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        scroll = Scrollbar(self.text_widget) #scrollbar
        scroll.place(relheight=1, relx=0.99 )
        scroll.configure(command=self.text_widget.yview)
        
        bottom_area = Label(self.frame, bg=BACKROUND_GRAY, height=80)
        bottom_area.place(relwidth=1, rely=0.85)
        

        self.msg_entry = Entry(bottom_area, bg="#f2f2f2", fg="#262626", font=FONT)     
        self.msg_entry.place(relwidth=0.8, relheight=0.04, rely=0.004, relx=0.03)
        self.msg_entry.focus()
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, f"Hi! I'm {AI_name} - Your Friendly AI Store Assistant \n\n-- What can I help you with?\n\n\n")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
        
        self.msg_entry.bind("<Return>", self.check_enter)
        

        send_button = Button(bottom_area, text="Send", font=FONT_2, width=10, bg=BACKROUND_GRAY, #send button
                             command=lambda: self.check_enter(None))
        send_button.place(relx=0.84, rely=0.008, relheight=0.03, relwidth=0.15)
     
    def check_enter(self, event):
        messege = self.msg_entry.get()
        self.type_message(messege, "You")
        
    def type_message(self, messege, client):
        
        if not messege:
            return
        
        self.msg_entry.delete(0, END)
        messege1 = f"{client}: {messege}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, messege1)
        self.text_widget.configure(state=DISABLED)
        
        messege2 = f"{AI_name}: {chatbot.get_response(messege)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, messege2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = AppBot()
    app.play()