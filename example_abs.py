from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def set_payment_type():
        pass

    @abstractmethod
    def process_payment():
        pass

class RozarpayProcess(Payment):

    def set_payment_type(self):
        self.payment_method = "rozorpay"
    
    def process_payment(self):
        return self.keys = {"rozorpay"}

    def test(self):
        print("Just a test method")


paymethod = RozarpayProcess()
paymethod.test()