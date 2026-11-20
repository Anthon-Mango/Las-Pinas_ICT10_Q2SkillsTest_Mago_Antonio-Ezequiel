
from pyscript import display, document

non_metals = {
    "Hydrogen": {"symbol": "H", "number": 1, "mass": 1.008},
    "Helium": {"symbol": "He", "number": 2, "mass": 4.0026},
    "Carbon": {"symbol": "C", "number": 6, "mass": 12.011},
    "Nitrogen": {"symbol": "N", "number": 7, "mass": 14.007},
    "Oxygen": {"symbol": "O", "number": 8, "mass": 15.999},
    "Fluorine": {"symbol": "F", "number": 9, "mass": 18.998},
    "Neon": {"symbol": "Ne", "number": 10, "mass": 20.180},
    "Phosphorus": {"symbol": "P", "number": 15, "mass": 30.974},
    "Sulfur": {"symbol": "S", "number": 16, "mass": 32.06},
    "Chlorine": {"symbol": "Cl", "number": 17, "mass": 35.45},
    "Argon": {"symbol": "Ar", "number": 18, "mass": 39.948},
    "Selenium": {"symbol": "Se", "number": 34, "mass": 78.971},
    "Bromine": {"symbol": "Br", "number": 35, "mass": 79.904},
    "Krypton": {"symbol": "Kr", "number": 36, "mass": 83.798},
    "Iodine": {"symbol": "I", "number": 53, "mass": 126.904},
    "Xenon": {"symbol": "Xe", "number": 54, "mass": 131.293},
    "Astatine": {"symbol": "At", "number": 85, "mass": 210},
    "Radon": {"symbol": "Rn", "number": 86, "mass": 222},
    "Tennessine": {"symbol": "Ts", "number": 117, "mass": 294}
}


def check_element(e):
    document.getElementById("result").innerHTML = ""

    element = document.getElementById("element").value.strip().title()

    # Using .get()
    details = non_metals.get(element)

    if details is not None:

        document.getElementById("result").innerHTML = f"""
            <h3>Nonmetal Element Found!</h3>
            <b>Element:</b> {element}<br>
            <b>Symbol:</b> {details["symbol"]}<br>
            <b>Atomic Number:</b> {details["number"]}<br>
            <b>Atomic Mass:</b> {details["mass"]}
        """

    else:
        document.getElementById("result").innerHTML = """
            <b>Element not found!</b><br>
            Please enter a valid nonmetal element.
        """
