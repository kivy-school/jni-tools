from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Modifier"]

class Modifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Modifier"
    __javaconstructor__ = [("()V", False)]
    ABSTRACT = JavaStaticField("I")
    FINAL = JavaStaticField("I")
    INTERFACE = JavaStaticField("I")
    NATIVE = JavaStaticField("I")
    PRIVATE = JavaStaticField("I")
    PROTECTED = JavaStaticField("I")
    PUBLIC = JavaStaticField("I")
    STATIC = JavaStaticField("I")
    STRICT = JavaStaticField("I")
    SYNCHRONIZED = JavaStaticField("I")
    TRANSIENT = JavaStaticField("I")
    VOLATILE = JavaStaticField("I")
    isPublic = JavaStaticMethod("(I)Z")
    isPrivate = JavaStaticMethod("(I)Z")
    isProtected = JavaStaticMethod("(I)Z")
    isStatic = JavaStaticMethod("(I)Z")
    isFinal = JavaStaticMethod("(I)Z")
    isSynchronized = JavaStaticMethod("(I)Z")
    isVolatile = JavaStaticMethod("(I)Z")
    isTransient = JavaStaticMethod("(I)Z")
    isNative = JavaStaticMethod("(I)Z")
    isInterface = JavaStaticMethod("(I)Z")
    isAbstract = JavaStaticMethod("(I)Z")
    isStrict = JavaStaticMethod("(I)Z")
    toString = JavaStaticMethod("(I)Ljava/lang/String;")
    classModifiers = JavaStaticMethod("()I")
    interfaceModifiers = JavaStaticMethod("()I")
    constructorModifiers = JavaStaticMethod("()I")
    methodModifiers = JavaStaticMethod("()I")
    fieldModifiers = JavaStaticMethod("()I")
    parameterModifiers = JavaStaticMethod("()I")