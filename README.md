# ATR Coverage Calculator
By providing ATR and Tag height values, this program will calculate the probable coverage area for a single ATR 7000.

This is version 3.0.3, written by Craig D'Costa using Python 3.9.6 and released on February 7 2022. 

The area calculation formulas implemented are available on pages 22 and 23 of the ZAATS Deployment User Guide.

## Version History

### 3.0.3
###### Monday February 7 2022
1. Added "ATR Height Override" feature. When this feature is enabled, accepted ATR height value is anything greater than 0.

### 3.0.2
###### September 14 2021
1. Resolved a bug in which if a subsequent calculation was performed before the reset button was clicked, displayed calculations were not being removed when the reset button was clicked.

### 3.0.1
###### September 14 2021
1. Resolved a bug in which displayed calculations were not being removed when the reset button was clicked.

### 3.0.0
###### September 10 2021
1. Version with a Graphical User Interface (GUI). Original command line version retained.

### 2.0.0
###### August 31 2021
1. Add check to determine if file is being called explicitly.
2. Add support for Metric and Imperial System of Measurment.
3. Add support for Tag Height.
4. Update coverage calculations to include the Typical and Max Accuracy calculations.
5. Moved calculation results printout to separate function.
6. Updated results printout to include the Unit of Measurment and squared superscript.
7. Updated display/output for prettier appearance.

### 1.0.0 - Initial Release
###### August 9 2021
1. Written using a base provided by L. Yatras and J. Yatras.