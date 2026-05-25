from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThemedSpinnerAdapter"]

class ThemedSpinnerAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ThemedSpinnerAdapter"
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")