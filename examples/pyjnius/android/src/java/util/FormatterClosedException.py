from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormatterClosedException"]

class FormatterClosedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/FormatterClosedException"
    __javaconstructor__ = [("()V", False)]