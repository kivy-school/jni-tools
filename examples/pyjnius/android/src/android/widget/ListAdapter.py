from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListAdapter"]

class ListAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ListAdapter"
    areAllItemsEnabled = JavaMethod("()Z")
    isEnabled = JavaMethod("(I)Z")