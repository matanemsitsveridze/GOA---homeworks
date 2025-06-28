Vending_machine = ["phone","TV","mouse","keyboard","chair","desk","glasses","umbrella","coca-cola","treasure"]
number = int(input("ჩაწერეთ ამოსარჩევი ციფრი: "))
for i in range(10):
    if i == number:
        print(Vending_machine[i])