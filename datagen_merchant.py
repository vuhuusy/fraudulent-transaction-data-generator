import os
import argparse
import random
from faker import Factory

def generate_merchants(output_dir):
    fake = Factory.create('en_US')
    category_list = [
        "gas_transport", "grocery_net", "grocery_pos", "pharmacy",
        "misc_net", "misc_pos", "shopping_net", "shopping_pos",
        "utilities", "entertainment", "food_dining", "health_fitness",
        "home", "kids_pets", "personal_care", "travel"
    ]

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "merchants.csv")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("id|name|category\n")
        merchant_id = 1
        for c in category_list:
            num_merchants = random.randint(20, 100)
            for _ in range(num_merchants):
                name = fake.company()
                f.write(f"{merchant_id}|{name}|{c}\n")
                merchant_id += 1

    print(f"✅ Merchants generated at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake merchant data per category.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output directory for merchants.csv")
    args = parser.parse_args()

    generate_merchants(args.output)
