from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeNotPresentException"]

class TypeNotPresentException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/TypeNotPresentException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]
    typeName = JavaMethod("()Ljava/lang/String;")