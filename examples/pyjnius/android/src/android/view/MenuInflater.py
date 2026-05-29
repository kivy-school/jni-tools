from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MenuInflater"]

class MenuInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/MenuInflater"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    inflate = JavaMethod("(ILandroid/view/Menu;)V")