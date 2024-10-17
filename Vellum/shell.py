import basic

while True:
    text = input('basic > ')
    
    # If no input is provided, just continue the loop
    if text.strip() == "":
        continue
    
    result, error = basic.run('<stdin>', text)

    if error: 
        print(error.as_string())
    else: 
        print(result)
