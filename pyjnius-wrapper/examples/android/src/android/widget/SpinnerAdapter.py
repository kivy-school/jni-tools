from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpinnerAdapter"]

class SpinnerAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SpinnerAdapter"
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")