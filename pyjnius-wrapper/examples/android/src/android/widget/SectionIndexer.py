from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SectionIndexer"]

class SectionIndexer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SectionIndexer"
    getSections = JavaMethod("()[Ljava/lang/Object;")
    getPositionForSection = JavaMethod("(I)I")
    getSectionForPosition = JavaMethod("(I)I")