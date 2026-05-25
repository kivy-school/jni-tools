from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AliasActivity"]

class AliasActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AliasActivity"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")