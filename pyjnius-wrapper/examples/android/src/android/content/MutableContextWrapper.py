from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MutableContextWrapper"]

class MutableContextWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/MutableContextWrapper"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    setBaseContext = JavaMethod("(Landroid/content/Context;)V")