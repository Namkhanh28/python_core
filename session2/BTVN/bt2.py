print("--- BLOOD DONOR SCREENING SYSTEM ---")

donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE.")
    if donor_age < 18:
        print("- Reason: Donor is under 18 years old.")
    if donor_weight < 50:
        print("- Reason: Donor weight is below 50 kg.")

#Sai toán tử logic thay or bằng and ,để xét đồng thời cả hai điều kiện thì sẽ cho ra sẽ đúng với nhu cầu y tế hơn 