# Pi Digit Frequency Analysis and Visualization

This project analyzes the frequency of digits in the first several digits of Pi and visualizes the distribution of these digits using bar charts. It fetches Pi digits from an external API, processes them to count the occurrence of each digit, and generates a graphical representation of the results. The tool helps to understand the distribution of digits in Pi and can be extended for further numerical analysis.

## Getting Started

To run this project locally, follow these steps:

### Requirements
You need to have the following Python libraries installed:
- `requests`
- `matplotlib`

### Installing the Requirements
To install the required libraries, run the following command:

```
pip install -r requirements.txt
```
### Usage
You can change the range of digits to analyze by modifying the parameters of the get_pi_from() function.
```
content = get_pi_from(0, 10000)
```
after retrieving the digits, you can process the data and visualize it:
```
times_by_digits, DIGITS = process_return_array(content)
bar_chart_show(DIGITS, times_by_digits)
```





