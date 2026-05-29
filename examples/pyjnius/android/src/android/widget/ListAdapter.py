from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListAdapter"]

class ListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ListAdapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    isEnabled = JavaMethod("(I)Z")
    areAllItemsEnabled = JavaMethod("()Z")