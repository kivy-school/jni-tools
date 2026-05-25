from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ref"]

class Ref(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Ref"
    getBaseTypeName = JavaMethod("()Ljava/lang/String;")
    getObject = JavaMultipleMethod([("(Ljava/util/Map;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    setObject = JavaMethod("(Ljava/lang/Object;)V")