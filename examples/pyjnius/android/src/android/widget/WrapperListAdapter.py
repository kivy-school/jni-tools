from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrapperListAdapter"]

class WrapperListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/WrapperListAdapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    getWrappedAdapter = JavaMethod("()Landroid/widget/ListAdapter;")