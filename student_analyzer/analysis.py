import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")

print(df.head())

print(df.describe())

print(df.info())

print(df.columns)
print("Average Maths:", df["Maths"].mean())
print("Max Physics:", df["Physics"].max())
print("Min Study Hours:", df["Hours_Studied"].min())

df["Total"] = df["Maths"] + df["Physics"] + df["Chemistry"]

print(df[["Name", "Total"]])

df["average"]=df["Total"]/3

print(df[["Name" , "average"]])

topper = df.loc[df["Total"].idxmax()]

print(topper)

losser = df.loc[df["Total"].idxmin()]

print(losser)


print("\n--- Top 3 Students ---")
print(df.head(3)[["Name", "Total"]])


weak_students = df[df["Average"] < 70]

print("\n--- Students Needing Improvement ---")
print(weak_students[["Name", "Average"]])


plt.bar(df["Name"],df["Total"])
plt.xlabel("students")
plt.ylabel("total marks")
plt.title("student performace")

plt.show()

colors = ["blue"] * len(df)
colors[df["Total"].idxmax()] = "red"

plt.bar(df["Name"], df["Total"], color=colors)
plt.show()


plt.scatter(df["Hours_Studied"], df["Total"])
plt.xlabel("Hours Studied")
plt.ylabel("Total Marks")
plt.title("Study Hours vs Marks")
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()