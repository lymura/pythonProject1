with open("python.txt", "a") as f_obj:
    input_str = input('Text: \n')
    while input_str:
        f_obj.writelines(f'{input_str}\n')
        input_str = input('Text: \n')
f_obj.close()






