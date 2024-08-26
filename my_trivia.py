from tkinter import *
import requests


my_params = {
    'amount':5,
    'category':17,
    # 'difficulty':'easy',
    'type':'boolean'
}

my_url = 'https://opentdb.com/api.php'



def get_question():
    response = requests.get(my_url, params=my_params)
    # response = requests.get('https://opentdb.com/api.php?amount=10&category=32&type=boolean')
    response.raise_for_status()
    data = response.json()['results']
    # print(f"{data}")
    return data
    # canvas.itemconfig(quote_text, text=data)


    #Write your code here.

# def my_app():
#     window = Tk()
#     window.title("Harsh Says...")
#     window.config(padx=50, pady=50)

#     canvas = Canvas(width=300, height=414)
#     background_img = PhotoImage(file="background.png")
#     canvas.create_image(150, 207, image=background_img)
#     quote_text = canvas.create_text(150, 207, text="Harsh's Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
#     canvas.grid(row=0, column=0)

#     kanye_img = PhotoImage(file="harsh_2.png", height= 350,width= 340)
#     kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_question)
#     kanye_button.grid(row=1, column=0)



#     window.mainloop()




if __name__ == "__main__":
    get_question()


