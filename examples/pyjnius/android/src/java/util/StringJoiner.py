from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringJoiner"]

class StringJoiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/StringJoiner"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Ljava/lang/CharSequence;)V", False)]
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    add = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/StringJoiner;")
    merge = JavaMethod("(Ljava/util/StringJoiner;)Ljava/util/StringJoiner;")
    setEmptyValue = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/StringJoiner;")