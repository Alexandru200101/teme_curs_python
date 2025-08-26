class IDGenerator:
    counter = 0

    @staticmethod
    def next_id():
        IDGenerator.counter += 1
        return IDGenerator.counter
if __name__ == "__main__":
    print("Primele 5 ID-uri generate:")
    for _ in range(5):
        print(IDGenerator.next_id())
