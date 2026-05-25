from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DumpableContainer"]

class DumpableContainer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/DumpableContainer"
    addDumpable = JavaMethod("(Landroid/util/Dumpable;)Z")
    removeDumpable = JavaMethod("(Landroid/util/Dumpable;)Z")