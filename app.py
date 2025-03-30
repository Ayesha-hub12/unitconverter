import streamlit as st






# unit converter
# input for unit converter application
# output given by unit con app

#innput
# 1 Value
# 2 unit from convertion/ 
# 3 unit to convertion





def convert_units(value: float, unit_from: str, unit_to: str):
    # 1 kilometer = 1000 meter 
    # 1 meter = 0.001 kilometer 
    # 1 kilogram = 1000 gram 
    # 1 gram = 0.001 kilogram 

    if unit_from == "kilometers" and unit_to == "meters":
     return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
     return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
     return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
     return value * 0.001
    else:
     return "Conversion is not supported!"

# result output ki value
# result1 = convert_units(1.5, "kilometers", "meters")
# print("the result in meters is", result1)
# result2 = convert_units(5000,"grams","kilograms")
# print("the value in kilograms is" , result2)




def main():
 st.title("Unit Converter")
 st.header("welcome to unit converter!")
main()
value = st.number_input("Enter the value you want to convert:",min_value=0.0)
unit_from = st.text_input("Enter the unit you want to convert from:(e.g . meters, kilometers, grams, kilograms)")
unit_to = st.text_input("Enter the unit you want from convertion: (e.g . meters, kilometers, grams, kilograms)")

if st.button("convert"):
    result = convert_units(value, unit_from,unit_to)
    st.write("converted value is :", result)


# result = convert_units(value, unit_from,unit_to)
# st.write("converted value is :", result)

# value = float(input("Enter the value you want to convert:"))
# unit_from = input("Enter the unit you want to convert from:(e.g . meters, kilometers, grams, kilograms)")
# unit_to = input("Enter the unit you want from convertion: (e.g . meters, kilometers, grams, kilograms)")
# print("value>>>",value)
# print("unit_to>>>",unit_to)
# print("unit_from",unit_from)
# result = convert_units(value, unit_from,unit_to)
# print("converted value is :", result)
