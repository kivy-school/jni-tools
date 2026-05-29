from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnumConstantNotPresentException"]

class EnumConstantNotPresentException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/EnumConstantNotPresentException"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/String;)V", False)]
    enumType = JavaMethod("()Ljava/lang/Class;")
    constantName = JavaMethod("()Ljava/lang/String;")