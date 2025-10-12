""" 
Exercise 7.1-3 
English: Justify that average-case running time of PARTITION on n elements is Θ(n).
Polish: Uzasadnij, że średni czas działania PARTITION dla n elementów wynosi Θ(n).
""" 

def partition_average_case():
    return "Θ(n), since each element is compared to pivot once."

if __name__ == "__main__":
    print("Exercise 7.1-3 Result:")
    print(partition_average_case())
