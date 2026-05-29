from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateTimeParseException"]

class DateTimeParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/DateTimeParseException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/CharSequence;I)V", False), ("(Ljava/lang/String;Ljava/lang/CharSequence;ILjava/lang/Throwable;)V", False)]
    getErrorIndex = JavaMethod("()I")
    getParsedString = JavaMethod("()Ljava/lang/String;")