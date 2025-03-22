import streamlit as st

# 🌍 Title and Description with emojis 🎯
st.title("🌍 Unit Converter App")

st.markdown("### 🔢 Convert Length, Weight, Temperature, and Time Units")

# 📌 User selects conversion type
conversion_type = st.selectbox(
    "👋 Welcome! Select the conversion type below:📌",
    ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "⏳ Time"]
)

# 🔄 Function to handle unit conversion
def convert_unit(category, value, from_unit):
    if category == "📏 Length":
        length_units = {
            "Kilometers to Meters": value * 1000,
            "Meters to Kilometers": value / 1000,
            "Meters to Centimeters": value * 100,
            "Centimeters to Meters": value / 100,
            "Meters to Millimeters": value * 1000,
            "Millimeters to Meters": value / 1000,
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371,
            "Feet to Meters": value * 0.3048,
            "Meters to Feet": value / 0.3048,
            "Inches to Centimeters": value * 2.54,
            "Centimeters to Inches": value / 2.54,
            "Yards to Meters": value * 0.9144,
            "Meters to Yards": value / 0.9144
        }
        return length_units.get(from_unit, "❌ Invalid conversion")

    elif category == "⚖️ Weight":
        weight_units = {
            "Kilograms to Grams": value * 1000,
            "Grams to Kilograms": value / 1000,
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462,
            "Kilograms to Ounces": value * 35.274,
            "Ounces to Kilograms": value / 35.274,
            "Grams to Ounces": value / 28.3495,
            "Ounces to Grams": value * 28.3495,
            "Pounds to Ounces": value * 16,
            "Ounces to Pounds": value / 16,
            "Tons to Kilograms": value * 1000,
            "Kilograms to Tons": value / 1000
        }
        return weight_units.get(from_unit, "❌ Invalid conversion")

    elif category == "⏳ Time":
        time_units = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Seconds": value * 3600,
            "Seconds to Hours": value / 3600,
            "Days to Hours": value * 24,
            "Hours to Days": value / 24
        }
        return time_units.get(from_unit, "❌ Invalid conversion")

    elif category == "🌡️ Temperature":
        if from_unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius to Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin to Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return "❌ Invalid conversion"

# 📌 User selects the specific unit conversion based on category
if conversion_type == "📏 Length":
    unit = st.selectbox("📏 Select Unit", [
        "Kilometers to Meters", "Meters to Kilometers",
        "Meters to Centimeters", "Centimeters to Meters",
        "Meters to Millimeters", "Millimeters to Meters",
        "Kilometers to Miles", "Miles to Kilometers",
        "Feet to Meters", "Meters to Feet",
        "Inches to Centimeters", "Centimeters to Inches",
        "Yards to Meters", "Meters to Yards"
    ])

elif conversion_type == "⚖️ Weight":
    unit = st.selectbox("⚖️ Select Unit", [
        "Kilograms to Grams", "Grams to Kilograms",
        "Kilograms to Pounds", "Pounds to Kilograms",
        "Kilograms to Ounces", "Ounces to Kilograms",
        "Grams to Ounces", "Ounces to Grams",
        "Pounds to Ounces", "Ounces to Pounds",
        "Tons to Kilograms", "Kilograms to Tons"
    ])

elif conversion_type == "🌡️ Temperature":
    unit = st.selectbox("🌡️ Select Unit", [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius",
        "Celsius to Kelvin", "Kelvin to Celsius",
        "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"
    ])

elif conversion_type == "⏳ Time":
    unit = st.selectbox("⏳ Select Unit", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Seconds", "Seconds to Hours",
        "Days to Hours", "Hours to Days"
    ])

# 🔢 User inputs a value to convert
value = st.number_input("🔢 Enter Value", min_value=0.0)

# 🚀 Conversion button
if st.button("Convert"):
    result = convert_unit(conversion_type, value, unit)
    
    if isinstance(result, str):
        st.error("❌ Invalid conversion selected. Please try again.")
    else:
        st.success(f"✅ The result for the given value is: {result:.2f}")
