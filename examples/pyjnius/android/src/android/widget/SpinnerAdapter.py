from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpinnerAdapter"]

class SpinnerAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SpinnerAdapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")