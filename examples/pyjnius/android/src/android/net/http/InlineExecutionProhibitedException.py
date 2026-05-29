from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineExecutionProhibitedException"]

class InlineExecutionProhibitedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/InlineExecutionProhibitedException"
    __javaconstructor__ = [("()V", False)]