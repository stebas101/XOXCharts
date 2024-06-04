XOXCharts
=========

The **XOXCharts** project has two goals: first, to preprocess time series data (prices) to help creating *Point-and-Figure* charts. On the top of that, a web app creates and visualizes the actual charts.

*Point-and-Figure* charts are offered in several financial charting software packages available commercially. However, with the exception of some high-end professional products, the version of 
*Point-and-Figure* charts provided there is a very simplified one and does not capture all the nuances and options
that this kind of charting technique can offer. Since the exact techniques and rules used for plotting in
those products can vary or be quite obscure, those charts can not be used to implement and test trading systems.

Two project has two main components:
- a class (`PnfChart`) that takes in time series data to preprocess it and
build point-and-figure charts. This library is reusable, and its output can be used for pattern recognition and
two build data analysis and machine learning projects;
- a front-end web app used to select and manage the time series data and to plot the
point-and-figure chart.

---

### Depends on:
- pandas
- NumPy
- Flask
- Flask-WTF
- WTForms

### Current features:
- Show PnF chart using existing data files
- Charts are built using the high-low method and linear scale only
- Chart parameters are still hard-coded for testing purposes

### Installation

This is a development version. To run it, makes sure the dependencies are installed and clone the repository:
```
git clone https://github.com/stebas101/XOXCharts
```
In the repository folder, run it with:
```
python run.py
```
This shoud start the server and the app should be available at the local URL:
```
http://127.0.0.1:5000/
```
Note: the app runs in *Debug* mode by default, not safe to deploy in live environments.

### How to use it

---

### TODO list:
- Chart parameters using web form
    align submit button
    form validation
    Parameters form changes with chart type
- Add logarithmic scales
- fix *zero-array* error (box size out of bounds)
- Implement Close/Last only method
- Choose any csv file from the data folder
- Handle scales with decimal box sizes (based on ***tick)
- Clean up chart: hide initial *status zero* column
- Chart graphics
- Implement SQL database for symbol and price data

---

### Reference on *Point-and-Figure* charts:

- [Investopedia: Point and Figure Charting: A Basic Introduction](https://www.investopedia.com/articles/technical/03/081303.asp)

- Heinrich Weber, Kermit Zieg  
The Complete Point-and-Figure Charting  
Harriman House Publishing

- Jeremy du Plessis  
The Definitive Guide to Point and Figure  
Harriman House Publishing  
