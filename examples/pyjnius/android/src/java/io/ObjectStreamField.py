from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamField"]

class ObjectStreamField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamField"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Class;Z)V", False), ("(Ljava/lang/String;Ljava/lang/Class;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    compareTo = JavaMethod("(Ljava/lang/Object;)I")
    isPrimitive = JavaMethod("()Z")
    getType = JavaMethod("()Ljava/lang/Class;")
    getTypeCode = JavaMethod("()C")
    getTypeString = JavaMethod("()Ljava/lang/String;")
    getOffset = JavaMethod("()I")
    isUnshared = JavaMethod("()Z")