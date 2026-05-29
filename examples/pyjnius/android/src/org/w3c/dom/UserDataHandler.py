from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserDataHandler"]

class UserDataHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/UserDataHandler"
    NODE_CLONED = JavaStaticField("S")
    NODE_IMPORTED = JavaStaticField("S")
    NODE_DELETED = JavaStaticField("S")
    NODE_RENAMED = JavaStaticField("S")
    NODE_ADOPTED = JavaStaticField("S")
    handle = JavaMethod("(SLjava/lang/String;Ljava/lang/Object;Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;)V")