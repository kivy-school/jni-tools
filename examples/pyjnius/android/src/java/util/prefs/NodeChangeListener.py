from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NodeChangeListener"]

class NodeChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/NodeChangeListener"
    childAdded = JavaMethod("(Ljava/util/prefs/NodeChangeEvent;)V")
    childRemoved = JavaMethod("(Ljava/util/prefs/NodeChangeEvent;)V")