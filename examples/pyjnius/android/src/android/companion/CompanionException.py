from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompanionException"]

class CompanionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/CompanionException"