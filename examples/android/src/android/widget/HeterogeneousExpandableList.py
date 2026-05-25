from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeterogeneousExpandableList"]

class HeterogeneousExpandableList(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/HeterogeneousExpandableList"
    getGroupType = JavaMethod("(I)I")
    getChildType = JavaMethod("(II)I")
    getGroupTypeCount = JavaMethod("()I")
    getChildTypeCount = JavaMethod("()I")