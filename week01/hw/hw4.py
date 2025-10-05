name: str = input("Enter your name: ")
score: int = int(input("Enter your score: "))
if score >= 90:
    print(f"{name} : Excellent🎉 ")
elif 70 <= score < 90:
    print(f"{name} : Good👍 ")
elif score < 70:
    print(f"{name} : Needs Improvement👎 ")
