from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipboardManager"]

class ClipboardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/ClipboardManager"
    __javaconstructor__ = [("()V", False)]
    hasText = JavaMethod("()Z")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    setText = JavaMethod("(Ljava/lang/CharSequence;)V")