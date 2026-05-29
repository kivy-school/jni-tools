from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThemedSpinnerAdapter"]

class ThemedSpinnerAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ThemedSpinnerAdapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")