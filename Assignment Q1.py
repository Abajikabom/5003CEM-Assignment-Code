import random

def folding_hash(ic_number, table_size):
    part1 = int(ic_number[0:4])
    part2 = int(ic_number[4:8])
    part3 = int(ic_number[8:12])
    folded_sum = part1 + part2 + part3
    return folded_sum % table_size

def generate_random_ic():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

def insert_and_print_table(ic_numbers, table_size):
    hash_table = [[] for _ in range(table_size)]
    collisions = 0

    for ic in ic_numbers:
        index = folding_hash(ic, table_size)
        if hash_table[index]:  
            collisions += 1
        hash_table[index].append(ic)

    print(f"\nHash Table with size {table_size}:")
    for i in range(table_size):
        if hash_table[i]:
            chain = ' --> '.join(hash_table[i])
            print(f"table[{i}] --> {chain}")
        else:
            print(f"table[{i}]")
    return collisions

def run_simulation():
    num_ic = 1000
    table_sizes = [1009, 3001]
    ic_numbers = [generate_random_ic() for _ in range(num_ic)]
    collisions_per_table = []

    for size in table_sizes:
        collisions = insert_and_print_table(ic_numbers, size)
        collisions_per_table.append(collisions)

    print()
    for idx, size in enumerate(table_sizes):
        total_collisions = collisions_per_table[idx]
        collision_rate = (total_collisions / num_ic) * 100
        label = "Smaller" if idx == 0 else "Bigger"
        print(f"Total collisions for {label} Hash Table: {total_collisions}")
        print(f"Collision Rate for {label} Hash Table: {collision_rate:.2f} %")

if __name__ == "__main__":
    run_simulation()
