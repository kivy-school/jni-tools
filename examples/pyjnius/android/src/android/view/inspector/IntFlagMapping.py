from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntFlagMapping"]

class IntFlagMapping(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/IntFlagMapping"
    __javaconstructor__ = [("()V", False)]
    get = JavaMethod("(I)Ljava/util/Set;")
    add = JavaMethod("(IILjava/lang/String;)V")