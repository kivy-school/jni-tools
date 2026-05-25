from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationOpenedReceiver"]

class NotificationOpenedReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/NotificationOpenedReceiver"
    __javaconstructor__ = [("()V", False)]