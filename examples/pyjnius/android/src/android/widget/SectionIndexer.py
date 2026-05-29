from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SectionIndexer"]

class SectionIndexer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SectionIndexer"
    getPositionForSection = JavaMethod("(I)I")
    getSectionForPosition = JavaMethod("(I)I")
    getSections = JavaMethod("()[Ljava/lang/Object;")