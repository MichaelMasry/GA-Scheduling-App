import tkinter as tk
from tkinter import *
from tkinter import filedialog
from Product import Product
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from termcolor import cprint
from Population import calculate_makespan, calculate_fitness, Population
from Job import Job

if __name__ == "__main__":

    number_of_batches = []
    dic = {}
    products = []
    list_of_products_objects = []
    iterations = 200
    all_jobs = []
    df = []
    m = []
    all_operations = []


    def clicked():
        no_of_products = input_no_of_products.get()
        entry1.delete(0, 'end')
        count = 0
        window1 = tk.Toplevel()
        window1.geometry('600x730')
        label5 = tk.Label(window1, image=img).place(x=450, y=15)
        x1 = 110
        y1 = 125
        y2 = 127
        x2 = 500
        x3 = 25
        y3 = 130
        while count < no_of_products:
            number = count + 1
            name_of_product = tk.StringVar()
            name_of_product.set("Select")
            products.append(name_of_product)
            optionmenu1 = tk.OptionMenu(window1, name_of_product, "ALKAPRESS 10MG 30 TAB", "ALKAPRESS 5MG 20TAB",
                                        "ALKAPRESS 5MG 30 TAB", "ALKAPRESS PLUS 10/160", "ALKAPRESS PLUS 5/160MG",
                                        "ALKOR 10/20MG Suecal 14 tab", "ALKOR 10/40MG Suecal 14 tab",
                                        "BISTOL 10MG 20TAB", "BISTOL 10MG 20TAB TENDER ", "BISTOL 2.5MG 20TAB",
                                        "CIPROBAY 250", "CIPROBAY 500MG", "CIPROBAY 750MG", "XANOXIBAN 15 MG 50TAB",
                                        "XANOXIBAN 20 MG 30TAB", "SUVIKAN 10MG 14 TAB ", "SUVIKAN 20MG 14 TAB ",
                                        "LYROLIN 50MG 30 CAP", "LYROLIN 75MG 20 CAP", "LYROLIN 75MG 30 CAP",
                                        "PEPZOL 40MG 14 CAP", "PEPZOL 40MG 14 CAP Tender", "PEPZOL 40MG 7 CAP")
            optionmenu1.place(x=x1, y=y1)
            optionmenu1.config(width=30)
            label2 = tk.Label(window1, text="Number of Batches :", bg="gainsboro").place(x=380, y=y2)
            no_of_batches = tk.IntVar()
            number_of_batches.append(no_of_batches)
            entry2 = tk.Entry(window1, textvariable=no_of_batches)
            entry2.place(x=x2, y=y2)
            entry2.config(width=5)
            x = "Product {} :"
            label3 = tk.Label(window1, text=x.format(number), bg="gainsboro").place(x=x3, y=y3)
            y2 = y2 + 35
            y1 = y1 + 35
            y3 = y3 + 35
            count = count + 1
        button2 = tk.Button(window1, text="Proceed",
                            command=lambda: clicked1(no_of_products, products, []), bg="maroon",
                            fg="white", width=10).place(x=200, y=60)
        button5 = tk.Button(window1, text="Quit",
                            command=clicked2, bg="maroon",
                            fg="white", width=10).place(x=300, y=60)
        button6 = tk.Button(window1, text="Display",
                            command=lambda: clicked3(no_of_products, products), bg="maroon",
                            fg="white", width=10).place(x=400, y=60)


    def clicked1(no_of_products, products, list_of_products_objects):
        i = 0
        job_id = 0
        while i < no_of_products:
            list_of_products_objects.append(Product(products[i].get(), filename))
            i += 1

        for product_object in list_of_products_objects:
            for i in range(int(product_object.number_of_batches)):
                all_jobs.append(Job(datetime.now(), datetime.now() + timedelta(hours=170), product_object.name
                                    , product_object.number_of_batches, job_id))
                job_id += 1
        for job in all_jobs:
            all_operations.extend(job.operations)

        var1, var2 = calculate_makespan(all_operations)
        cprint("********** JSSP Genetic Solver **********", "yellow")
        population_size = int(4.9 * len(all_operations))
        population = Population(all_operations, population_size)
        current_best = population.genomes[1]  # So that the first best is always printed
        makespans = []
        iteration_numbers = []
        print("Population size: " + str(population_size))

        cprint("\n\nBase configuration:", "blue")
        for operation in all_operations:
            print(str(operation))
            task1 = operation.machine
            finish = operation.start_time + operation.duration
            df.append(dict(Task=task1, Start=operation.start_time, Finish=operation.duration))
        cprint("Total makespan: " + str(var2) + "\n", "red")
        print("\nReproducing population " + str(iterations) + " times...\n")
        p = 1
        flag = False
        print("Running ....")
        while True and p <= iterations:
            makespans.extend([calculate_fitness(x.operations) for x in population.genomes])
            if current_best.score > population.genomes[0].score:
                current_makespan = calculate_makespan(current_best.operations)[1]
                current_best = population.genomes[0]
                print(
                    "#" + str(p) + ". The current best is: " + str(calculate_makespan(current_best.operations)[1])[:7],
                    end=" ")
                print("    Improvement over base: ", end="")
                cprint(str(100 - calculate_makespan(current_best.operations)[1] / var2 * 100)[:6] + "%", "cyan")
                if p >= 2:
                    flag = True
            elif (current_best.score == population.genomes[0].score) and flag:
                break
            population.reproduce_population()
            if (p % 500) == 0:
                cprint("- Completion Iter.: " + str(p) + " ", 'green')
            p = p + 1

        population.reap_population()
        dummy, best_makespan = calculate_makespan(current_best.operations)
        sorted_operations = sorted(current_best.operations, key=lambda x: x.start_time, reverse=False)
        cprint("\n\nOptimized configuration:", "blue")
        for operation in sorted_operations:
            print(str(operation))
        cprint("Total makespan: " + str(best_makespan) + "\n", "grey")


    def openfile():
        global filename
        filename = filedialog.askopenfilename(initialdir="/", title="Select a file")


    def clicked3(no_of_products, products):
        global window2
        window2 = tk.Toplevel()
        window2.geometry('600x730')
        Names = []
        j = 0
        while j < no_of_products:
            Names.append(products[j].get())
            j = j + 1
        update()
        variable = StringVar(window2)
        variable.set(products[0].get())

        optionmenu1 = tk.OptionMenu(window2, variable, *Names, command=callback)

        optionmenu1.place(x=200, y=15)
        optionmenu1.config(width=30)


    def update():
        list_of_products_objects = []
        i = 0
        while i < len(products):
            list_of_products_objects.append(Product(products[i].get(), filename))
            i = i + 1
        return list_of_products_objects


    def callback(selection):
        list_of_products_objects = update()
        infoname = selection
        count = 0
        while count < len(list_of_products_objects):
            if list_of_products_objects[count].name == infoname:
                x = list_of_products_objects[count].info()
                # label9 = tk.Label(window2, text=x, bg="gainsboro").place(x=160, y=200)
                text = Text(window2)
                text.place(x=160, y=200)
                text.insert(INSERT, x)
            count = count + 1


    def clicked2():
        window.destroy()


    window = tk.Tk()
    window.geometry('600x500')
    window.config(bg="gainsboro")
    window.title("Products Form")
    img = ImageTk.PhotoImage(Image.open("photo3.png"))
    label4 = tk.Label(window, image=img).place(x=450, y=15)
    label0 = tk.Label(window, text="Products Form", width=20, font=("bold", 30), bg="gainsboro").place(x=65, y=90)
    label1 = tk.Label(window, text="Number of products :", width=20, font=("bold", 15), bg="gainsboro").place(x=100,
                                                                                                              y=200)
    input_no_of_products = tk.IntVar()
    entry1 = tk.Entry(window, textvariable=input_no_of_products)
    entry1.place(x=350, y=204)
    button1 = tk.Button(window, text="Submit", command=clicked, bg="maroon", fg="white", width=10)
    button1.place(x=200, y=290)
    button3 = tk.Button(window, text="Quit", command=clicked2, bg="maroon", fg="white", width=10).place(x=250, y=350)
    button4 = tk.Button(window, text="Open a file", command=openfile, bg="maroon",
                        fg="white", width=10).place(x=300, y=290)
    window.mainloop()
