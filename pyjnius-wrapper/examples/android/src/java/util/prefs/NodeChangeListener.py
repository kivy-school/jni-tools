from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NodeChangeListener"]

class NodeChangeListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/NodeChangeListener"
    childAdded = JavaMethod("(Ljava/util/prefs/NodeChangeEvent;)V")
    childRemoved = JavaMethod("(Ljava/util/prefs/NodeChangeEvent;)V")