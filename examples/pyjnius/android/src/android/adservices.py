from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AdServicesState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/AdServicesState"
    isAdServicesStateEnabled = JavaStaticMethod("()Z")