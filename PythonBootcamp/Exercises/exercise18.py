def fitness_plan(name, age, level):
    print(f"Hello, {name}! Based on your info: ")
    if age > 50:
        print("Low-impact activities like walking and swimming are recommended.")
    else:
        if level == "beginner":
            print("Start with light cardio and bodyweight exercises.")
        elif level == "intermediate":
            print("Include strength training and moderate cardio.")
        elif level == "advanced":
            print("You can follow an intense workout plan including HIIT and weightlifting.")
        else:
            print("Unknown level, please enter beginner, intermediate, or advanced.")

#Kullanicidan giris almak:
name_input = (input("What is your name? "))
age_input = int(input("What is your age? "))
level_input = input("What is your level? ")

fitness_plan(name_input, age_input, level_input)
