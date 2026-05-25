from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamField"]

class ObjectStreamField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamField"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Class;)V", False), ("(Ljava/lang/String;Ljava/lang/Class;Z)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/Class;")
    getTypeCode = JavaMethod("()C")
    getTypeString = JavaMethod("()Ljava/lang/String;")
    getOffset = JavaMethod("()I")
    setOffset = JavaMethod("(I)V")
    isPrimitive = JavaMethod("()Z")
    isUnshared = JavaMethod("()Z")
    compareTo = JavaMethod("(Ljava/lang/Object;)I")
    toString = JavaMethod("()Ljava/lang/String;")