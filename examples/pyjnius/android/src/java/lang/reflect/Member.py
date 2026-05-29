from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Member"]

class Member(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Member"
    PUBLIC = JavaStaticField("I")
    DECLARED = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    isSynthetic = JavaMethod("()Z")
    accessFlags = JavaMethod("()Ljava/util/Set;")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")