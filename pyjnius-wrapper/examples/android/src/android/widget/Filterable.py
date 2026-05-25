from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filterable"]

class Filterable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Filterable"
    getFilter = JavaMethod("()Landroid/widget/Filter;")