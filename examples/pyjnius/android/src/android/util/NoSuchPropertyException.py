from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchPropertyException"]

class NoSuchPropertyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/NoSuchPropertyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]