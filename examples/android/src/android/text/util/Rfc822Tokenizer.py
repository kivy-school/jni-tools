from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rfc822Tokenizer"]

class Rfc822Tokenizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Rfc822Tokenizer"
    __javaconstructor__ = [("()V", False)]
    tokenize = JavaMultipleMethod([("(Ljava/lang/CharSequence;Ljava/util/Collection;)V", True, False), ("(Ljava/lang/CharSequence;)[Landroid/text/util/Rfc822Token;", True, False)])
    findTokenStart = JavaMethod("(Ljava/lang/CharSequence;I)I")
    findTokenEnd = JavaMethod("(Ljava/lang/CharSequence;I)I")
    terminateToken = JavaMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")