from mailer import Mailer
from mailer import Message

message = Message(From="tiago.cnorberto@pbh.gov.br", To=["tiago.cnorberto@pbh.gov.br"])
message.Subject = "Kitty with dynamite"
message.Body = """Kitty go boom!"""
message.attach("kitty.jpg")

sender = Mailer('10.0.25.19')
sender.send(message)