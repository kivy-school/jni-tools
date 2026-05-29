from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdServicesState"]

class AdServicesState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/AdServicesState"
    isAdServicesStateEnabled = JavaStaticMethod("()Z")