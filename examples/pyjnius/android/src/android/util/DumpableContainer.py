from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DumpableContainer"]

class DumpableContainer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/DumpableContainer"
    addDumpable = JavaMethod("(Landroid/util/Dumpable;)Z")
    removeDumpable = JavaMethod("(Landroid/util/Dumpable;)Z")