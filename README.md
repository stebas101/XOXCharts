# XOX-PointAndFigure
The goal of the **XOX-PointAndFigure** project is to create an app that displays *Point-and-Figure* charts from financial and commodity price series. In addition, it will detect patterns that can be used as part of a trading strategy.

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

### To do next:
- Add *standard* and logarithmic scales
- Select chart parameters using web form
- fix *zero-array* error
- Choose any csv file from the data folder
- Clean up chart: hide initial *status zero* column; line padding when high/low is exactly equal to box value
- Implement Close/Last only method


### Reference on *Point-and-Figure* charts:

- [Investopedia: Point and Figure Charting: A Basic Introduction](https://www.investopedia.com/articles/technical/03/081303.asp)

- Heinrich Weber, Kermit Zieg  
The Complete Point-and-Figure Charting  
Harriman House Publishing

- Jeremy du Plessis  
The Definitive Guide to Point and Figure  
Harriman House Publishing  