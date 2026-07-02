# Task: Implement encapsulation using a satellite receiver example.


class SatelliteReceiver:
    def __verify_chip(self):
        print("Access card verified.")

    def __decode_signal(self):
        print("Decoding signal stream.")

    def start(self):
        print("Receiver is starting...")
        self.__verify_chip()
        self.__decode_signal()
        print("Broadcast started!")


# Testing the receiver.
receiver = SatelliteReceiver()
receiver.start()

# receiver.__decode_signal() # This will cause an AttributeError.
