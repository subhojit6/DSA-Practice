class Processor:
    def run(self):
        print("Processor is running!")

class Computer:
    def __init__(self, processor):
        self.processor = processor

    def start_computer(self):
        print("Starting computer")
        self.processor.run()

processor1 = Processor()
computer1 = Computer(processor1)

computer1.start_computer()