from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdServicesException"]

class AdServicesException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/exceptions/AdServicesException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False)]