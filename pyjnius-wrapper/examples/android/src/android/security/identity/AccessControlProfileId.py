from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessControlProfileId"]

class AccessControlProfileId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AccessControlProfileId"
    __javaconstructor__ = [("(I)V", False)]
    getId = JavaMethod("()I")