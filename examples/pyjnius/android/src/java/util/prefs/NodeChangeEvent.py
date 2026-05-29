from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NodeChangeEvent"]

class NodeChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/prefs/NodeChangeEvent"
    __javaconstructor__ = [("(Ljava/util/prefs/Preferences;Ljava/util/prefs/Preferences;)V", False)]
    getParent = JavaMethod("()Ljava/util/prefs/Preferences;")
    getChild = JavaMethod("()Ljava/util/prefs/Preferences;")