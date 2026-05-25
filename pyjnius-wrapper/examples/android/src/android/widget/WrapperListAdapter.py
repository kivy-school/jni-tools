from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrapperListAdapter"]

class WrapperListAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/WrapperListAdapter"
    getWrappedAdapter = JavaMethod("()Landroid/widget/ListAdapter;")