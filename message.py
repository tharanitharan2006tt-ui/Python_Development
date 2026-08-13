class Smsnotification:
    def send(self, message):
        print(f"notification send {message}")
class Emailnotification:
    def send(self, message):
        print(f"email send {message}")
class Whatsappnotification:
    def send(self, message):
        print(f"whatsapp send {message}")
class Notification:
    def notify(self,Notification,message):
        Notification.send(message)

S=Smsnotification()
E=Emailnotification()
W=Whatsappnotification()
n=Notification()
n.notify(S,"Hello")
n.notify(E,"Hello")
n.notify(W,"Hello")