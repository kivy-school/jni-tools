from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipboardManager"]

class ClipboardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/ClipboardManager"
    __javaconstructor__ = [("()V", False)]
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    setText = JavaMethod("(Ljava/lang/CharSequence;)V")
    hasText = JavaMethod("()Z")