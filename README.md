# ATR Coverage Calculator
By providing ATR and Tag height values, this program will calculate the probable coverage area for a single ATR 7000.

This is version 2.0.0, written by Craig D'Costa using Python 3.9.6 on August 31 2021. 

The area calculation formulas implemented are available on pages 22 and 23 of the ZAATS Deployment User Guide.

## Version History

### 2.0.0
###### August 31 2021
1. Add check to determine if file is being called explicitly.
2. Add support for Metric and Imperial System of Measurment.
3. Update coverage calculations to include the Typical and Max Accuracy calculations.
4. Moved calculation results printout to separate function.
5. Updated results printout to include the Unit of Measurment and squared superscript.
6. Updated dispaly/output for prettier appearance.

### 1.0.0 - Initial Release
###### August 9 2021
1. Written using a base provided by L. Yatras and J. Yatras.