from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Exchanger"]

class Exchanger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Exchanger"
    __javaconstructor__ = [("()V", False)]
    exchange = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])