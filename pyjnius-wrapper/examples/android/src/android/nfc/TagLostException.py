from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TagLostException"]

class TagLostException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/TagLostException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]