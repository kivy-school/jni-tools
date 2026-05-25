from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableFloat"]

class MutableFloat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/MutableFloat"
    __javaconstructor__ = [("(F)V", False)]
    value = JavaField("F")