from Klasy import student as st

kuba = st.Student("Jakub", [90, 40, 50, 50, 40, 50, 50, 50, 50])
print(kuba.is_passed())

michal = st.Student("Michal", [30, 20, 20, 30, 20, 70, 30, 10, 10])
print(michal.is_passed())
