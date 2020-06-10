import abc
class User:
    def __init__(self,type):
        self.type = type
    
    def isAdmin(self):
        return self.type == "admin"
    
    def isAuthor(self):
        return self.type == "author"


class Document:
    def __init__(self,state):
        self.state = state
        self.state.define_document(self)
  
    def render(self,user):
        self.state.render(user)
    
    def publish(self,user):
        self.state.publish(user)

    def failedReview(self):
        self.state.failedReview()
    
    def expiredPublication(self):
        self.state.expiredPublication()

    def changeState(self,new_state):
        self.state = new_state
        self.state.define_document(self)


class State():
    
  
    def document(self):
        return self.document

    
    def define_document(self, document):
        self.document = document

    @abc.abstractmethod
    def render(self,user):
        pass
    
    @abc.abstractmethod
    def publish(self,user):
        pass
    

class DraftState(State):

    def render(self,user):
        if(user.isAdmin() or user.isAuthor()):
            self.document.changeState(ModerationState())
            print("O documento foi renderizado")
        else:
            print("Você nao tem autorizacao para renderizar o documento.")
    
    def publish(self,user):
        if(user.isAdmin()):
            self.document.changeState(PublishedState())
            print("O documento foi publicado")
        else:
            print("Você nao tem autorizacao para publicar o documento.")

class ModerationState(State):
    

    def failedReview(self):
        self.document.changeState(DraftState())
        print("A revisão falhou")
    
    def publish(self,user):
        if(user.isAdmin()):
            self.document.changeState(PublishedState())
            print("O documento foi publicado")
        else:
            print("Você nao tem autorizacao para publicar o documento.")

class PublishedState(State):
    
    def expiredPublication(self):
        self.document.changeState(DraftState())
        print("O tempo de publicacao expirou")


admin = User("admin")
author = User("author")
user = User("user")

initialState = DraftState()
document = Document(initialState)

document.render(user)
document.render(author)
document.failedReview()
document.render(admin)
document.publish(author)
document.publish(admin)
document.expiredPublication()
document.publish(author)
document.publish(admin)

