from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CheckBoxPreference"]

class CheckBoxPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/CheckBoxPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    onBindView = JavaMethod("(Landroid/view/View;)V")