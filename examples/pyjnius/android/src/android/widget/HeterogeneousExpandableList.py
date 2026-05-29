from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeterogeneousExpandableList"]

class HeterogeneousExpandableList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/HeterogeneousExpandableList"
    getChildTypeCount = JavaMethod("()I")
    getChildType = JavaMethod("(II)I")
    getGroupType = JavaMethod("(I)I")
    getGroupTypeCount = JavaMethod("()I")