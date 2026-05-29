from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filterable"]

class Filterable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Filterable"
    getFilter = JavaMethod("()Landroid/widget/Filter;")