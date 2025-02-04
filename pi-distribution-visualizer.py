import requests
from  matplotlib import pyplot 

def get_pi(start = 0,number_of_digits = 100):
    # Fetches digits of Pi from an external API.
    # API supports maxium 100 digits
    URL = f"https://api.pi.delivery/v1/pi?start={start}&numberOfDigits={number_of_digits}&radix=10"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Eror {response.status_code}")
        return None
    pi =  data["content"]
    return pi

def get_pi_from(start_from = 0,end = 100):
    # Returns values using get_pi() without a limit.
    text = ""
    current_start = start_from
    length = end - start_from
    if length < 100:
        text = get_pi(start_from,length)
        return text
    else:
        request_number = ( length//100 ) 
        remainder = length % 100
        for i in  range(request_number):
            text += get_pi(current_start,100)
            current_start += 100
        if remainder > 0:
            text += get_pi(current_start,remainder)
        return text
    
def write_file(start,end):
    # Creates text file using 
    with open("pi.txt","w") as file:
        file.write(get_pi_from(start,end))

def read_file():
    # Reads text file which created by write_file()
    with open("pi.txt","r") as file:
        content = file.read()
    return content

def process_return_array(content):
    # Counts number of digits in a string
    DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
    pi_list = [char for char in content]
    times_by_digits = []
    for i in DIGITS:
        times = pi_list.count(i)
        times_by_digits.append(times)
    return times_by_digits,DIGITS

def bar_chart_show(digits,times_by_digits):
    #show bar chart
    pyplot.bar(digits,times_by_digits,0.5, edgecolor = "black")
    pyplot.xlabel("digits")
    pyplot.ylabel("How many")
    pyplot.title("pi number")
    pyplot.show()

#
content = get_pi_from(0,10000)
times_by_digits,DIGITS= process_return_array(content=content)
bar_chart_show(DIGITS,times_by_digits)