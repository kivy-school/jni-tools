from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Member"]

class Member(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Member"
    DECLARED = JavaStaticField("I")
    PUBLIC = JavaStaticField("I")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    getName = JavaMethod("()Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    isSynthetic = JavaMethod("()Z")