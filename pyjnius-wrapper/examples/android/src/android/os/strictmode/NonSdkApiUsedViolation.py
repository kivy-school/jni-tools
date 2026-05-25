from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NonSdkApiUsedViolation"]

class NonSdkApiUsedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/NonSdkApiUsedViolation"